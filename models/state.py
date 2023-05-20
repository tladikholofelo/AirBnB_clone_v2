#!/usr/bin/python3
"""This module defines the State class."""
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """Represents a state.
    
    Attributes:
        name (str): The name of the state.    
    """
    __tablename__ = 'states'
    if storage_type != 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

    @property
    def cities(self):
        """Returns list of City instances with state_id = current State.id.
        FileStorage relationship between State and City.
        """
        city_objs = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_objs.append(city)
            return city_objs
