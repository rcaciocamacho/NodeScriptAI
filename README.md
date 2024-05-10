# NodeScriptAI
Script para NodeMCU con capacidades de conexión con ChatGPT, Alexa y Telegram.

## Contenido de requirements.txt
```
Flask==2.1.2
requests==2.28.1
python-telegram-bot==13.12
```

## Instalación utilizando requirements.txt
```
pip install -r requirements.txt
```

## Nota adicional sobre el entorno
```
# Instalar el paquete de entorno virtual si aún no está instalado
pip install virtualenv

# Crear un entorno virtual
virtualenv venv

# Activar el entorno virtual en Windows
venv\Scripts\activate

# Activar el entorno virtual en Unix o MacOS
source venv/bin/activate
```

## Instrucciones para construir y ejecutar el contenedor
```
# Construir la imagen de Docker usando Docker Compose
docker-compose build

# Ejecutar el servidor en un contenedor
docker-compose up
```