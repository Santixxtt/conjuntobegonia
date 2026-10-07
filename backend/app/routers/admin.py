from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.usuario_model import Usuario
from app.schemas.usuario_schema import UsuarioResponse, UsuarioCreate
from app.core.security import get_password_hash
from app.dependencias import get_current_user

router = APIRouter(prefix="/admin", tags=["Panel de Administración"])

def verificar_admin(current_user: Usuario = Depends(get_current_user)):
    """Bloquea el acceso a cualquier usuario que no sea Admin"""
    if current_user.rol != "Admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Acceso denegado. Privilegios de administrador requeridos."
        )
    return current_user

@router.get("/usuarios", response_model=List[UsuarioResponse])
def listar_todos_los_usuarios(
    skip: int = 0, limit: int = 100, 
    db: Session = Depends(get_db),
    admin: Usuario = Depends(verificar_admin) # Protegido
):
    """Devuelve la lista completa de usuarios registrados en el conjunto"""
    return db.query(Usuario).offset(skip).limit(limit).all()

@router.post("/usuarios", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db),
    admin: Usuario = Depends(verificar_admin) # Protegido
):
    """Permite al administrador registrar nuevos residentes, porteros u otros admins"""
    # Verificar que la cédula o correo no existan ya
    if db.query(Usuario).filter(Usuario.cedula == usuario.cedula).first():
        raise HTTPException(status_code=400, detail="La cédula ya está registrada")
    
    if usuario.email and db.query(Usuario).filter(Usuario.email == usuario.email).first():
        raise HTTPException(status_code=400, detail="El correo electrónico ya está registrado")

    nuevo_usuario = Usuario(
        cedula=usuario.cedula,
        nombre=usuario.nombre,
        email=usuario.email,
        telefono=usuario.telefono,
        rol=usuario.rol,
        apartamento_id=usuario.apartamento_id,
        password_hash=get_password_hash(usuario.password),
        requires_password_change=True # Obliga al residente a cambiar la clave al primer login
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario