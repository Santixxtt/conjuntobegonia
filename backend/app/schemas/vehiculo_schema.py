from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TipoVehiculoEnum(str, Enum):
    Carro = 'Carro'
    Moto = 'Moto'
    Bicicleta = 'Bicicleta'

class VehiculoBase(BaseModel):
    placa: str
    tipo: TipoVehiculoEnum
    parqueadero_asignado: Optional[str] = None

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoResponse(VehiculoBase):
    id: int
    usuario_id: int

    class Config:
        from_attributes = True