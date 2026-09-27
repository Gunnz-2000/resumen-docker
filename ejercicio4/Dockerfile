FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Se instalan las dependencias usando pip (Gestor de paquetes de Python)
# --no-cache-dir: evita que se almacenen en caché
# -r: especifica el archivo de requerimientos
RUN pip install --no-cache-dir -r requirements.txt

# Se copia el resto de los archivos
COPY . .

# Se expone el puerto 5000
EXPOSE 5000

# Se define el comando de ejecución
# --host=0.0.0.0: permite que el contenedor sea accesible desde el host
# CMD: comando que se ejecuta al iniciar el contenedor
# flask run: comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]