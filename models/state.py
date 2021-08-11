#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage_type
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        states = relationship("City", backref='state')
    else:
        state_id = ""
        name = ""
