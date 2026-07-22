from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.config import APP_NAME, APP_VERSION
from app.core.database import check_database_connection, get_db

from app.crud.note import (
    create_note,
    delete_note,
    get_note,
    get_notes,
    update_note,
)

from app.schemas.note import (
    NoteCreate,
    NoteResponse,
    NoteUpdate,
)

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
        return {"database": "connected"}

    return {"database": "disconnected"}


@router.post(
    "/notes",
    response_model=NoteResponse,
    tags=["Notes"],
)
def create_new_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
):
    return create_note(db, note)


@router.get(
    "/notes",
    response_model=list[NoteResponse],
    tags=["Notes"],
)
def read_notes(
    db: Session = Depends(get_db),
):
    return get_notes(db)


@router.get(
    "/notes/{note_id}",
    response_model=NoteResponse,
    tags=["Notes"],
)
def read_note(
    note_id: int,
    db: Session = Depends(get_db),
):
    note = get_note(db, note_id)

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        )

    return note


@router.put(
    "/notes/{note_id}",
    response_model=NoteResponse,
    tags=["Notes"],
)
def update_existing_note(
    note_id: int,
    updated_note: NoteUpdate,
    db: Session = Depends(get_db),
):
    note = update_note(db, note_id, updated_note)

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        )

    return note


@router.delete(
    "/notes/{note_id}",
    tags=["Notes"],
)
def delete_existing_note(
    note_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_note(db, note_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        )

    return {
        "message": "Note deleted successfully"
    }