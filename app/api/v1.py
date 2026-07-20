from fastapi import APIRouter
from app.core.config import APP_NAME, APP_VERSION
from app.core.database import check_database_connection
from fastapi import Depends
from app.crud.note import get_notes
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.note import NoteCreate, NoteResponse
from app.crud.note import create_note

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

@router.get("/db-health")
def database_health():

    if check_database_connection():
        return {
            "database": "connected"
        }
    
    return {
        "database": "disconnected"
    }

@router.post(
    "/notes",
    response_model=NoteResponse,
)
def create_new_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
):
    return create_note(db, note)

@router.get(
    "/notes",
    response_model=list[NoteResponse],
)
def read_notes(
    db: Session = Depends(get_db),
):
    return get_notes(db)