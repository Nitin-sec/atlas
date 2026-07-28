from fastapi import FastAPI

from app.core.exceptions import register_exception_handlers

from app.core.logging import setup_logging
from app.middleware.logging import LoggingMiddleware

from app.api.routes import router
from app.core.config import (
    APP_DESCRIPTION,
    APP_NAME,
    APP_VERSION,
)

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    openapi_tags=[
        {
            "name": "Notes",
            "description": "CRUD operations for Atlas notes.",
        },
        {
            "name": "Users",
            "description": "User registration and authentication.",
        },
    ],
)

app.include_router(router)

app = FastAPI(
    title="Atlas API",
    version="0.1.0",
)

register_exception_handlers(app)

app.include_router(router)

app = FastAPI(
    title="Atlas API",
    version="0.1.0",
)

setup_logging()

register_exception_handlers(app)

app.add_middleware(LoggingMiddleware)

app.include_router(router)