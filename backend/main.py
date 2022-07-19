from typing import Union

from fastapi import FastAPI
from core.config import Settings

app = FastAPI(title=Settings.PROJECT_TITLE, version=Settings.PROJECT_VERSION,
              description=Settings.PROJECT_DESCRIPTION)


@app.get("/")
def read_root():
    return {"Hello": "World"}
