from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Torre(Base):
    __tablename__ = "torres"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)
    
    # Usar strings ("Apartamento") evita importaciones circulares entre archivos
    apartamentos = relationship("Apartamento", back_populates="torre")