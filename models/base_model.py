#!/usr/bin/python3
"""
Defines the BaseModel class.
"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel of the HBnB projects"""

    def __init__(self, *args, **kwargs):
        """
        initialization of class

        Args:
            *args (any): unused
            **kwargs (dict): key/value pairs of attributes
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        updates the updated_at attr
        with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Return dict representaion of the basemodel
        """
        redict = self.__dict__.copy()
        redict["created_at"] = self.created_at.isoformat()
        redict['updated_at'] = self.updated_at.isoformat()
        redict["__class__"] = self.__class__.__name__
        return redict

    def __str__(self):
        """
        return string representation of  basemodel
        """
        class_name = self.__class__.__name__
        return '[{}] ([]) []'.format(class_name, self.id, self.__dict__)
