# Curso y Apuntes de Docker 🐳

Este repositorio contiene mis apuntes personales y ejemplos prácticos para aprender comenzar a aprender Docker.

## 📌 Tabla de Contenidos

- [Comandos Básicos](#comandos-básicos)
- [WSL (Windows Subsystem for Linux)](#wsl-windows-subsystem-for-linux)
- [Dockerfile](#dockerfile)
- [Docker Hub](#docker-hub)
- [Redes en Docker](#redes-en-docker)
- [Persistencia y Gestión de Datos](#persistencia-y-gestión-de-datos)
- [Docker Compose](#docker-compose)
- [Multi-Stage Builds](#multi-stage-builds-multicapas)

---

## 🛠️ Comandos Básicos

Los contenedores nacen de las imágenes. Si no tenemos la imagen localmente, Docker la descarga automáticamente.

- `docker run hello-world`: Corre una imagen. `docker` indica que estamos usando docker y `run` que estamos corriendo una imagen.
- `docker ps`: Muestra todos los contenedores en ejecución.
- `docker ps -a`: Muestra todos los contenedores, incluso si están apagados.
- `docker images`: Lista todas las imágenes descargadas en tu sistema local.
- `docker search nginx`: Lista todas las imágenes relacionadas a `nginx` en Docker Hub (indicando cuál es la oficial).
- `docker pull nginx`: Descarga la imagen `nginx` desde Docker Hub a tu máquina.
- `docker rm <id_contenedor>`: Elimina un contenedor específico.
- `docker rmi <nombre_imagen>`: Elimina una imagen. 
  > **Nota:** No puedes eliminar una imagen que le pertenece a un contenedor (primero debes eliminar el contenedor).

---

## 🐧 WSL (Windows Subsystem for Linux)

- `wsl`: Entrar al subsistema de Linux desde Windows. Usa `exit` para salir.
- `docker run --name contenedor1 hello-world`: Ejecuta un contenedor y le asigna un nombre específico. No puedes tener 2 contenedores con el mismo nombre.
- `docker inspect <nombre_contenedor>`: Ver toda la información detallada (configuración, red, volúmenes) del contenedor.
- `docker container prune`: Elimina todos los contenedores que estén detenidos.
- `docker run -it ubuntu`: Ejecuta la imagen de ubuntu en modo interactivo. Se abre la terminal para interactuar con la imagen y se puede ejecutar cualquier comando de Linux. Usa `exit` para salir.
- `docker run --name alwaysup -d ubuntu tail -f /dev/null`: Crea un contenedor de ubuntu. `-d` para que se ejecute en segundo plano (detached) y `tail -f /dev/null` para mantener el contenedor activo (evita que se cierre automáticamente).
- `docker run -it --rm -d -p 8080:80 --name web nginx:latest`: 
  - `-p 8080:80`: Mapeo de puertos (puerto_host : puerto_contenedor).
  - `--rm`: Elimina el contenedor automáticamente cuando se detiene.
  - `-d`: Segundo plano.
- `docker stop <nombre_o_id_contenedor>`: Detiene un contenedor en ejecución.

---

## 📄 Dockerfile

Archivo de texto que contiene instrucciones que Docker usa mediante `build` para construir una imagen. Al ejecutar la imagen con `run` se obtiene un contenedor.

- **Sintaxis básica**: `docker run [opciones] IMAGEN [COMANDO] [ARGS...]`
- `docker build -t ubuntu-new .`: Construye la imagen a través del archivo Dockerfile. El `.` indica que el archivo está en el directorio actual. `-t` le asigna el nombre (etiqueta) `ubuntu-new`.
- `docker run -it -p 7070:70 ubuntu-new /bin/bash`: Inicia el contenedor y `/bin/bash` permite obtener una terminal interactiva con bash.
- `docker run -it -p 7080:80 ubuntu-new`: Ejecuta la imagen. Los comandos adicionales no sobreescriben la instrucción `CMD` del Dockerfile.
- `docker exec -it my-container ls /usr/share/nginx/html`: `docker exec` entra a un contenedor que ya está corriendo para ejecutar un comando (en este caso listar archivos).
- `docker run my-image1 echo "mensaje extra"`: Ejecuta un comando extra, ideal para sobreescribir la instrucción `CMD` del Dockerfile.

---

## ☁️ Docker Hub

Repositorio oficial y registro de imágenes en Docker.

- `docker login`: Iniciar sesión en tu cuenta de Docker Hub desde la terminal.
- `docker tag ubuntu-new jhimysp/ubuntu-new-repo1`: Crea un alias o etiqueta para una imagen existente (`usuario/nombre_repo`).
- `docker push jhimysp/ubuntu-new-repo1`: Sube tu imagen local a Docker Hub, dentro de tu cuenta.
- `docker logs -f my-test-container`: Muestra la salida de consola (logs) de un contenedor. `-f` lo mantiene en tiempo real (`Ctrl + C` para salir).
- `docker stats my-test-container`: Muestra estadísticas de uso de recursos (CPU, RAM) en tiempo real (`Ctrl + C` para salir).

---

## 🌐 Redes en Docker

Permiten la comunicación entre contenedores y el mundo exterior. Puedes crear tus propias redes personalizadas para aislar tus servicios.

- `docker network ls`: Lista todas las redes de Docker (la predeterminada es `bridge`).
- `docker network create my-network`: Crea una red personalizada.
- `docker network inspect my-network`: Inspecciona los detalles de una red.
- `docker run -d --name my-container-5 --network my-network nginx:latest`: Crea y arranca un contenedor conectado a la red `my-network`.
- `docker network disconnect my-network my-container-6`: Desconecta un contenedor de una red.
- `docker network rm my-network`: Elimina la red `my-network`.

---

## 💾 Persistencia y Gestión de Datos

Si eliminas un contenedor, todos sus datos internos se pierden. Por eso existen mecanismos de persistencia:
1. **Volúmenes**: Espacio de almacenamiento gestionado completamente por Docker.
2. **Bind mounts**: Montas una carpeta/archivo de tu máquina (host) directamente al contenedor. (Útil para desarrollo).

- `docker run -d --name my-mongodb-container -v "/mongodb_data:/data/db" mongo:latest`: **Bind Mount**. Monta la carpeta `/mongodb_data` de tu PC en `/data/db` del contenedor.
- `docker exec -it my-mongodb-container bash`: Entrar al contenedor de mongo. `mongosh` para interactuar con la base de datos.
- `docker run --name mysql-container -v "/mysql_db:/var/lib/mysql" -e MYSQL_ROOT_PASSWORD=1234 -d mysql`: Inicia MySQL con persistencia y define la contraseña root mediante una variable de entorno (`-e`).
- `docker volume ls`: Lista los volúmenes de Docker.
- `docker volume create db_mongo`: Crea un volumen gestionado por Docker.
- `docker run -d --name mongocontainer --mount src=db_mongo,dst=/data/db mongo`: Inicia un contenedor MongoDB usando el volumen de Docker llamado `db_mongo`.

---

## 🐙 Docker Compose

Herramienta para definir y ejecutar aplicaciones Docker de múltiples contenedores usando un archivo `docker-compose.yml`.

- `docker compose up -d`: Levanta todos los servicios definidos en el archivo, creándolos y arrancándolos en segundo plano.
- `docker compose down`: Detiene y elimina todos los contenedores y redes creados por `compose up`.
- `docker compose stop db`: Detiene solo el servicio `db` sin eliminarlo.
- `docker compose rm db`: Elimina el contenedor del servicio `db` previamente detenido.

---

## 🏗️ Multi-Stage Builds (Multicapas)

Técnica de optimización en los `Dockerfile`.
Cuando construyes una imagen, necesitas herramientas de compilación, pero esas herramientas no se necesitan en producción. 

Divides el `Dockerfile` en varias etapas (`FROM ... AS nombre`):
1. **Etapa de build**: Usa una imagen pesada con todas las herramientas y compila el proyecto.
2. **Etapa final**: Usa una imagen ligera (como Alpine o distroless) y copia solo el artefacto resultante de la etapa anterior. Las etapas intermedias se descartan, resultando en una imagen final muy pequeña y segura.