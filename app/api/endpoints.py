from fastapi import APIRouter, HTTPException
from app.services.external_api import recuperarClimaActualCiudad
from app.utils.estadisticas import calcularEstadisticasColombia, verificarParametro

router = APIRouter()
# Este endpoint devuelve el clima actual de una ciudad específica en un país dado.
# Se requiere proporcionar el nombre de la ciudad y el código ISO del país (de dos letras).
# La respuesta incluye información sobre temperatura, presión, humedad y otros datos meteorológicos.
@router.get("/clima/{ciudad}/{pais}")
async def obtener_clima(ciudad: str, pais: str):
    data = recuperarClimaActualCiudad(ciudad, pais)
    
    if "error" in data:
        raise HTTPException(status_code=data["code"], detail=data["error"])
    
    return data


# Este endpoint recibe un parametro de entrada que puede ser uno de los siguientes
# "temperatura", "presion", "humedad", "velocidad-viento", "general"
# Dependiendp del parametro se retorna el promedio de 5 ciudades en ese dato especifico
@router.post("/clima/estadisticas/{parametro}")
async def obtener_estadisticas(parametro: str):
    datos = calcularEstadisticasColombia(parametro)
    return {"promedio": datos}
