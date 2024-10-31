from fastapi import APIRouter, HTTPException
from app.services.external_api import recuperarClimaActualCiudad

router = APIRouter()

@router.get("/clima/{ciudad}/{pais}")
async def obtener_clima(ciudad: str, pais: str):
    # Llamar a la función que consume la API externa
    data = recuperarClimaActualCiudad(ciudad, pais)
    
    # Verificar si hay un error en los datos devueltos
    if "error" in data:
        print("FAIL")
        raise HTTPException(status_code=data["code"], detail=data["error"])
    
    # Si todo va bien, retornar los datos de la API externa
    return data