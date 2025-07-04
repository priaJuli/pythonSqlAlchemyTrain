from sqlalchemy import Column, Integer, String, DateTime, text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel
from typing import List


class User(BaseModel):
    __tablename__ = "user"  # Explicitly set table name
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)

    products: Mapped[List["Product"]] = relationship(back_populates="owner")
    items: Mapped[List["Item"]] = relationship(back_populates="owner")
