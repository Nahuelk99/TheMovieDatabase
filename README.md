# Proyecto: CLI de Películas con TMDB

Este es un proyecto de interfaz de línea de comandos (CLI) que utiliza la API de The Movie Database (TMDB) para obtener y mostrar información sobre películas directamente en la terminal.

## Características

- Obtener y visualizar listas de películas populares, mejor calificadas, próximas y en reproducción actualmente.
- Permite al usuario especificar el tipo de películas que desea ver mediante argumentos de línea de comandos.
- Manejo de errores para garantizar una experiencia fluida.

## Requisitos

- Tener instalado Node.js o Python (según el lenguaje utilizado).
- Obtener una clave de API de TMDB para realizar las solicitudes.

## Instalación

1. Clona este repositorio:
   ```sh
   git clone https://github.com/Nahuelk99/TheMovieDatabase.git
   cd TheMovieDatabase
   ```
2. Instala las dependencias necesarias (si aplica):
   ```sh
   npm install   # Para Node.js
   ```
   o
   ```sh
   pip install -r requirements.txt   # Para Python
   ```
3. Configura tu clave de API de TMDB:
   - Crea un archivo `.env` y agrega tu clave de API:
     ```sh
     TMDB_API_KEY=tu_api_key
     ```

## Uso

Ejecuta el siguiente comando en la terminal para ver las películas según el tipo especificado:

```sh
node index.js --type "popular"
```

o si está en Python:

```sh
python app.py --type "top"
```

Opciones disponibles:
- `--type "playing"` → Películas en reproducción
- `--type "popular"` → Películas populares
- `--type "top"` → Películas mejor calificadas
- `--type "upcoming"` → Próximos estrenos

## Consideraciones

- Manejo de errores en caso de problemas de conexión o fallos de la API.
- Puede extenderse para incluir más funcionalidades según las necesidades del usuario.

## Contribución

Si deseas contribuir, puedes hacer un fork del repositorio y enviar un pull request con mejoras o nuevas funcionalidades.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes utilizarlo y modificarlo libremente.

---

🎥 Disfruta explorando películas desde tu terminal con este CLI! 🎬

