from sqlalchemy.orm import Session
from app.models.note import Note
from app.schemas.note import NoteCreate
from typing import List
from app.schemas.note import NoteUpdate

def create_note(db: Session, note: NoteCreate) -> Note:
    db_note = Note(
        title=note.title,
        content=note.content,
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note

def get_notes(db: Session) -> List[Note]:
    return db.query(Note).all()

def get_note(db: Session, note_id: int) -> Note | None:
    return (
        db.query(Note)
        .filter(Note.id == note_id)
        .first()
    )

def update_note(
        db: Session,
        note_id: int,
        updated_note: NoteUpdate,
) -> Note | None:
    
    note = db.query(Note).filter(Note.id == note_id).first()

    if note is None:
        return None
    
    note.title = updated_note.title
    note.content = updated_note.content

    db. commit()
    db.refresh(note)

    return note