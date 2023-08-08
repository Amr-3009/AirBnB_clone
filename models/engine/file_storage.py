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


class FileStorage():
    """
    File Storage class
    attrs:
        __file_path: str to json file
        __objects: dict that will store objects by class name
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return method for all objects
        """
        return(self.__objects)

    def new(self, obj):
        """
        sets key/value pair in dict
        Key format: <obj class name>.<id>
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """saves obj to json file"""
        with open(self.__file_path, mode="w+") as myFile:
            return myFile.write(json.dumps({key: value.to_dict() for key, value
                                in self.__objects.items()}))

    def reload(self):
        """loads saved ojects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as js_f:
                for key, obj in json.loads(js_f.read()).items():
                    obj = eval(obj['__class__'])(**obj)
                    FileStorage.__objects[key] = obj
