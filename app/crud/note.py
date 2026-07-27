from typing import List

from sqlalchemy.orm import Session

from app.models.note import Note
from app.models.user import User
from app.schemas.note import NoteCreate, NoteUpdate


def create_note(
    db: Session,
    note: NoteCreate,
    owner: User,
) -> Note:

    db_note = Note(
        title=note.title,
        content=note.content,
        owner_id=owner.id,
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note


def get_notes(
    db: Session,
    owner: User,
) -> List[Note]:

    return (
        db.query(Note)
        .filter(Note.owner_id == owner.id)
        .all()
    )


def get_note(
    db: Session,
    note_id: int,
    owner: User,
) -> Note | None:

    return (
        db.query(Note)
        .filter(
            Note.id == note_id,
            Note.owner_id == owner.id,
        )
        .first()
    )


def update_note(
    db: Session,
    note_id: int,
    updated_note: NoteUpdate,
    owner: User,
) -> Note | None:

    note = get_note(
        db,
        note_id,
        owner,
    )

    if note is None:
        return None

    note.title = updated_note.title
    note.content = updated_note.content

    db.commit()
    db.refresh(note)

    return note


def delete_note(
    db: Session,
    note_id: int,
    owner: User,
) -> bool:

    note = get_note(
        db,
        note_id,
        owner,
    )

    if note is None:
        return False

    db.delete(note)
    db.commit()

    return True