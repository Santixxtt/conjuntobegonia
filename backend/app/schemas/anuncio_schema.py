from pydantic import BaseModel
from datetime import datetime

class AnuncioBase(BaseModel):
    titulo: str
    contenido: str

class AnuncioCreate(AnuncioBase):
    pass

class AnuncioResponse(AnuncioBase):
    id: int
    autor_id: int
    fecha_publicacion: datetime

    class Config:
        from_attributes = True