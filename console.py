#!/usr/bin/python3
"""Defines the HBnB console"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parser(arg):
    #searches for text inside curly braces
    curly_text = re.search(r"\{(.*?)\}", arg)
    #searches for text inside square brackets
    square_text = re.search(r"\[(.*?)\]", arg)

    if curly_text is None:
        if square_text is None:
            return [i.strip(',') for i in split(arg)
        else:
            var_a = split(arg[:square_text.span()[0]])
            var_b = [i.strip(',') for i in var_a]
            var_b.append(square_text.group())
            return var_b
    else:
        var_a = split(arg[:curly_text.span()[0]])
        var_b = [i.strip(',') for i in var_a]
        var_b.append(curly_text.group())
        return var_b


class HBNBCommand(cmd.Cmd):
    """
    Defines the HBnB command prompt

    Attributes:
        prompt (str): the prompt text
    """

    prompt = "(hbnb) "
    class_items = {"BaseModel", "User", "State", "City", "Place",
                   "Amenity", "Review"}

    def handle_emptyline(self):
        """Do nothing when a new line is passed"""
        pass

    def console_def(self, arg):
        """
        What the console is supposed to do for
        commands and error handling
        """
        cmd_dict = {"all": self.do_all, "show": self.do_show,
                    "destory": self.do_destroy,
                    "count": self.do_count, "update": self.do_update}

        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\[(.*?)\]", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in cmd_dict.key():
                    call = "{} {}".format(arg_list[0], command[1])
                    return cmd_dict[command[0]](call)
        print("** Unknown syntax: {} **".format(arg))
        return False

    def do_quit(self, arg):
        """
        quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        end of file to exit the program
        """
        print("")
        return True

    def do_create(self, arg):
        """
        Usage: create <class>
        Create a new class instance
        """
        arg_list = parser(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.class_items:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Usage: shows the string representation
        of a class given the id
        """
        arg_list = parser(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.class_items:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict['{}.{}'.format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """
        Usage: destroy a class given the id
        """
        arg_list = parser(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.class_items:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict['{}.{}'.format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """
        Usage: display string representation of 
        all instances
        """
        arg_list = parser(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.class_items:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(arg_list) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, arg):
        """
        Usage: count the number of instances 
        in a given class
        """
        arg_list = parser(arg)
        count = 0
        for obj in storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)


    def do_update(self, arg):
        """
        Usage: updates a class instance of a given id
        by changing attributes
        """
        arg_list = parser(arg)
        obj_dict = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.class_items:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg_list) == 4:
            obj = obj_dict['{}.{}'.format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__.keys():
                val = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = val(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
            elif type(eval(arg_list[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            for key, value in eval(arg_list[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    val = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
