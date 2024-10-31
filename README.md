# FastAPI de clima

Trabajo desarrollado por Andrés Felipe Limas Zea

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
