#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models using SQL Alchemy
    connecting to a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """The DBStorage constructor"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all instances of a given class if passed as argument
        or all classes otherwise"""
        classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City,
            'Amenity': Amenity, 'Review': Review
        }
        q_dict = {}

        if cls:
            if type(cls) == str:
                for obj in self.__session.query(classes[cls]).all():
                    q_dict[cls + '.' + obj.id] = obj
            else:
                print(cls)
                for obj in self.__session.query(cls).all():
                    print(obj)
                    q_dict[cls.__name__ + '.' + obj.id] = obj
        else:
            for cls_name, cls_val in classes.items():
                for obj in self.__session.query(cls_val).all():
                    q_dict[cls_name + '.' + obj.id] = obj

        return q_dict

    def new(self, obj):
        """Adds a new instance of the class to the SQLAlchemy session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Saves all changes to the database using the SQLAlchemy session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all schema in the database and initializes a session
        using SQLAlchemy"""
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Closes connection"""
        self.__session.close()
