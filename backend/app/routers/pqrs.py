from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.pqrs_model import PQRS
from app.models.usuario_model import Usuario
from app.schemas.pqrs_schema import PQRSCreate, PQRSResponse, EstadoPQRSEnum
from app.dependencias import get_current_user

router = APIRouter(prefix="/pqrs", tags=["PQRS"])

@router.post("/", response_model=PQRSResponse, status_code=status.HTTP_201_CREATED)
def crear_pqrs(
    pqrs: PQRSCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user) # Exige login
):
    nueva_pqrs = PQRS(
        usuario_id=current_user.id,
        tipo=pqrs.tipo,
        descripcion=pqrs.descripcion,
        prioridad=pqrs.prioridad
    )
    db.add(nueva_pqrs)
    db.commit()
    db.refresh(nueva_pqrs)
    return nueva_pqrs

@router.get("/", response_model=List[PQRSResponse])
def obtener_pqrs(
    skip: int = 0, 
    limit: int = 50, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    # LÓGICA DE ROLES: 
    # El Admin ve todo. Los demás solo ven sus propios casos.
    if current_user.rol == "Admin":
        casos = db.query(PQRS).order_by(PQRS.fecha_creacion.desc()).offset(skip).limit(limit).all()
    else:
        casos = db.query(PQRS).filter(PQRS.usuario_id == current_user.id).order_by(PQRS.fecha_creacion.desc()).offset(skip).limit(limit).all()
    
    return casos

@router.put("/{pqrs_id}/estado", response_model=PQRSResponse)
def actualizar_estado_pqrs(
    pqrs_id: int,
    nuevo_estado: EstadoPQRSEnum,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    # Solo administración puede cambiar el estado de un ticket
    if current_user.rol != "Admin":
        raise HTTPException(status_code=403, detail="Sin permisos para actualizar estados")
        
    pqrs = db.query(PQRS).filter(PQRS.id == pqrs_id).first()
    if not pqrs:
        raise HTTPException(status_code=404, detail="Caso no encontrado")
        
    pqrs.estado = nuevo_estado
    db.commit()
    db.refresh(pqrs)
    return pqrs