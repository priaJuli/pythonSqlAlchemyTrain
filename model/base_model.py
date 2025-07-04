from sqlalchemy import create_engine, Column, Integer, String, DateTime, text, func, Text

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker, Session, Mapped, mapped_column
from sqlalchemy.orm import scoped_session

from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Define the base for declarative models
Base = declarative_base()

userdb = os.getenv('DB_USER')
dbpass = os.getenv('DB_PASSWD')
dbhost = os.getenv('DB_HOST')
dbname = os.getenv('DB_NAME')
dbtype = os.getenv('DB_TYPE')

DATABASE_URL = f"{dbtype}+psycopg://{userdb}:{dbpass}@{dbhost}/{dbname}"
engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Session = scoped_session(SessionLocal)

class TimestampMixin:
    """Adds created at and updated at timestamps to a model."""
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __repr__(self):
        columns = self.__table__.columns.keys()
        values = ', '.join(f'{col}={getattr(self, col)}' for col in columns)
        return f'<{self.__class__.__name__}({values})>'


class BaseModel(Base, TimestampMixin):
    """Base class to add common database operations to models."""

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    session: Session
    __allow_unmapped__ = True
    __abstract__ = True

    def __init__(self,  **kwargs):
        self.session = Session
        super().__init__(**kwargs)

    def save(self):
        self.session.add(self)
        self.session.commit()
        self.session.refresh(self)

    @classmethod
    def all(cls):
        return Session.query(cls).all()

    @classmethod
    def where(cls,  column: str, value: str):
        return Session.query(cls).filter(getattr(cls, column)  == value)

    @classmethod
    def find(cls,  id: int):
        return Session.query(cls).filter(cls.id == id).first()

    @classmethod
    def selectRaw(cls,  query: str):
        """Executes a raw SELECT query and returns the results."""
        return Session.execute(text(query)).fetchall()

    @classmethod
    def groupByRaw(cls,  group_by: str):
        """Applies a raw GROUP BY clause to the query."""
        return Session.query(cls).group_by(text(group_by))

    @classmethod
    def whereIn(cls, column, value: str):
        """Searches if a string value is contained within an array column (PostgreSQL ARRAY)."""
        column = getattr(cls, column)
        return Session.query(cls).filter(func.lower(column.cast(Text)).like(f"%{value.lower()}%"))

    @classmethod
    def where_raw(cls, raw_condition: str):
        """Applies a raw SQL WHERE condition to the query."""
        return Session.query(cls).filter(text(raw_condition))

def create_db_and_tables():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
