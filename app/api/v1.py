from fastapi import APIRouter
from app.core.config import APP_NAME, APP_VERSION

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Welcome to Atlas"}


@router.get("/health")
def health_check():
    return {"status": "healthy"}


@router.get("/info")
def get_info():
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
        "status": "healthy",
    }