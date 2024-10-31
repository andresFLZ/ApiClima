from fastapi import HTTPException
from app.services.external_api import recuperarClimaActualCiudad

ciudades = ["Bogota", "Cali", "Medellin", "Cartagena", "Cucuta"]

# Función que recibe un parametro y retorna el promedio de dicho parametro tomando 5 ciudades
def calcularEstadisticasColombia(parametro: str):
    verificarParametro(parametro)
    datos = []

    for ciudad in ciudades:
        dataCiudad = recuperarClimaActualCiudad(ciudad, "co")

        if "error" in dataCiudad:
            raise HTTPException(status_code=dataCiudad["code"], detail=dataCiudad["error"] + " consultando" + ciudad)

        parametroRecuperado = recuperarDatoEspecifico(parametro, dataCiudad)
        datos.append(parametroRecuperado)

    if not datos:
        raise HTTPException(status_code=400, detail="No se pudieron recuperar datos válidos.")

    promedio = calcularPromedio(datos, parametro)
    return promedio


# Verifica que el parametro ingresado sea valido
def verificarParametro(parametro: str):
    parametros_validos = ["temperatura", "presion", "humedad", "velocidad-viento", "general"]

    if parametro not in parametros_validos:
        raise HTTPException(status_code=400, detail=f"El parámetro '{parametro}' no es válido. Debe ser uno de los siguientes: {', '.join(parametros_validos)}.")


# Recupera el dato especifico de un diccionario
def recuperarDatoEspecifico(parametro: str, data: dict):
    opciones = {
        "temperatura": lambda d: d["main"]["temp"],
        "presion": lambda d: d["main"]["pressure"],
        "humedad": lambda d: d["main"]["humidity"],
        "velocidad-viento": lambda d: d["wind"]["speed"],
        "general": lambda d: {
            "temperatura": d["main"]["temp"],
            "presion": d["main"]["pressure"],
            "humedad": d["main"]["humidity"],
            "velocidad-viento": d["wind"]["speed"]
        }
    }
    
    return opciones.get(parametro, lambda d: None)(data)


# Calcula el promedio de una lista de elementos
def calcularPromedio(lista, parametro):
    if not lista:
        return {}

    if isinstance(lista[0], (int, float)):
        promedio = sum(lista) / len(lista)
        return {parametro: promedio}

    elif isinstance(lista[0], dict):
        sumas = {}
        conteos = {}
        
        for diccionario in lista:
            for clave, valor in diccionario.items():
                if clave not in sumas:
                    sumas[clave] = 0
                    conteos[clave] = 0
                sumas[clave] += valor
                conteos[clave] += 1

        promedios = {clave: suma / conteos[clave] for clave, suma in sumas.items()}
        return promedios

    else:
        raise ValueError("La lista debe contener números o diccionarios.")