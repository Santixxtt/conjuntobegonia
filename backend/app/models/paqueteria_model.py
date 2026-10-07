from sqlalchemy import Column, Integer, String, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Paquete(Base):
    __tablename__ = "paqueteria"
    
    id = Column(Integer, primary_key=True, index=True)
    apartamento_id = Column(Integer, ForeignKey("apartamentos.id", ondelete="CASCADE"), nullable=False)
    descripcion = Column(String(255), nullable=False)
    estado = Column(Enum('En Porteria', 'Entregado'), default='En Porteria')
    fecha_recepcion = Column(TIMESTAMP, server_default=func.now())
    fecha_entrega = Column(TIMESTAMP, nullable=True)

    apartamento = relationship("Apartamento")