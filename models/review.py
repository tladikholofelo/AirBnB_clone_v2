#!/usr/bin/python3
"""This module defines the Review class."""
from models.base_model import BaseModel
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, ForeignKey
from models import storage_type


class Review(BaseModel):
    Represents a review.
    
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.    
    """
    __tablename__ = 'reviews'
    if storage_type == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
