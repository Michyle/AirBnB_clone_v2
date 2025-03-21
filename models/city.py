#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
    state_id: The state id
    name: imput name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(string(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="cities")
