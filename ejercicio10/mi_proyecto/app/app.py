from flask import Flask
from redis import Redis
from redis.exceptions import ConnectionError
import os

app = Flask(__name__)
redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = int(os.environ.get("REDIS_PORT", "6379"))
redis_client = Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def index():
    try:
        hits = redis_client.incr("visitas")
        return f"Hola Docker Compose. Contador: {hits}"
    except ConnectionError:
        return "No se puede conectar a Redis todavía.", 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)