from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class PQRS(Base):
    __tablename__ = "pqrs"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    tipo = Column(Enum('Peticion', 'Queja', 'Reclamo', 'Sugerencia', 'Riesgo_SGSST', 'Caso_Sistema'), nullable=False)
    descripcion = Column(Text, nullable=False)
    estado = Column(Enum('Abierto', 'En Proceso', 'Resuelto'), default='Abierto')
    prioridad = Column(Enum('Baja', 'Media', 'Alta'), default='Media')
    fecha_creacion = Column(TIMESTAMP, server_default=func.now())

    # Relación para poder acceder a los datos del creador fácilmente si se necesita
    autor = relationship("Usuario")