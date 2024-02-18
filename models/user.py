#!/usr/bin/python3
"""The module defines the class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.place import Place
from models.review import Review
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Theclass defines the user through various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="all, delete", backref="user")
    reviews = relationship("Review", cascade="all, delete", backref="user")
