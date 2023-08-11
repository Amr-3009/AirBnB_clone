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

list_items = ["BaseModel", "City", "State", "User",
              "Place", "Review", "Amenity"]


class HBNBCommand(cmd.Cmd):
    """
    HBNB CMD Class
    used to create, use and manage all HBnB command
    Inherits from cmd
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """ignores empty lines"""
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

    def do_destroy(self, args):
        """
        Deletes an instance based on the
        name and ID of the instance
        """

        flag = 0
        arg = args.split()
        if args == "":
            print("** class name missing **")
        elif arg[0] not in list_items:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            arg_key = (arg[0] + "." + arg[1])
            dict_items = storage.all()
            for key, value in dict_items.items():
                if key == arg_key
                del dict_items[key]
                flag = 1
                storage.save()
                storage.reload()
                return
            if flag == 0:
                print("** no instance found **")

    def do_all(self, args):
        """
        Prints all str representation of all instances
        """
        _list = []
        if args == "":
            for key, value in storage.all().items():
                _list.append(str(value))
            print(_list)
        elif args in list_items:
            for key, value in storage.all().items():
                if args == key.split(".")[0]:
                    _list.append(str(value))
            print(_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates instances based on name and ID
        by changing attr
        """
        flag = 0
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] not in list_items:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            index_key = (arg[0] + "." + arg[1])
            for key, value in storage.all().items():
                if key == index_key:
                    index_arg = len(arg[0]) + len(arg[1]) + len(arg[2]) + 3
                    val_arg = args[index_arg:]
                    if args[index_arg] == "\"":
                        index_arg += 1
                        val_arg = args[index_arg:-1]
                    if hasattr(value, arg[2]):
                        val_arg = type(getattr(value,
                                               arg[2]))(args[index_arg:])
                    setattr(value, arg[2], val_arg)
                    flag = 1
                    storage.save()
            if flag == 0:
                print("** no instance found **")
                return -1

    def default_cmd(self, args):
        """normal behaviour"""
        count = 0
        if len(args.split(".")) > 1:
            class_name = args.split(".")[0]
            if class_name in list_items:
                try:
                    if args.split(".")[1] == "all()":
                        self.do_all(class_name)
                    if args.split(".")[1] == "count()":
                        for key, obj in storage.all().items():
                            if key.split(".")[0] == class_name:
                                count += 1
                        print(count)
                    if args.split(".")[1].split("(")[0] == "show":
                        _id = args.split("\"")[1].split("\"")[0]
                        self.do_show(class_name + " " + _id)
                    if args.split(".")[1].split("\"")[0] == "destory":
                        _id = args.split("\"")[1].split("\"")[0]
                        self.do_destroy(class_name + " " + _id)

                    if args.split(".")[1].split("(")[0] == "update":
                        arg_ip = args.split(".", 1)[1]
                        arg_ip = arg_ip.split("(")[1][:-1].split(",")
                        if "{" not in arg_ip[1]:
                            _id = arg_ip[0][1:-1]
                            name = arg_ip[1][2:-1]
                            value = arg_ip[2][1:]
                            if value[0] == "\"":
                                value = value[1:-1]
                            self.do_update(class_name + "\"" +
                                           _id + " " + name + " " + value)

                        else:
                            _id = arg_ip[0][1:-1]
                            _dict = args.split(".")[1]
                            _dict = _dict.split("(")[1][:-1]
                            _dict = _dict.split("{")[1]
                            _dict = "{" + _dict
                            _dict2 = eval(_dict)
                            for key, value in _dict2.items():
                                flag = self.do_update(class_name + "\"" +
                                                      _id + " " + key + " " +
                                                      str(value))
                                if flag == -1:
                                    break
                except Exception:
                    cmd.Cmd.default(self, args)
            else:
                cmd.Cmd.default(self, args)


if __name__ == "__main__":
    comand = HBNBCommand()
    comand.cmdloop()
