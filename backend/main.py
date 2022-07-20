from typing import Union

from fastapi import FastAPI
from db.session import engine
from db.base import Base
from core.config import Settings


def create_tables():  # new
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=Settings.PROJECT_TITLE, version=Settings.PROJECT_VERSION,
                  description=Settings.PROJECT_DESCRIPTION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def read_root():
    return {"Hello": "World"}
