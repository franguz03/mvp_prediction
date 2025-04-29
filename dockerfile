# Usar una imagen base de Python
FROM python:3.10.11

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos e instalar las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el contenido del proyecto al contenedor
COPY . /app/

# Exponer el puerto en el que Flask escuchará (5000 por defecto)
EXPOSE 5000

# Definir el comando para iniciar la aplicación Flask (usando __init__.py como punto de entrada)
CMD ["python", "__init__.py"]
