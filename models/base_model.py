#!/usr/bin/python3
"""
Parent class that will inherit
"""


import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """Initializes all attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    dataTime = "%Y-%m-%dT %H:%M:%S.%f"
                    val = datetime.strptime(kwargs[key], dataTime)
                if key != '__class__':
                    setattr(self, key, val)

    def __str__(self):
        """
        method for named
        """
        nameClass = self.__class__.__name__
        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates last update time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns dict with all keys/values of __dict__ of the instance"""
        copy_dict = self.__dict__.copy()
        copy_dict['__class__'] = type(self).__name__
        if not isinstance(copy_dict['created_at'], str):
            copy_dict['created_at'] = self.created_at.isoformat()
        if not isinstance(copy_dict['updated_at'], str):
            copy_dict['updated_at'] = self.updated_at.isoformat()
        return copy_dict
