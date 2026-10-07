import random
from faker import Faker
from app.database import SessionLocal
from app.models.torre_model import Torre
from app.models.apartamento_model import Apartamento
from app.models.usuario_model import Usuario
from app.models.pqrs_model import PQRS
from app.core.security import get_password_hash

# Configurar Faker con datos de Colombia (nombres, teléfonos, etc.)
fake = Faker('es_CO') 
db = SessionLocal()

def generar_datos_masivos():
    try:
        print("Iniciando inyección masiva de datos...")
        
        # 1. Crear 5 Torres
        torres_db = []
        for i in range(1, 6):
            # Evitar duplicados si ejecutas el script varias veces
            torre = db.query(Torre).filter(Torre.nombre == f"Torre {i}").first()
            if not torre:
                torre = Torre(nombre=f"Torre {i}")
                db.add(torre)
                db.commit()
                db.refresh(torre)
            torres_db.append(torre)

        # 2. Crear 20 Apartamentos por Torre (100 en total)
        aptos_db = []
        for torre in torres_db:
            for piso in range(1, 6):
                for num in range(1, 5):
                    numero_apto = f"{piso}0{num}"
                    apto = db.query(Apartamento).filter(Apartamento.numero == numero_apto, Apartamento.torre_id == torre.id).first()
                    if not apto:
                        apto = Apartamento(torre_id=torre.id, numero=numero_apto)
                        db.add(apto)
                        db.commit()
                        db.refresh(apto)
                    aptos_db.append(apto)

        # 3. Crear 150 Residentes aleatorios
        # Hasheamos la contraseña una sola vez para que el script sea muy rápido
        password_default = get_password_hash("prueba123") 
        for _ in range(150):
            apto_asignado = random.choice(aptos_db)
            residente = Usuario(
                cedula=str(fake.random_number(digits=10, fix_len=True)),
                nombre=fake.name(),
                email=fake.unique.email(),
                telefono=fake.phone_number(),
                rol="Residente",
                apartamento_id=apto_asignado.id,
                password_hash=password_default,
                requires_password_change=False
            )
            db.add(residente)
        db.commit()

        # 4. Generar 50 PQRS aleatorias
        usuarios_db = db.query(Usuario).filter(Usuario.rol == "Residente").all()
        tipos_pqrs = ['Peticion', 'Queja', 'Reclamo', 'Sugerencia']
        estados_pqrs = ['Abierto', 'En Proceso', 'Resuelto']
        
        for _ in range(50):
            autor = random.choice(usuarios_db)
            pqrs = PQRS(
                usuario_id=autor.id,
                tipo=random.choice(tipos_pqrs),
                descripcion=fake.text(max_nb_chars=200),
                estado=random.choice(estados_pqrs),
                prioridad=random.choice(['Baja', 'Media', 'Alta'])
            )
            db.add(pqrs)
        db.commit()

        print("✅ Inyección masiva completada: Torres, Apartamentos, 150 Residentes y 50 PQRS creados.")
    except Exception as e:
        print(f"❌ Error durante la inyección: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    generar_datos_masivos()