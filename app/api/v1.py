from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.security.dependencies import get_current_user
from app.models.user import User

from app.core.config import APP_NAME, APP_VERSION
from app.core.database import check_database_connection, get_db

from app.schemas.user import (
    UserCreate,
    UserResponse,
    Token,
)

from app.schemas.note import (
    NoteCreate,
    NoteResponse,
    NoteUpdate,
)

from app.crud.user import (
    create_user,
    get_user_by_email,
    get_user_by_username,
    authenticate_user,
)

from app.crud.note import (
    create_note,
    delete_note,
    get_note,
    get_notes,
    update_note,
)

from app.security.jwt import create_access_token

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


# ------------------------
# Notes
# ------------------------

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


# ------------------------
# Users
# ------------------------

@router.post(
    "/users/register",
    response_model=UserResponse,
    tags=["Users"],
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    if get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=409,
            detail="Email already registered",
        )

    if get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=409,
            detail="Username already taken",
        )

    return create_user(db, user)


@router.post(
    "/users/login",
    response_model=Token,
    tags=["Users"],
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(
        db,
        form_data.username,
        form_data.password,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    access_token = create_access_token(
        {
            "sub": user.username,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

@router.get(
    "/users/me",
    response_model=UserResponse,
    tags=["Users"],
)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user