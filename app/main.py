from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI()

# Registra las routas (endpoints)
app.include_router(router)