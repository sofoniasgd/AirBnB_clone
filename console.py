#!/usr/bin/python3
"""Console interface module"""

import cmd
from models.base_model import BaseModel


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
        elif (line != "BaseModel"):
            print("** class doesn't exist **")
        else:
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        if (line == ""):
            print("** class name missing  **")
        else:
            words = line.split()
        cls = words[0]
        obj_id = words[1]
        print("class={} id= {}".format(cls, obj_id))
        if (cls != "BaseModel"):
            print("** class doesn't exist **")
        elif (obj_id == ""):
            print("** instance id missing  **")
        print(cls.obj_id)
        # elif (cls.obj_id is None):
        #     print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
