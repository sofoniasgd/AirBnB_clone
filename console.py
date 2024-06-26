#!/usr/bin/python3
"""Console interface module"""

import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """cmd interface for the project."""

    prompt = '(hbnb) '
    classes = ("BaseModel", "User", "Place", "State",
               "City", "Amenity", "Review")
    commands = ("all", "count", "destroy", "update")

    def precmd(self, line):
        """ preprocesses commandline to expand command set
        """
        # search for the alternate command style(class.command(options))
        pattern = r'\w+\.\w+\((("[^"]*")(,\s*"[^"]*")*)?\)'
        match = []
        match = re.findall(pattern, line)
        # if no match then return original line
        if len(match) == 0:
            return line
        # split line into class name, command, argument string
        line_words = line.split(".", 1)
        class_name = line_words[0]
        command_name = line_words[1].split("(")[0]
        if (command_name == "all"):
            command_name = "Instances"
        args = line_words[1].split("(")[1]
        args = args.replace(')', '')
        args = args.replace(',', '')
        args = args.replace('"', '')
        # convert into primary command style(command class args)
        new_line = command_name + " " + class_name + " " + args
        return new_line

    def emptyline(self):
        pass

    def default(self):
        pass

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF to exit the program")

    def do_count(self, line):
        """return instances of a class"""
        if (line == ""):
            print("** class name missing **")
        # dosesnt search for classes
        elif (line.split()[0] not in self.classes):
            print("** class doesn't exist **")
        else:
            count = 0
            words = line.split()
            class_name = words[0]
            obj_dict = storage.all()
            for key in obj_dict.keys():
                cls = key.split(".")[0]
                if cls == class_name:
                    count += 1
        print(count)

    def do_create(self, line):
        if (line == ""):
            print("** class name missing **")
        # dosesnt search for classes
        elif (line.split()[0] not in self.classes):
            print("** class doesn't exist **")
        else:
            # get class object from class name using getattr
            class_name = line.split()[0]
            cls = globals()[class_name]
            # create instance of the class and save it
            new_obj = cls()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        if (line == ""):
            print("** class name missing **")
            return
        words = line.split()
        cls = words[0]
        found_obj = None
        if (len(words) != 2):
            print("** instance id missing **")
            return
        # now class name is 'cls' and object id is 'obj_id'
        obj_id = words[1]
        obj_id = obj_id.replace('"', '')
        # get dict of all objects
        obj_dict = storage.all()
        obj_key = None
        if cls in self.classes:
            for key in obj_dict.keys():
                class_name = key.split(".")[0]
                object_name = key.split(".")[1]
                if (class_name == cls and object_name == obj_id):
                    # object found !!
                    obj_key = key
                    break
            if (obj_key is None):
                print("** no instance found **")
                return
        else:
            print("** class doesn't exist **")
            return
        obj = obj_dict[obj_key]
        print(obj)

    def do_destroy(self, line):
        # empty command
        if (line == ""):
            print("** class name missing **")
            return
        words = line.split()
        cls = words[0]
        found_obj = None
        # empty id
        if (len(words) != 2):
            print("** instance id missing **")
            return
        # now class name is 'cls' and object id is 'obj_id'
        obj_id = words[1]
        # get dict of all objects
        obj_dict = storage.all()
        obj_key = None
        if cls in self.classes:
            for key in obj_dict.keys():
                class_name = key.split(".")[0]
                object_name = key.split(".")[1]
                if (class_name == cls and object_name == obj_id):
                    # object found !!
                    obj_key = key
                    break
        else:
            print("** class doesn't exist **")
            return
        if (obj_key is None):
            print("** no instance found **")
            return
        # delete object and update json
        del obj_dict[obj_key]
        storage.save()

    def do_all(self, line):
        objects = storage.all()
        object_list = []
        for key, value in objects.items():
            if (line == ""):
                object_list.append(str(value))
            else:
                if (line.split()[0] in self.classes):
                    object_list.append(str(value))
        if (len(object_list) == 0):
            print("** class doesn't exist **")
            return
        else:
            print(object_list)

    def do_Instances(self, line):
        objects = storage.all()
        object_list = []
        words = line.split()
        cls = words[0]
        print("Instances")
        for key, value in objects.items():
            if (cls == key.split('.')[0]):
                object_list.append(str(value))
        if (len(object_list) == 0):
            print("** class doesn't exist **")
            return
        else:
            print(object_list)

    def do_update(self, line):
        # empty command
        if (line == ""):
            print("** class name missing **")
            return
        words = line.split()
        cls = words[0]
        objects = storage.all()
        object_to_update = None
        if cls not in self.classes:
            print("** class doesn't exist **")
            return
        # check for empty id
        if (len(words) < 2):
            print("** instance id missing **")
            retur
        cls += "." + words[1]
        for key, value in objects.items():
            if (cls == key):
                object_to_update = value
        if object_to_update is None:
            print("** no instance found **")
            return
        if len(words) < 3:
            print("** attribute name missing **")
            return
        if len(words) < 4:
            print("** value missing **")
            return
        setattr(object_to_update, words[2], words[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
