from locust import HttpUser, task, between

class BegoniaLoadTest(HttpUser):
    # Simula el tiempo que un humano pasa leyendo la pantalla antes de hacer otro clic (entre 1 y 5 segundos)
    wait_time = between(1, 5)

    def on_start(self):
        """
        Se ejecuta automáticamente cada vez que 'nace' un nuevo bot.
        Haremos que el bot inicie sesión con la cuenta de Administrador.
        """
        response = self.client.post("/api/auth/login", data={
            "username": "123456",
            "password": "admin123"
        })
        
        if response.status_code == 200:
            token = response.json().get("access_token")
            self.client.headers.update({"Authorization": f"Bearer {token}"})
        else:
            # Reemplaza el print anterior por este:
            print(f"❌ Error en el login. Código: {response.status_code}, Detalle: {response.text}")

    # El número entre paréntesis es el "peso". Un peso de 3 significa que 
    # esta tarea se ejecutará 3 veces más seguido que la tarea de peso 1.
    @task(3)
    def cargar_cartelera(self):
        """Simula la carga de la pantalla principal de anuncios"""
        self.client.get("/api/anuncios/")

    @task(2)
    def revisar_pqrs(self):
        """Simula la apertura de la bandeja de PQRS"""
        self.client.get("/api/pqrs/")

    @task(1)
    def cargar_parqueaderos(self):
        """Simula la revisión del módulo de vehículos"""
        self.client.get("/api/vehiculos/")