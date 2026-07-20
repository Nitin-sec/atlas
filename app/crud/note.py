from sqlalchemy.orm import Session
from app.models.note import Note
from app.schemas.note import NoteCreate

def create_note(db: Session, note: NoteCreate) -> Note:
    db_note = Note(
        title=note.title,
        content=note.content,
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note