from importlib import reload
from turtle import back
import uvicorn
from app.db.database import Base, engine
from app.main import app

def create_tables():
    Base.metadata.create_all(bind=engine) # type: ignore

if __name__ == "__main__":

    create_tables()
    

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)