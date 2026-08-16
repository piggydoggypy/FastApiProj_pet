from app.models.models import Base
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4





class UsersORM(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    username: Mapped[str]
    email: Mapped[str]
    role: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[str]
