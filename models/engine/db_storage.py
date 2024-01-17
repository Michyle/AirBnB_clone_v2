#!/usr/bin/python3
"""Class for SQLAlchemy"""
from os import getenv
from sqlalchmey.orm import sessionmaker, scoped_session
from sqlalchmey import (create_engine)
from sqlalchmey.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Review
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """ creates tables in the environmental"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passed = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_HOST")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}' .format(user, passwd, host, db), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This returns a dictionary
        Return:
            return a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}",format(type(elem).__name__, elem.id)
                    dic[key] = elem
    def new(self, obj):
       """This adds a new element in the table"""
       self.__session.add(obj)

    def save(self):
        """saves changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an element in the table"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """configuration"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """this calls remove()"""
        self.__session.close()
