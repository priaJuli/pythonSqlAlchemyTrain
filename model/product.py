from sqlalchemy import create_engine, Column, Integer, String, DateTime, text, func
from typing import List


from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY, JSON, JSONB

from datetime import datetime

from .base_model import BaseModel


class Product(BaseModel):
    __tablename__ = "product"  # Explicitly set table name
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    owner_id: Mapped[int] = mapped_column(Integer)
    harga: Mapped[int] = mapped_column(Integer)
    variation: Mapped[List[str]]  = mapped_column(ARRAY(String))
