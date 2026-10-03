from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base

class Vehiculo(Base):
    __tablename__ = "vehiculos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    placa = Column(String(10), unique=True, nullable=False)
    tipo = Column(Enum('Carro', 'Moto', 'Bicicleta'), nullable=False)
    parqueadero_asignado = Column(String(20), nullable=True)
    
    propietario = relationship("Usuario", back_populates="vehiculos")