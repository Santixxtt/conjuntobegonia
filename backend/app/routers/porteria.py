from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timezone

from app.database import get_db
from app.models.paqueteria_model import Paquete
from app.models.visita_model import Visita
from app.models.usuario_model import Usuario
from app.schemas.porteria_schema import (
    PaqueteCreate, PaqueteResponse, VisitaCreate, VisitaResponse
)
from app.dependencias import get_current_user

router = APIRouter(prefix="/porteria", tags=["Portería (Paquetes y Visitas)"])

def verificar_permiso_porteria(usuario: Usuario):
    """Dependencia auxiliar para bloquear el paso a residentes al crear registros"""
    if usuario.rol not in ["Admin", "Porteria"]:
        raise HTTPException(status_code=403, detail="Acceso exclusivo para Portería y Administración")

# RUTAS DE PAQUETERÍA

@router.post("/paquetes", response_model=PaqueteResponse, status_code=status.HTTP_201_CREATED)
def registrar_paquete(
    paquete: PaqueteCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    verificar_permiso_porteria(current_user)
    nuevo_paquete = Paquete(
        apartamento_id=paquete.apartamento_id,
        descripcion=paquete.descripcion
    )
    db.add(nuevo_paquete)
    db.commit()
    db.refresh(nuevo_paquete)
    return nuevo_paquete

@router.get("/paquetes", response_model=List[PaqueteResponse])
def obtener_paquetes(
    skip: int = 0, limit: int = 50, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    if current_user.rol in ["Admin", "Porteria"]:
        return db.query(Paquete).order_by(Paquete.fecha_recepcion.desc()).offset(skip).limit(limit).all()
    
    # Si es residente, solo ve los paquetes de su propio apartamento
    if current_user.apartamento_id is None:
        return [] # Residente sin apartamento asignado
        
    return db.query(Paquete).filter(Paquete.apartamento_id == current_user.apartamento_id).order_by(Paquete.fecha_recepcion.desc()).offset(skip).limit(limit).all()

@router.put("/paquetes/{paquete_id}/entregar", response_model=PaqueteResponse)
def marcar_paquete_entregado(
    paquete_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    verificar_permiso_porteria(current_user)
    paquete = db.query(Paquete).filter(Paquete.id == paquete_id).first()
    
    if not paquete:
        raise HTTPException(status_code=404, detail="Paquete no encontrado")
    if paquete.estado == "Entregado":
        raise HTTPException(status_code=400, detail="El paquete ya fue entregado previamente")
        
    paquete.estado = "Entregado"
    paquete.fecha_entrega = datetime.now(timezone.utc)
    db.commit()
    db.refresh(paquete)
    return paquete

# RUTAS DE VISITAS

@router.post("/visitas", response_model=VisitaResponse, status_code=status.HTTP_201_CREATED)
def registrar_visita(
    visita: VisitaCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    verificar_permiso_porteria(current_user)
    nueva_visita = Visita(
        apartamento_id=visita.apartamento_id,
        nombre_visitante=visita.nombre_visitante,
        cedula_visitante=visita.cedula_visitante
    )
    db.add(nueva_visita)
    db.commit()
    db.refresh(nueva_visita)
    return nueva_visita

@router.get("/visitas", response_model=List[VisitaResponse])
def obtener_visitas(
    skip: int = 0, limit: int = 50, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    if current_user.rol in ["Admin", "Porteria"]:
        return db.query(Visita).order_by(Visita.fecha_ingreso.desc()).offset(skip).limit(limit).all()
        
    if current_user.apartamento_id is None:
        return []
        
    return db.query(Visita).filter(Visita.apartamento_id == current_user.apartamento_id).order_by(Visita.fecha_ingreso.desc()).offset(skip).limit(limit).all()