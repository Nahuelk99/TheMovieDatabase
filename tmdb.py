import requests
import argparse
from config import API_KEY, BASE_URL

def obtener_peliculas(tipo):
    """Obtiene las películas según el tipo especificado."""
    tipos_validos = {
        "playing": "now_playing",
        "popular": "popular",
        "top": "top_rated",
        "upcoming": "upcoming"
    }

    if tipo not in tipos_validos:
        print("Error: Tipo no válido. Usa: playing, popular, top, upcoming")
        return

    url = f"{BASE_URL}{tipos_validos[tipo]}?api_key={API_KEY}&language=es-ES"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza error si la respuesta no es 200
        data = response.json()

        if "results" in data:
            print(f"\n📽️ {tipo.upper()} PELÍCULAS 📽️")
            for i, movie in enumerate(data["results"][:10], 1):  # Muestra solo 10 películas
                print(f"{i}. {movie['title']} ({movie['release_date']})")

        else:
            print("No se encontraron resultados.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos: {e}")

# Argumentos de línea de comandos
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Herramienta CLI para obtener información de películas en TMDB.")
    parser.add_argument("--type", required=True, help="Opciones: playing, popular, top, upcoming")
    args = parser.parse_args()

    obtener_peliculas(args.type)
