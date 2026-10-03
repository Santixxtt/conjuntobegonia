# backend/seed.py
from app.database import SessionLocal
from app.models.torre_model import Torre
from app.models.apartamento_model import Apartamento
from app.models.usuario_model import Usuario
from app.core.security import get_password_hash

def seed_data():
    db = SessionLocal()
    try:
        # 1. Verificar o Crear Torre de prueba
        torre = db.query(Torre).filter(Torre.nombre == "Torre A").first()
        if not torre:
            torre = Torre(nombre="Torre A")
            db.add(torre)
            db.commit()
            db.refresh(torre)

        # 2. Verificar o Crear Apartamento de prueba
        apto = db.query(Apartamento).filter(Apartamento.numero == "101", Apartamento.torre_id == torre.id).first()
        if not apto:
            apto = Apartamento(torre_id=torre.id, numero="101")
            db.add(apto)
            db.commit()
            db.refresh(apto)

        # 3. Verificar o Crear Usuario Admin
        admin = db.query(Usuario).filter(Usuario.cedula == "123456").first()
        if not admin:
            admin = Usuario(
                cedula="123456",
                nombre="Admin Begonia",
                email="admin@begonia.com",
                rol="Admin",
                password_hash=get_password_hash("admin123"),
                requires_password_change=False
            )
            db.add(admin)
        
        # 4. Verificar o Crear Usuario Residente
        residente = db.query(Usuario).filter(Usuario.cedula == "654321").first()
        if not residente:
            residente = Usuario(
                cedula="654321",
                nombre="Residente Begonia",
                email="residente@begonia.com",
                rol="Residente",
                apartamento_id=apto.id,
                password_hash=get_password_hash("residente123"),
                requires_password_change=False
            )
            db.add(residente)

        db.commit()
        print("✅ Datos de prueba verificados e insertados exitosamente.")
    except Exception as e:
        print(f"❌ Error insertando datos: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()