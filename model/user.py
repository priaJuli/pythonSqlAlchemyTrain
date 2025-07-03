from sqlalchemy import Column, Integer, String, DateTime, text, func
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import BaseModel


class User(BaseModel):
    __tablename__ = "user"  # Explicitly set table name
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
