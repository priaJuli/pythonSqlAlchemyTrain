from sqlalchemy import Column, Integer, String, DateTime, text, func
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import BaseModel
from typing import Dict, Any
from sqlalchemy.dialects.postgresql import JSONB


class Item(BaseModel):
    __tablename__ = "item"  # Explicitly set table name
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    owner_id: Mapped[int] = mapped_column(Integer)
    attribute: Mapped[Dict[str, Any]] = mapped_column(JSONB, nullable=True)
