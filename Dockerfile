# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos primero para aprovechar la caché de capas de Docker
COPY requirements.txt /app/requirements.txt

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente del servidor en el contenedor
COPY . /app

# Expone el puerto en el que Flask se ejecutará
EXPOSE 3000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
