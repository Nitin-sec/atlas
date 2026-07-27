from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.models import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    hashed_password: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    notes = relationship(
        "Note", 
        back_populates="owner",
        cascade="all, delete-orphan",
    )