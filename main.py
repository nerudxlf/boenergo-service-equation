from fastapi import FastAPI

from src.routers import equation

app = FastAPI()

app.include_router(equation.router)
