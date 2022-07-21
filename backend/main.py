from fastapi import FastAPI, Request, Response
from db.session import engine
from db.base import Base
from core.config import Settings
from apis.base import api_router


def create_tables():  # new
    Base.metadata.create_all(bind=engine)


def create_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=Settings.PROJECT_TITLE, version=Settings.PROJECT_VERSION,
                  description=Settings.PROJECT_DESCRIPTION)
    create_tables()
    create_router(app)
    return app


app = start_application()


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        return Response("Internal server error", status_code=500)

app.middleware('http')(catch_exceptions_middleware)


@app.get("/")
def read_root():
    return {"Hello": "World"}
