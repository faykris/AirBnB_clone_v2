#!/usr/bin/python3
""" DB Module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


uname = os.environ.get('HBNB_MYSQL_USER')
upass = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
db = os.environ.get('HBNB_MYSQL_DB')
u_env = os.environ.get('HBNB_ENV')

class DBStorage:
    """DataBase Manager"""
    __engine = None
    __session = None

    def __init__(self):
        """Class constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:/{}'.
                                      format(uname, upass, host, db),
                                      pool_pre_ping=True)

        if u_env == "test":
            Base.metadata.drop_all(engine)

    def all(self, cls=None)
        """Return all obj of a class"""
        query_dict = {}
        if cls == None:
            sql = self.__session.query(State, User, City, Amenity,
                                       Place, Review)
            result = sql.all()
            for obj in result:
                key = obj.__class__.__name__ + "." + obj.id
                query_dict[key] = obj
        else:
            sql = self.__session.query(cls)
            result = sql.all()
            for obj in result:
                key = obj.__class__.__name__ + "." + obj.id
                query_dict[key] = obj
        return query_dict

    def new(self, obj):
        """Add new obj to a db"""
        self.__session.add(obj)

    def save(self):
        """Save the current changes in the db"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an obj"""
        if obj:
            sql = self.__session.delete(obj)

    def reload(self):
        """Make tables and make a session"""
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
