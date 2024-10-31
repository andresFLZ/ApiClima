from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI()

# Registrar el router
app.include_router(router)