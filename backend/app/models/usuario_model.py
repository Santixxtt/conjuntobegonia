from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    apartamento_id = Column(Integer, ForeignKey("apartamentos.id", ondelete="SET NULL"), nullable=True)
    cedula = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=True)
    telefono = Column(String(20), nullable=True)
    rol = Column(Enum('Admin', 'Residente', 'Porteria'), nullable=False)
    password_hash = Column(String(255), nullable=False)
    requires_password_change = Column(Boolean, default=True)
    fecha_creacion = Column(TIMESTAMP, server_default=func.now())
    
    apartamento = relationship("Apartamento", back_populates="usuarios")
    vehiculos = relationship("Vehiculo", back_populates="propietario")