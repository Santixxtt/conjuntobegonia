from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class EstadoPaqueteEnum(str, Enum):
    En_Porteria = 'En Porteria'
    Entregado = 'Entregado'

# Paquetería
class PaqueteCreate(BaseModel):
    apartamento_id: int
    descripcion: str

class PaqueteResponse(BaseModel):
    id: int
    apartamento_id: int
    descripcion: str
    estado: EstadoPaqueteEnum
    fecha_recepcion: datetime
    fecha_entrega: Optional[datetime] = None

    class Config:
        from_attributes = True

# Visitas
class VisitaCreate(BaseModel):
    apartamento_id: int
    nombre_visitante: str
    cedula_visitante: Optional[str] = None

class VisitaResponse(BaseModel):
    id: int
    apartamento_id: int
    nombre_visitante: str
    cedula_visitante: Optional[str] = None
    fecha_ingreso: datetime

    class Config:
        from_attributes = True