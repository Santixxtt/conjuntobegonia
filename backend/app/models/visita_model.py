from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Visita(Base):
    __tablename__ = "registro_visitas"
    
    id = Column(Integer, primary_key=True, index=True)
    apartamento_id = Column(Integer, ForeignKey("apartamentos.id", ondelete="CASCADE"), nullable=False)
    nombre_visitante = Column(String(100), nullable=False)
    cedula_visitante = Column(String(20), nullable=True)
    fecha_ingreso = Column(TIMESTAMP, server_default=func.now())

    apartamento = relationship("Apartamento")