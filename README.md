# FastAPI de clima

Trabajo desarrollado por Andrés Felipe Limas Zea

## Descripción

Esta api consume data de la api OpenWeatherMap y la trata para poder sacar ciertas estadísticas

## Requerimientos

* Versión de python mayor a la 3.7

## Instrucciones de instalación

1. Clonación del repositorio en tu maquina local

```bash
git clone https://github.com/andresFLZ/ApiClima.git
```

2. Creación del entorno virtual en la carpeta donde clonaste el repositorio

```bash
python3 -m venv venv
```

3. Activación del entorno virtual

```bash
venv\Scripts\activate
```

4. Instalación de dependencias

```bash
pip install -r requirements.txt

```

5. Ejecucuión de la aplicación

```bash
uvicorn app.main:app --reload
```

Esto inicia el servidor de desarrollo en http://127.0.0.1:8000

## Stack tecnológico

Para desarrollar la api se uso fastAPI

<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/fastapi/fastapi-original.svg" title="FastAPI" alt="FastAPI" width="40" height="40"/>&nbsp;

## Parte 1 - Manejo de APIs

### Elección de api publica

API de Clima Seleccionada: OpenWeatherMap

Escogí esta api porque siento que es bastante completa, trata bastante información y a parte esa información se presta para poder hacer cálculos de todo tipo. A parte nunca había trabajado con esta api y me pareció interesante.

Aunque la api presenta diversas formas de recuperar información de bastantes ambitos climaticos yo me enfoque en recuperar la información del clima actual de una ciudad, que retorna la información de la siguiente manera:

```markdown                          
{
   "coord": {
      "lon": 7.367,
      "lat": 45.133
   },
   "weather": [
      {
         "id": 501,
         "main": "Rain",
         "description": "moderate rain",
         "icon": "10d"
      }
   ],
   "base": "stations",
   "main": {
      "temp": 284.2,
      "feels_like": 282.93,
      "temp_min": 283.06,
      "temp_max": 286.82,
      "pressure": 1021,
      "humidity": 60,
      "sea_level": 1021,
      "grnd_level": 910
   },
   "visibility": 10000,
   "wind": {
      "speed": 4.09,
      "deg": 121,
      "gust": 3.47
   },
   "rain": {
      "1h": 2.73
   },
   "clouds": {
      "all": 83
   },
   "dt": 1726660758,
   "sys": {
      "type": 1,
      "id": 6736,
      "country": "IT",
      "sunrise": 1726636384,
      "sunset": 1726680975
   },
   "timezone": 7200,
   "id": 3165523,
   "name": "Province of Turin",
   "cod": 200
}                    
```

Usando esta información pretendo retornarla si es lo deseado o también usarla para calcular estadísticas

### Estructura del proyecto

```markdown
ApiClima/
├── .gitignore
├── venv/
├── app/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── external_api.py
├   ├── core/
│   │   └── config.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── estadisticas.py
│   └── main.py
├── requirements.txt
└── README.md
```

* api/: Esta carpeta alberga la lógica relacionada con los endpoints de la API. El archivo endpoints.py es responsable de definir y manejar las rutas de la aplicación, organizando la lógica de negocio de cada endpoint de forma clara y separada.
* services/: Aquí se encuentra el archivo external_api.py, que se encarga de la interacción con la API pública del clima. Este enfoque modular permite que el código de consumo de la API esté separado de la lógica del endpoint, facilitando su reutilización y mantenimiento.
* core/: En esta carpeta se encuentra el archivo config.py, donde se almacenan las variables de entorno necesarias para la configuración de la aplicación. Centralizar la configuración mejora la seguridad y la flexibilidad, ya que permite cambiar variables sin modificar el código.
* utils/: Esta carpeta contiene el archivo estadisticas.py, que almacena la lógica para calcular estadísticas a partir de los datos del clima. Al tener funciones auxiliares organizadas en un módulo específico, se promueve la reutilización de código y se mejora la legibilidad.
* main.py: Este es el punto de entrada de la aplicación, donde se inicia el servidor y se configuran los routers y middlewares necesarios para que la API funcione correctamente.

La estructura del proyecto ApiClima está diseñada para ser modular y facilitar la mantenibilidad y escalabilidad. Al separar las responsabilidades en diferentes carpetas, como api, services, core y utils, el código se vuelve más organizado y fácil de entender. Esto permite que los desarrolladores trabajen en diferentes aspectos de la aplicación sin interferencias, lo que reduce la probabilidad de errores y mejora la colaboración en equipo. Además, la centralización de la configuración en un archivo específico (config.py) facilita la gestión de variables de entorno, permitiendo ajustes rápidos sin necesidad de modificar el código fuente.

Esta modularidad también promueve la reutilización de código. Funciones como las de cálculo de estadísticas, almacenadas en utils, pueden ser utilizadas en múltiples partes de la aplicación, evitando la duplicación y mejorando la eficiencia del desarrollo.

### Funcionamiento

fastAPI tiene la gran ventaja de generar la documentación automaticamente, después de iniciar la aplicación se puede acceder a ella a traves de esta ruta http://127.0.0.1:8000/docs#/
Esto permite poder probar los endpoints por ti mismo

#### Método GET

Para esté método lo que se hace es recuperar la información del clima actual de una ciudad en especifico, para ello se reciben 2 parametros en la url del endpoint, la ciudad y el código del país en formato ISO 3166, en este [link](https://www.iso.org/obp/ui/#search) puedes consultar los códigos de los paises.

* Endpoint para recuperar el clima actual de bogotá

```bash
http://127.0.0.1:8000/clima/Bogota/co
```

* Funcionamiento

[Get.webm](https://github.com/user-attachments/assets/5708cfa0-957f-49f5-a292-670674c3c035)

#### Método POST

Este endpoint recibe un parametro de entrada que puede ser uno de los siguientes: "temperatura", "presion", "humedad", "velocidad-viento", "general". Dependiendp del parametro se retorna el promedio de 5 ciudades en ese dato especifico.

Las ciudades en este caso son: ["Bogota", "Cali", "Medellin", "Cartagena", "Cucuta"]

* Endpoint para recuperar la temperatura promedio

```bash
http://127.0.0.1:8000/clima/estadisticas/temperatura
```

* Funcionamiento
  
[POST.webm](https://github.com/user-attachments/assets/73d75ad6-db29-4136-b1cc-c1a44a7c1ca8)

Ambos enpoints manejan los casos erroneos donde se ingresa mal la información y evuelven los códigos de estado pertinentes

### Procedimiento

A continuación dejo el procedmiento que yo seguí para completar la primera parte de la prueba:

1. Creación de carpeta para crear el proyecto
2. Creación del entorno virtual usando el comando: python3 -m venv venv
3. Activación del entorno virtual usando el comando: venv\Scripts\activate 
4. Instalación de dependencias principales: pip install fastapi uvicorn requests
5. Creación de la estructura inicial
6. Configuración de variables en archivo config.py
7. Creación de funciones get que consumen el api externa
8. Creación de endpoint get que consume la función 
9. Configuración del archivo main para usar el endpoint creado
10. Creación carpeta utils y archivo estadísticas donde se desarrollara la lógica de la función que se usara en el endpoint post
11. Implementación de las funciones reqeuridas para el funcionamiento del método
12. Creación de endpoint post que consume las funciones

