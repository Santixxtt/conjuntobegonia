from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.anuncio_model import Anuncio
from app.models.usuario_model import Usuario
from app.schemas.anuncio_schema import AnuncioCreate, AnuncioResponse
from app.dependencias import get_current_user

router = APIRouter(prefix="/anuncios", tags=["Anuncios"])

@router.post("/", response_model=AnuncioResponse, status_code=status.HTTP_201_CREATED)
def crear_anuncio(
    anuncio: AnuncioCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    # Validar que solo los administradores puedan crear anuncios
    if current_user.rol != "Admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Solo los administradores pueden publicar anuncios"
        )
    
    nuevo_anuncio = Anuncio(
        titulo=anuncio.titulo,
        contenido=anuncio.contenido,
        autor_id=current_user.id
    )
    db.add(nuevo_anuncio)
    db.commit()
    db.refresh(nuevo_anuncio)
    return nuevo_anuncio

@router.get("/", response_model=List[AnuncioResponse])
def obtener_anuncios(
    skip: int = 0, 
    limit: int = 50, 
    db: Session = Depends(get_db),
    #current_user: Usuario = Depends(get_current_user)
):
    """
    Cualquier usuario autenticado (Admin, Residente, Portero) puede leer los anuncios
    anuncios = db.query(Anuncio).order_by(Anuncio.fecha_publicacion.desc()).offset(skip).limit(limit).all()
    return anuncios
    """

    # Cualquier persona (incluso sin token) puede leer los anuncios
    anuncios = db.query(Anuncio).order_by(Anuncio.fecha_publicacion.desc()).offset(skip).limit(limit).all()
    return anuncios