from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from app.database import engine, Base
from app.models import *  
from app.routers import auth, anuncios, pqrs, porteria, admin, residentes, vehiculos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Begonia")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "https://conjuntobegonia.vercel.app/"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], # Permite enviar tokens y otros headers
)

app.include_router(auth.router, prefix="/api")
app.include_router(anuncios.router, prefix="/api")
app.include_router(pqrs.router, prefix="/api")
app.include_router(porteria.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
app.include_router(residentes.router, prefix="/api")
app.include_router(vehiculos.router, prefix="/api")

@app.get("/")
def root():
    return {"mensaje": "API de Begonia conectada y funcionando"}