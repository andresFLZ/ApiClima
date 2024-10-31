import requests
from app.core.config import settings

# Función que recupera el clima actual de una ciudad de la api OpenWeatherMap API
# recibe 2 parametros: ciudad que es string, pais que es string.
# Si no hay errores devuelve un JSON con la data pero si hay errores verfica de que error se trata y lo notifica
def recuperarClimaActualCiudad(ciudad: str, pais: str):
    url = f"{settings.API_CLIMA}weather?q={ciudad},{pais}&units=metric&appid={settings.API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        return response.json()
    
    except requests.HTTPError as e:
        if response.status_code == 404:
            return {"error": "Ciudad no encontrada.", "code": 404}
        elif response.status_code == 401:
            return {"error": "Autenticación fallida. Verifica tu API key.", "code": 401}
        elif response.status_code == 400:
            return {"error": "Solicitud incorrecta. Verifica los parámetros.", "code": 400}
        elif response.status_code == 500:
            return {"error": "Error interno del servidor. Intenta más tarde.", "code": 500}
        else:
            return {"error": f"Ocurrió un error: {str(e)}", "code": 500}

    except requests.RequestException as e:
        return {"error": f"Error en la conexión: {str(e)}", "code": 500}
