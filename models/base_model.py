#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, Starting, DateTime

Base = declarative_base()

class BaseModel:
    """This class defines all common atttributes and methods for other classes"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow())) 
    updated_at = Column(DateTime, nullable=False,default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instantitaion of base model class Args:
            args: it wont be used
            kwargs: arguments for the construecor of the BaseModel
            Attributes:
                id: unique id generated
                created_at: date of creation
                updated_at: date updated
        """
        if kwargs:
            for key,value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime( value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setter(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not on kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """This returns a string
        Return:
            A string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(type(self).__name__,self.id, self.__dict__)

    def __repr__(Self):
        """This returns a string representation"""
        return self.__str__()

    def save(self):
        """This updates the public instace attribute UPdated_at to the current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """This creates a dictionary of the class and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict
    def delete(self):
        """delete object """
        models.storage.delete(self)
