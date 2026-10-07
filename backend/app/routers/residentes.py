from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.usuario_model import Usuario
from app.schemas.usuario_schema import UsuarioResponse
from app.dependencias import get_current_user

router = APIRouter(prefix="/residentes", tags=["Panel de Residentes"])

def verificar_residente(current_user: Usuario = Depends(get_current_user)):
    """Permite acceso a Residentes (y al Admin para auditoría)"""
    if current_user.rol not in ["Admin", "Residente"]:
        raise HTTPException(status_code=403, detail="Acceso exclusivo para residentes")
    return current_user

@router.get("/mi-apartamento/convivientes", response_model=List[UsuarioResponse])
def listar_convivientes(
    db: Session = Depends(get_db),
    residente: Usuario = Depends(verificar_residente)
):
    """Muestra todos los usuarios registrados en el mismo apartamento del residente actual"""
    if not residente.apartamento_id:
        raise HTTPException(status_code=404, detail="No tienes un apartamento asignado en el sistema")
    
    convivientes = db.query(Usuario).filter(
        Usuario.apartamento_id == residente.apartamento_id
    ).all()
    
    return convivientes