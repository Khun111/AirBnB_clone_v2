#!/usr/bin/python3
""" City Module for HBNB project """
from .base_model import BaseModel
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from . import HBNB_TYPE_STORAGE
from .base_model import Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship(
        "Place", cascade="all, delete-orphan", backref="cities")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
