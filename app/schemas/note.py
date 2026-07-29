from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

TitleField = Annotated[
    str,
    Field(
        min_length=3,
        max_length=100,
        strip_whitespace=True,
        description="Title of the note",
    ),
]

ContentField = Annotated[
    str, 
    Field(
        min_length=5,
        max_length=5000,
        strip_whitespace=True,
        description="Content of the note",
    ),
]

class NoteCreate(BaseModel):
    title: TitleField
    content: ContentField

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str

    model_config = ConfigDict(from_attributes=True)

class NoteUpdate(BaseModel):
    title: TitleField
    content: ContentField