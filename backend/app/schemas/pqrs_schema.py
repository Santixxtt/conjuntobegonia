from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

# Enumeradores para validación estricta
class TipoPQRSEnum(str, Enum):
    Peticion = 'Peticion'
    Queja = 'Queja'
    Reclamo = 'Reclamo'
    Sugerencia = 'Sugerencia'
    Riesgo_SGSST = 'Riesgo_SGSST'
    Caso_Sistema = 'Caso_Sistema'

class EstadoPQRSEnum(str, Enum):
    Abierto = 'Abierto'
    En_Proceso = 'En Proceso'
    Resuelto = 'Resuelto'

class PrioridadPQRSEnum(str, Enum):
    Baja = 'Baja'
    Media = 'Media'
    Alta = 'Alta'

# Datos que envía el usuario para crear (el estado y fecha los pone el backend)
class PQRSCreate(BaseModel):
    tipo: TipoPQRSEnum
    descripcion: str
    prioridad: Optional[PrioridadPQRSEnum] = PrioridadPQRSEnum.Media

# Datos que devolvemos
class PQRSResponse(BaseModel):
    id: int
    usuario_id: int
    tipo: TipoPQRSEnum
    descripcion: str
    estado: EstadoPQRSEnum
    prioridad: PrioridadPQRSEnum
    fecha_creacion: datetime

    class Config:
        from_attributes = True