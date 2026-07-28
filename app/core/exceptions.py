from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException,
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": {
                    "code": exc.status_code,
                    "message": exc.detail,
                },
            },
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(
        request: Request,
        exc: Exception,
    ):
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": {
                    "code": 500,
                    "message": "Internal Server Error",
                },
            },
        )