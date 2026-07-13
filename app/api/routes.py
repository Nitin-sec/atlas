from fastapi import APIRouter
from app.api.v1 import router as v1_router

router = APIRouter(prefix="/api/v1")

router.include_router(v1_router)