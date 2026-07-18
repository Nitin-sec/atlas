from fastapi import FastAPI
from app.core.database import create_tables
from app.api.routes import router
from app.core.database import engine
from app.core.config import (
    APP_DESCRIPTION,
    APP_NAME,
    APP_VERSION,
)

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

app.include_router(router)

@app.on_event("startup")
def startup():

    create_tables()
