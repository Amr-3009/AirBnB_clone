#!/usr/bin/python3
"""
Class BaseModel
"""


import uuid
from datetime import datetime
import models


format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base Model class for every class"""
    def __init__(self, *args, **kwargs):
        """
        initialization of class
        """
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(value, format)
                    setattr(self, key, value)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string reprenstation of class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        """Method for saving an object"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an object"""
        dict_repr = dict(self.__dict__)
        dict_repr["__class__"] = type(self).__name__
        dict_repr["created_at"] = dict_repr["created_at"].isoformat()
        dict_repr["updated_at"] = dict_repr["updated_at"].isoformat()

        return dict_repr
