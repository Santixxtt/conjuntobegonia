from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Apartamento(Base):
    __tablename__ = "apartamentos"
    id = Column(Integer, primary_key=True, index=True)
    torre_id = Column(Integer, ForeignKey("torres.id", ondelete="CASCADE"), nullable=False)
    numero = Column(String(20), nullable=False)
    estado = Column(Enum('Habitado', 'Deshabitado', 'Remodelacion'), default='Habitado')
    
    torre = relationship("Torre", back_populates="apartamentos")
    usuarios = relationship("Usuario", back_populates="apartamento")