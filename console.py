#!/usr/bin/python3
"""Console interface module"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """cmd interface for the project."""

    prompt = '(hbnb) '

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

    def do_create(self, line):
        if (line == ""):
            print("** class name missing  **")
        # !!!!!!!!!!!!!!!!! dosesnt search for classes
        elif (line != "BaseModel"):
            print("** class doesn't exist **")
        else:
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        if (line == ""):
            print("** class name missing  **")
            return
        words = line.split()
        cls = words[0]
        found_obj = None
        if (len(words) != 2):
            print("** instance id missing  **")
            return
        # now class name is 'cls' and object id is 'obj_id'
        obj_id = words[1]
        # get dict of all objects
        obj_dict = storage.all()
        obj_key = None
        classf = None
        for key in obj_dict.keys():
            cls_name = key.split(".")[0]
            if (cls_name == cls):
                # class found !!
                classf = 1
                if (key.split(".")[1] == obj_id):
                    # object found !!
                    obj_key = key
                    break
        if (classf is None):
            print("** class doesn't exist **")
            return
        elif (obj_key is None):
            print("** no instance found **")
            return
        else:
            obj = obj_dict[obj_key]
            print(obj)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
