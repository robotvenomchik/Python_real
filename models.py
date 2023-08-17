from database import Base
from sqlalchemy import (
    Column, Integer, Float, String, DateTime, Boolean,
)
from sqlalchemy.dialects.postgresql import JSONB


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    login = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_conflict=Column(Boolean, default=False)

