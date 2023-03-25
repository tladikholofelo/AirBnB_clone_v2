#!/usr/bin/python3
"""This module defines the City class."""
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel):
    """Represents a city. 

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city. 
    """
    __tablename__ = "cities"
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
    else:
        state_id = ""
        name = ""
