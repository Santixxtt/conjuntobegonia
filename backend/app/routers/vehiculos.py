from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.vehiculo_model import Vehiculo
from app.models.usuario_model import Usuario
from app.schemas.vehiculo_schema import VehiculoCreate, VehiculoResponse
from app.dependencias import get_current_user

router = APIRouter(prefix="/vehiculos", tags=["Vehículos y Parqueaderos"])

@router.post("/", response_model=VehiculoResponse, status_code=status.HTTP_201_CREATED)
def registrar_vehiculo(
    vehiculo: VehiculoCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    # Validar que no existan placas duplicadas en el conjunto
    vehiculo_existente = db.query(Vehiculo).filter(Vehiculo.placa == vehiculo.placa).first()
    if vehiculo_existente:
        raise HTTPException(status_code=400, detail="Esta placa ya se encuentra registrada en el sistema")

    nuevo_vehiculo = Vehiculo(
        usuario_id=current_user.id,
        placa=vehiculo.placa,
        tipo=vehiculo.tipo,
        # Si un residente crea el vehículo, el parqueadero queda en None hasta que el Admin lo asigne.
        # Si el Admin lo crea, puede asignarlo de inmediato.
        parqueadero_asignado=vehiculo.parqueadero_asignado if current_user.rol == "Admin" else None
    )
    db.add(nuevo_vehiculo)
    db.commit()
    db.refresh(nuevo_vehiculo)
    return nuevo_vehiculo

@router.get("/", response_model=List[VehiculoResponse])
def obtener_vehiculos(
    skip: int = 0, limit: int = 50,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    """El Administrador ve todos los vehículos, el Residente solo los suyos."""
    if current_user.rol == "Admin":
        return db.query(Vehiculo).offset(skip).limit(limit).all()
        
    return db.query(Vehiculo).filter(Vehiculo.usuario_id == current_user.id).offset(skip).limit(limit).all()

@router.put("/{vehiculo_id}/asignar-parqueadero", response_model=VehiculoResponse)
def asignar_parqueadero(
    vehiculo_id: int,
    numero_parqueadero: str,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    """Ruta exclusiva para que el Admin asigne el resultado de un sorteo o disponibilidad."""
    if current_user.rol != "Admin":
        raise HTTPException(status_code=403, detail="Privilegios insuficientes. Solo Administración puede asignar espacios.")
        
    vehiculo = db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
        
    vehiculo.parqueadero_asignado = numero_parqueadero
    db.commit()
    db.refresh(vehiculo)
    return vehiculo