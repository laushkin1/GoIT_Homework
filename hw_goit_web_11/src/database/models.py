from sqlalchemy import Column, Integer, String, TIMESTAMP
from pydantic import BaseModel, Field, EmailStr
from datetime import date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.database.db import engine


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    birthday = Column(TIMESTAMP)


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str = Field(default='+380123456789')
    birthday: date


class ContactRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str = Field(default='+380123456789')
    birthday: date
