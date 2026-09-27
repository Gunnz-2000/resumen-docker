#Indicamos la imagen que vamos a utilizar
FROM ubuntu:latest

#Actualizamos los repositorios de ubuntu e instalamos algunas herramientas
#Siempre es recomendado actualizar antes de instalar
#El && nos permite encadenar comandos
#El \ nos permite separar los comandos en varias lineas
#El rm -rf /var/lib/apt/lists/* nos permite limpiar la cache y optimizar el tamaño de la imagen
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    vim \
    git \
    && rm -rf /var/lib/apt/lists/*

#Establecemos el directorio de trabajo - aqui se guardan los archivos necesarios para trabajar con este container
WORKDIR /app

#Generamos un archivo dentro del directorio de trabajo
# > sobreescribe el archivo
# >> añade contenido al archivo
RUN echo "Hola mundo desde Docker" > hola.txt

#Exportamos el puerto
EXPOSE 80

#Comando que se ejecuta cuando se inicia el container - solo se permite uno por Dockerfile
#Si en el Dockerfile no se especifica ningun CMD, se ejecuta el CMD de la imagen base
#Si en el Dockerfile se especifica un CMD, se ejecuta el CMD de la imagen base y luego el CMD del Dockerfile
#Si en el Dockerfile se especifica un ENTRYPOINT, se ejecuta el ENTRYPOINT de la imagen base y luego el CMD del Dockerfile
CMD ["echo","Este es un contenedor de ejemplo"]