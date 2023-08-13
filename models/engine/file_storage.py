#!/usr/bin/python3
"""
File Storage Module
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    File Storage class

    Attributes:
        _filepath: str to json file
        _obj: dict that will store objects by class name
    """

    _filepath = "file.json"
    _obj = {}

    def all(self):
        """
        return method for all objects
        """
        return FileStorage._obj

    def new(self, obj):
        """
        sets key/value pair in dict
        Key format: <obj class name>.<id>
        """
        FileStorage._obj["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """saves obj to json file"""
        obj_dict = FileStorage._obj
        obj_dict2 = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage._filepath, "w") as f:
            json.dump(obj_dict2, f)

    def reload(self):
        """loads saved ojects"""
        try:
            with open(FileStorage._filepath) as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
