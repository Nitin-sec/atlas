from pydantic import BaseModel

class NoteCreate(BaseModel):
    title:str
    content:str

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str

    model_config = {
        "from_attributes": True
    }

class NoteUpdate(BaseModel):
    title: str
    content: str