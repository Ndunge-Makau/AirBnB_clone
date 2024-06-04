#!/usr/bin/python3
"""
Defines the BaseModel Class.
"""
import datetime
import models
from uuid import uuid4


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self):
        """Initialize base object."""
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns string representation"""
        return "[{}] ({}) <{}>".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = str(self.__class__.__name__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
