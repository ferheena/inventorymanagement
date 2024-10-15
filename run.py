from importlib import reload
from turtle import back
import uvicorn
from app.db.database import Base, engine


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)