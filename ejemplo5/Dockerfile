FROM nginx:latest

#COPY es una instrucción que permite copiar archivos o directorios del host al container
#En este caso, se copia el archivo myapp.html al directorio /usr/share/nginx/html del container
#Este directorio es el directorio por defecto donde nginx busca los archivos HTML
#Esto significa que cuando el container se inicie, nginx servirá el archivo myapp.html
COPY myapp.html /usr/share/nginx/html

EXPOSE 80