#!/bin/bash

# Nombre de la imagen y el contenedor
IMAGE_NAME="api-don-galleto"
CONTAINER_NAME="api-don-galleto"

# Detener y eliminar el contenedor si ya existe
if [ $(docker ps -a -q -f name=$CONTAINER_NAME) ]; then
  echo "Deteniendo y eliminando el contenedor existente..."
  docker stop $CONTAINER_NAME
  docker rm $CONTAINER_NAME
fi

# Eliminar la imagen anterior si ya existe
if [ $(docker images -q $IMAGE_NAME) ]; then
  echo "Eliminando la imagen Docker existente..."
  docker rmi $IMAGE_NAME
fi

# Construir la nueva imagen
echo "Construyendo la imagen Docker..."
docker build -t $IMAGE_NAME .

# Verificar si la construcción fue exitosa antes de continuar
if [ $? -ne 0 ]; then
  echo "Error: La construcción de la imagen Docker falló."
  exit 1
fi

# Crear y ejecutar el nuevo contenedor
echo "Creando y ejecutando un nuevo contenedor..."
docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME

# Verificar si el contenedor se inició correctamente
if [ $? -ne 0 ]; then
  echo "Error: Falló al crear y ejecutar el contenedor."
  exit 1
fi

echo "Despliegue completado con éxito."

docker logs api-don-galleto 