# ðŸ³ Curso de Docker â€” Apuntes y Ejercicios PrÃ¡cticos

> Apuntes personales y ejercicios del curso de Docker, desde conceptos bÃ¡sicos hasta CI/CD con GitHub Actions.

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

---

## ðŸ“Œ Tabla de Contenidos

- [Estructura del repositorio](#-estructura-del-repositorio)
- [Ejercicios prÃ¡cticos](#ï¸-ejercicios-prÃ¡cticos)
- [Referencia de comandos](#-referencia-de-comandos)
  - [Comandos bÃ¡sicos](#ï¸-comandos-bÃ¡sicos)
  - [WSL](#-wsl-windows-subsystem-for-linux)
  - [Dockerfile](#-dockerfile)
  - [Docker Hub](#ï¸-docker-hub)
  - [Redes en Docker](#-redes-en-docker)
  - [Persistencia y datos](#-persistencia-y-gestiÃ³n-de-datos)
  - [Docker Compose](#-docker-compose)
  - [Multi-Stage Builds](#ï¸-multi-stage-builds-multicapas)
  - [CI/CD con GitHub Actions](#-cicd-con-github-actions)

---

## ðŸ“ Estructura del repositorio

```
curso-docker/
â”œâ”€â”€ ejemplo1-8/       # Archivos generados durante las clases del curso
â”œâ”€â”€ ejercicio1/       # Levantar servidor Nginx
â”œâ”€â”€ ejercicio2/       # Contenedor Ubuntu interactivo
â”œâ”€â”€ ejercicio3/       # Script Python con Dockerfile
â”œâ”€â”€ ejercicio4/       # API Flask en contenedor
â”œâ”€â”€ ejercicio5/       # API FastAPI en contenedor
â”œâ”€â”€ ejercicio6/       # Persistencia con volÃºmenes en Ubuntu
â”œâ”€â”€ ejercicio7/       # Persistencia de datos con MySQL + volumen
â”œâ”€â”€ ejercicio8/       # ComunicaciÃ³n entre contenedores via red Docker
â”œâ”€â”€ ejercicio9/       # Flask + Nginx con Docker Compose
â”œâ”€â”€ ejercicio10/      # Flask + Redis con Docker Compose
â”œâ”€â”€ ejercicio11/      # Node.js con Nodemon y hot reload
â”œâ”€â”€ ejercicio12/      # CI/CD con GitHub Actions y Docker Hub
â””â”€â”€ ejercicio13/      # Multi-Stage Build con C y scratch
```

---

## ðŸ‹ï¸ Ejercicios PrÃ¡cticos

Cada ejercicio tiene un archivo `.txt` con el enunciado y los pasos detallados.

| # | Ejercicio | TecnologÃ­as | Concepto clave |
|---|-----------|-------------|----------------|
| 01 | [Servidor Nginx](./ejercicio1/) | Nginx | `docker run`, mapeo de puertos `-p` |
| 02 | [Contenedor Ubuntu interactivo](./ejercicio2/) | Ubuntu | Modo `-it`, `apt-get`, archivos dentro del contenedor |
| 03 | [Script Python](./ejercicio3/) | Python | `Dockerfile`, `COPY`, `CMD`, `docker build` |
| 04 | [API con Flask](./ejercicio4/) | Python, Flask | `RUN pip install`, `EXPOSE`, `requirements.txt` |
| 05 | [API con FastAPI](./ejercicio5/) | Python, FastAPI, Uvicorn | `EXPOSE 8000`, `uvicorn` como servidor ASGI |
| 06 | [VolÃºmenes en Ubuntu](./ejercicio6/) | Ubuntu | Persistencia de datos, `-v`, sobrevivir a la eliminaciÃ³n del contenedor |
| 07 | [MySQL + Volumen](./ejercicio7/) | MySQL | VolÃºmenes nombrados, `-e` para variables de entorno, `docker exec` |
| 08 | [Redes entre contenedores](./ejercicio8/) | PostgreSQL, Alpine | `docker network create`, DNS interno de Docker, `ping` entre contenedores |
| 09 | [Flask + Nginx (Compose)](./ejercicio9/) | Flask, Nginx | Proxy inverso, `docker-compose.yml`, `depends_on` |
| 10 | [Flask + Redis (Compose)](./ejercicio10/) | Flask, Redis | MÃºltiples servicios, variables de entorno, contador con persistencia |
| 11 | [Node.js + Nodemon](./ejercicio11/) | Node.js, Nodemon | Hot reload en desarrollo, bind mount del cÃ³digo local |
| 12 | [CI/CD con GitHub Actions](./ejercicio12/) | Node.js, GitHub Actions | Pipeline automatizado, `secrets`, build y push a Docker Hub |
| 13 | [Multi-Stage Build con C](./ejercicio13/) | C, gcc, scratch | Imagen mÃ­nima de producciÃ³n, separar build de runtime |

---

## ðŸ“– Referencia de Comandos

### ðŸ› ï¸ Comandos BÃ¡sicos

> Los contenedores nacen de las imÃ¡genes. Si no tenemos la imagen localmente, Docker la descarga automÃ¡ticamente.

| Comando | DescripciÃ³n |
|---------|-------------|
| `docker run hello-world` | Corre un contenedor desde la imagen `hello-world`. Si no existe, la descarga. |
| `docker ps` | Muestra todos los contenedores **en ejecuciÃ³n**. |
| `docker ps -a` | Muestra **todos** los contenedores, incluso los detenidos. |
| `docker images` | Lista todas las imÃ¡genes descargadas en tu sistema local. |
| `docker search nginx` | Busca imÃ¡genes relacionadas a `nginx` en Docker Hub. |
| `docker pull nginx` | Descarga la imagen `nginx` desde Docker Hub. |
| `docker rm <id>` | Elimina un contenedor especÃ­fico. |
| `docker rmi <imagen>` | Elimina una imagen. No puedes eliminar la imagen de un contenedor existente. |
| `docker stop <nombre_o_id>` | Detiene un contenedor en ejecuciÃ³n. |
| `docker container prune` | Elimina **todos** los contenedores detenidos. |
| `docker inspect <nombre>` | Muestra informaciÃ³n detallada (red, volÃºmenes, config) de un contenedor. |

---

### ðŸ§ WSL (Windows Subsystem for Linux)

```bash
wsl          # Entrar al subsistema Linux en Windows
exit         # Salir del subsistema
```

**Flags Ãºtiles para `docker run`:**

| Flag | DescripciÃ³n |
|------|-------------|
| `--name <nombre>` | Asigna un nombre al contenedor. No puede haber dos iguales. |
| `-it` | Modo interactivo con terminal (ideal para Ubuntu, bash, etc.). |
| `-d` | Detached: ejecuta en segundo plano sin bloquear la terminal. |
| `-p 8080:80` | Mapeo de puertos: `puerto_host:puerto_contenedor`. |
| `--rm` | Elimina el contenedor automÃ¡ticamente cuando se detiene. |

```bash
docker run --name alwaysup -d ubuntu tail -f /dev/null    # Contenedor Ubuntu siempre activo
docker run -it --rm -d -p 8080:80 --name web nginx:latest # Nginx con auto-limpieza al detenerlo
```

---

### ðŸ“„ Dockerfile

> Archivo de texto con instrucciones que Docker usa para construir una imagen. Una imagen ejecutada con `run` se convierte en un contenedor.

**Instrucciones clave:**

| InstrucciÃ³n | DescripciÃ³n |
|-------------|-------------|
| `FROM <imagen>` | Imagen base sobre la que se construye. |
| `WORKDIR /app` | Define el directorio de trabajo dentro del contenedor. |
| `COPY <src> <dst>` | Copia archivos del host al contenedor. |
| `RUN <comando>` | Ejecuta un comando durante la **construcciÃ³n** de la imagen. |
| `EXPOSE <puerto>` | Documenta el puerto que usarÃ¡ el contenedor (no lo publica solo). |
| `CMD ["cmd", "arg"]` | Comando por defecto al iniciar el contenedor (puede sobreescribirse). |
| `ENTRYPOINT [...]` | Comando fijo al iniciar el contenedor (mÃ¡s rÃ­gido que `CMD`). |

```bash
docker build -t mi-imagen .                           # Construir imagen (. = directorio actual)
docker run -it -p 7080:80 mi-imagen                   # Ejecutar contenedor con mapeo de puertos
docker run -it mi-imagen /bin/bash                    # Abrir terminal bash dentro del contenedor
docker exec -it mi-container ls /usr/share/nginx/html # Ejecutar comando en un contenedor corriendo
docker run mi-imagen echo "mensaje"                   # Sobreescribir CMD del Dockerfile
```

---

### â˜ï¸ Docker Hub

> Registro oficial de imÃ¡genes Docker. Cualquier imagen que subas puede ser descargada desde cualquier mÃ¡quina del mundo.

```bash
docker login                                 # Iniciar sesiÃ³n en Docker Hub
docker tag mi-imagen usuario/nombre-repo     # Crear alias con formato usuario/repo
docker push usuario/nombre-repo              # Subir imagen a Docker Hub
docker logs -f mi-contenedor                 # Ver logs en tiempo real (Ctrl+C para salir)
docker stats mi-contenedor                   # Ver uso de CPU y RAM en tiempo real
```

---

### ðŸŒ Redes en Docker

> Permiten la comunicaciÃ³n entre contenedores y el mundo exterior. Docker asigna DNS interno automÃ¡ticamente: los contenedores se pueden referenciar por su `--name` dentro de la misma red.

```bash
docker network ls                                         # Listar redes (predeterminada: bridge)
docker network create mi-red                              # Crear red personalizada
docker network inspect mi-red                             # Ver detalles de la red
docker run -d --name srv --network mi-red nginx:latest    # Conectar contenedor a la red
docker network disconnect mi-red mi-contenedor            # Desconectar contenedor de una red
docker network rm mi-red                                  # Eliminar la red
```

---

### ðŸ’¾ Persistencia y GestiÃ³n de Datos

> Si eliminas un contenedor, sus datos internos se pierden. Existen dos mecanismos para persistirlos:

| Mecanismo | Sintaxis | DescripciÃ³n | Uso recomendado |
|-----------|----------|-------------|-----------------|
| **Volumen** | `-v nombre:/ruta` | Almacenamiento gestionado por Docker, vive fuera del contenedor. | ProducciÃ³n |
| **Bind Mount** | `-v /ruta/host:/ruta/contenedor` | Carpeta de tu PC montada directamente en el contenedor. | Desarrollo local |

```bash
# VolÃºmenes
docker volume ls                                                       # Listar volÃºmenes
docker volume create mi-volumen                                        # Crear volumen
docker run -d --name mongo --mount src=mi-volumen,dst=/data/db mongo  # Usar volumen con --mount

# Bind Mount
docker run -d --name mongodb -v "/datos:/data/db" mongo:latest        # Montar carpeta local

# Bases de datos con persistencia
docker run --name mysql -v "/mysql_db:/var/lib/mysql" -e MYSQL_ROOT_PASSWORD=1234 -d mysql
docker exec -it mysql bash    # Entrar al contenedor MySQL
mysql -u root -p              # Abrir consola MySQL dentro del contenedor

docker exec -it mongodb bash  # Entrar al contenedor MongoDB
mongosh                       # Abrir consola MongoDB
```

---

### ðŸ™ Docker Compose

> Herramienta para definir y levantar aplicaciones de **mÃºltiples contenedores** usando un archivo `docker-compose.yml`. Cada servicio es un contenedor independiente que se puede comunicar con los demÃ¡s por nombre.

```bash
docker compose up -d          # Levantar todos los servicios en segundo plano
docker compose up --build     # Reconstruir imÃ¡genes y levantar servicios
docker compose down           # Detener y eliminar contenedores y redes
docker compose stop db        # Detener solo el servicio 'db' (sin eliminarlo)
docker compose rm db          # Eliminar el contenedor del servicio 'db'
```

**Estructura bÃ¡sica de `docker-compose.yml`:**

```yaml
services:
  web:
    build: ./app           # Construye desde un Dockerfile local
    ports:
      - "5000:5000"
    environment:
      - REDIS_HOST=redis   # Variable de entorno accesible dentro del contenedor
    depends_on:
      - redis              # Espera a que 'redis' inicie primero

  redis:
    image: redis:7.2-alpine
    volumes:
      - redis_data:/data   # Volumen para persistencia de datos

volumes:
  redis_data:              # DeclaraciÃ³n del volumen nombrado
```

---

### ðŸ—ï¸ Multi-Stage Builds (Multicapas)

> TÃ©cnica de optimizaciÃ³n para imÃ¡genes de producciÃ³n. Divide el `Dockerfile` en etapas: una pesada para compilar y una mÃ­nima para producciÃ³n. **Las etapas intermedias se descartan automÃ¡ticamente.**

```dockerfile
# Etapa 1: CompilaciÃ³n (imagen pesada con todas las herramientas)
FROM gcc:latest AS builder
WORKDIR /app
COPY hello.c .
RUN gcc -static -o hello hello.c

# Etapa 2: ProducciÃ³n (imagen mÃ­nima, solo contiene el ejecutable final)
FROM scratch
COPY --from=builder /app/hello .
CMD ["/hello"]
```

| Etapa | Imagen usada | Contiene |
|-------|-------------|---------|
| Build | `gcc:latest` (~1.2 GB) | Compilador, herramientas, cÃ³digo fuente |
| Final | `scratch` (~0 MB) | Solo el binario compilado |

---

### ðŸš€ CI/CD con GitHub Actions

> Pipeline automÃ¡tico que construye y publica la imagen en Docker Hub cada vez que se hace `push` a la rama `main`. Automatiza el ciclo completo: cÃ³digo â†’ imagen â†’ registro.

**Paso 1 â€” Configurar secrets en GitHub** (`Settings > Secrets and variables > Actions`):

| Secret | Valor |
|--------|-------|
| `DOCKERHUB_USERNAME` | Tu usuario de Docker Hub |
| `DOCKERHUB_TOKEN` | Token de acceso generado en Docker Hub (no tu contraseÃ±a) |

**Paso 2 â€” Definir el workflow** (`.github/workflows/docker.yml`):

```yaml
name: Docker CI
on:
  push:
    branches: ["main"]

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout cÃ³digo
        uses: actions/checkout@v4

      - name: Login en Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build de la imagen
        run: docker build -t ${{ secrets.DOCKERHUB_USERNAME }}/mi-app:latest .

      - name: Push a Docker Hub
        run: docker push ${{ secrets.DOCKERHUB_USERNAME }}/mi-app:latest
```

---

*Apuntes tomados durante el curso de Docker. Cada carpeta de ejercicio contiene el enunciado en un `.txt` y la soluciÃ³n paso a paso con los archivos correspondientes.*
