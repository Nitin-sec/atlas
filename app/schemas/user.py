from typing import Annotated

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    StringConstraints,
)


UsernameField = Annotated[
    str,
    StringConstraints(
        min_length=3,
        max_length=30,
        strip_whitespace=True,
        pattern=r"^[a-zA-Z0-9_]+$",
    ),
]

PasswordField = Annotated[
    str,
    StringConstraints(
        min_length=8,
        max_length=128,
        strip_whitespace=True,
    ),
]


class UserCreate(BaseModel):
    username: UsernameField
    email: EmailStr
    password: PasswordField


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(
        from_attributes=True
    )


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str