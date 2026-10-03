# app/routers/auth.py
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencias import get_current_user
from app.models.usuario_model import Usuario
from app.core.security import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.schemas.token import Token


router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/login") # Puedes usar response_model=Token si quieres tipado estricto
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    # Buscamos al usuario usando la cédula que vendrá en el campo "username" del formulario
    user = db.query(Usuario).filter(Usuario.cedula == form_data.username).first()
    
    # Validamos existencia del usuario y la contraseña hasheada
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Cédula o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generar el token incluyendo el rol para usarlo en el frontend
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.cedula, "rol": user.rol}, 
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "rol": user.rol,
        "nombre": user.nombre
    }

@router.get("/me")
async def read_users_me(current_user: Usuario = Depends(get_current_user)):
    # Si el código llega hasta aquí, significa que el token es válido
    return {
        "mensaje": "¡Tienes acceso a esta ruta protegida!",
        "datos_usuario": {
            "nombre": current_user.nombre,
            "cedula": current_user.cedula,
            "rol": current_user.rol
        }
    }