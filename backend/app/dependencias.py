from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy.orm import Session
from app.core.security import SECRET_KEY, ALGORITHM
from app.database import get_db
from app.models.usuario_model import Usuario

# Le indica a FastAPI dónde conseguir el token (para la documentación de Swagger)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Desencripta el token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        cedula: str = payload.get("sub")
        if cedula is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
        
    # Busca al usuario en la base de datos
    user = db.query(Usuario).filter(Usuario.cedula == cedula).first()
    if user is None:
        raise credentials_exception
        
    return user