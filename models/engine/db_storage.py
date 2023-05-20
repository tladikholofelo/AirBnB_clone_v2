#!/usr/bin/python3
"""This module defines the sqlAlchemy class."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    """Database storage engine for mysql storage."""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a new dbstorage instance."""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                                           HBNB_MYSQL_USER,
                                           HBNB_MYSQL_PWD,
                                           HBNB_MYSQL_HOST,
                                           HBNB_MYSQL_DB
                                       ), pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary: (like FileStorage)
        key = <class-name>.<object-id>
        value = object
        """
        dct = {}
        if cls is None:
            for c in classes.values():
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dct[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dct[key] = obj
        return dct

    def new(self, obj):
        """Adds an object."""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        """Commits (saves) all changes."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object."""
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """Reloads the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """Closes sqlAlchemy."""
        self.__session.remove()
