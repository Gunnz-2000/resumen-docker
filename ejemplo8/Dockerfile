#Etapa 1 Stage 1: le asignamos un nombre a esta etapa
FROM node:alpine AS build
#Definimos el directorio de trabajo
WORKDIR /app
#Copiamos la carpeta app al directorio de trabajo
COPY app /app

#Stage 2- Iniciamos nueva etapa en la imagen nginx
FROM nginx:alpine AS final
#Copiamos los archivos de la etapa anterior
COPY --from=build /app /usr/share/nginx/html
#Exportamos el puerto
EXPOSE 80
#Iniciamos el servidor
CMD ["nginx","-g","daemon off;"]