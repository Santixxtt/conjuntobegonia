from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # IMPORTANTE: Nueva importación
from app.database import engine, Base
from app.models import *  
from app.routers import auth  

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Begonia")

# Configuración de CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"], # Puertos de Vite
    allow_credentials=True,
    allow_methods=["*"], # Permite GET, POST, PUT, DELETE, etc.
    allow_headers=["*"], # Permite enviar tokens y otros headers
)

app.include_router(auth.router, prefix="/api")

@app.get("/")
def root():
    return {"mensaje": "API de Begonia conectada y funcionando"}