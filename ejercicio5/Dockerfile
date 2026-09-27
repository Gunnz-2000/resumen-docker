FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia solo el archivo app.py
COPY app.py .

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta la aplicacion
# --host: bind the server to all network interfaces
# --port: port to listen on
# --reload: si hay cambios en el código, se reinicia el servidor automáticamente
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]