# Proyecto: CLI de Películas con TMDB

Este proyecto es una interfaz de línea de comandos (CLI) que permite obtener y visualizar información de películas desde The Movie Database (TMDB). Es una excelente manera de practicar el consumo de APIs, manejo de datos JSON y creación de herramientas CLI.

## Características
- Obtener y mostrar películas populares, mejor calificadas, en estreno y próximamente disponibles.
- Interactuar con la API de TMDB desde la terminal.
- Manejo de errores ante fallos de API o problemas de red.

## Requisitos
- Tener Node.js instalado en tu sistema.
- Una cuenta en [TMDB](https://www.themoviedb.org/) para obtener la API Key.

## Cómo obtener una API Key de TMDB
1. Regístrate en [TMDB](https://www.themoviedb.org/).
2. Inicia sesión y dirígete a la sección "Settings" (Configuración).
3. En el menú lateral, busca "API" y haz clic en "Create" para generar una clave.
4. Guarda la clave, ya que será necesaria para acceder a la API.

## Instalación y Configuración
1. Clona este repositorio:
   ```sh
   git clone https://github.com/Nahuelk99/TheMovieDatabase.git
   cd TheMovieDatabase
   ```
2. Instala las dependencias necesarias:
   ```sh
   npm install
   ```
3. Crea un archivo `.env` en la raíz del proyecto y añade tu API Key:
   ```env
   API_KEY=tu_api_key_aqui
   ```

## Uso
Ejecuta la aplicación desde la línea de comandos con el siguiente formato:
```sh
tmdb-app --type "playing"
tmdb-app --type "popular"
tmdb-app --type "top"
tmdb-app --type "upcoming"
```

Donde:
- `playing`: Muestra las películas en reproducción.
- `popular`: Muestra las películas más populares.
- `top`: Muestra las películas mejor calificadas.
- `upcoming`: Muestra las próximas películas.

## Consideraciones
- Asegúrate de manejar errores correctamente (fallos en la API, problemas de conexión, etc.).
- Puedes usar cualquier lenguaje de programación para desarrollar este proyecto.

## Contribución
Si deseas mejorar este proyecto, ¡las contribuciones son bienvenidas! Puedes hacer un fork, trabajar en mejoras y enviar un pull request.

## Licencia
Este proyecto está bajo la licencia MIT.


