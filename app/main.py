from turtle import title
from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="Inventory Management System")

app.include_router(router, prefix="/api/v1")

@app.get("/")
def read_rppt():
    return{"message": "Welcome to the Inventory Management System"}