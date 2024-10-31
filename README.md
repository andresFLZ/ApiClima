# FastAPI de clima

Trabajo desarrollado por Andrés Felipe Limas Zea

## Descripción

Esta api consume data de la api OpenWeatherMap y la trata para poder sacar ciertas estadisticas

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

Escogí esta api porque siento que es bastante completa, trata bastante información y a parte esa información se presta para poder hacer cálculos de todo tipo. A parte nunca había trabajado con esta api y me pareció interesante 

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
