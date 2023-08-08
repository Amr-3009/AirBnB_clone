#!/usr/bin/python3
"""Console Init"""

import sys
import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models import storage

list_items = ["BaseModel", "City", "State", "User", "Place", "Review", "Amenity"]

class HBNBCommand(cmd.Cmd):
    """
    HBNB CMD Class
    used to create, use and manage all HBnB command
    Inherits from cmd
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """repeats line on receiving empty line"""
        pass

    def can_exit(self):
        """enables exiting of the cmd loop"""
        return True

    def do_quit(self, s):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, s):
        """Sends EoF to quit"""
        exit()

    def do_create(self, model_type="None"):
        """
        creates a new instance of BaseModel
        saves it to a JSON file and prints the ID
        """
        if model_type == "" or None:
            print("** class name missing **")
        elif model_type not in list_items:
            print("** class doesn't exist **")

        else:
            if model_type == "BaseModel":
                new_model = BaseModel()
            elif model_type == "State":
                new_modell = State()
            elif model_type == "City":
                new_modell = City()
            elif model_type == "Place":
                new_modell = Place()
            elif model_type == "Amenity":
                new_modell = Amenity()
            elif model_type == "Review":
                new_modell = Review()
            elif model_type == "User":
                new_modell = User()
            print(new_model.id)
            storage.new(new_model)
            storage.save()

    def do_show(self, model_key=None):
        """
        Prints the string representation of instance
        """

        class_name = None
        model_id = None
        if model_key != "":
            try:
                class_name = model_key.split(" ")[0]
                model_id = model_key.split(" ")[1]
            except IndexError:
                pass
            if class_name is None:
                print("** class name missing **")
            elif class_name not in list_items:
                print("** class doesn't exist **")
            elif model_id is None:
                print("** instance id missing **")
            else:
                model_key = class_name + "." + model_id
                key_is = False
                for key in storage.all().keys():
                    if key == model_key:
                        print(storage.all().get(key))
                        key_is = True
                        break
                if key_is is not True:
                    print("** no instance found **")

