import redis
import os
from dotenv import load_dotenv

load_dotenv()

# Si tienes la URL de Upstash, ponla en el .env como REDIS_URL
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

redis_client = redis.from_url(REDIS_URL, decode_responses=True)