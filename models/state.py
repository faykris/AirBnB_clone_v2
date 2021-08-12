#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
import models
from models.city import City
=======
>>>>>>> 4d81c127a453772ada34675c518592fc7e29efef
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
            cities = relationship("City",
                                backref="state",
                                cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """ Returns the list of City instances with
            state_id == current State.id """
            all_cities = models.storage.all(City)
            state_cities = []
            for city_ins in all_cities.values():
                if city_ins.state_id == self.id:
                    state_cities.append(city_ins)
            return state_cities
