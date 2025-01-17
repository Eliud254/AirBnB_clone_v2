#!/usr/bin/python3
""" The State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv


class Amenity(BaseModel, Base):
    """The amenity"""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
