from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum

# Coincide con los roles de tu base de datos
class RolEnum(str, Enum):
    Admin = 'Admin'
    Residente = 'Residente'
    Porteria = 'Porteria'

# Propiedades compartidas
class UsuarioBase(BaseModel):
    cedula: str
    nombre: str
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    rol: RolEnum
    apartamento_id: Optional[int] = None

# Usado para crear un usuario (requiere contraseña)
class UsuarioCreate(UsuarioBase):
    password: str

# Usado para devolver el usuario en la API (excluye contraseña)
class UsuarioResponse(UsuarioBase):
    id: int
    requires_password_change: bool
    fecha_creacion: datetime

    class Config:
        from_attributes = True  # Permite a Pydantic leer los modelos de SQLAlchemy