#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Review(BaseModel, Base):
    """Class for Review
    Attributes:
        place_id: the place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"
    text = Column(String(1204), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
