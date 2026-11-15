# Piratefy 🎶
Este proyecto sirve para administrar una *biblioteca musical*.

## Requisitos previos

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.
* Visual Studio Code con la extensión **Dev Containers** (opcional, para desarrollar dentro del contenedor).

## Configuración e instalación con Docker

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Andrey-Enrique-GM/Piratefy
   cd Piratefy
   ```

2. **Construir la imagen de Docker:**
    Desde la carpeta raíz del proyecto, ejecuta:
    ```bash
    docker build -t piratefy .
    ```

3. **Ejecutar el contenedor:**
    ```bash
    docker run -p 5000:5000 --name piratefy-container piratefy
    ```

## Desarrollo con Dev Containers (VS Code)
Si utilizas la extensión Dev Containers en VS Code (asegúrate de haber construido la imagen piratefy previamente en el paso 2):

* Abre la carpeta del proyecto en VS Code.
* Presiona Ctrl + Shift + P y selecciona Dev Containers: Reopen in Container.
* VS Code cargará el entorno configurado en ```.devcontainer/devcontainer.json```.

## Salu2
Chihuahua!