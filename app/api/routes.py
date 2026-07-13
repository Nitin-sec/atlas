from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to Atlas"}

@router.get("/health")
def health_check():
    return {"status": "healthy"}
