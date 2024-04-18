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
            print("** class name missing **")
        # !!!!!!!!!!!!!!!!! dosesnt search for classes
        elif (line != "BaseModel"):
            print("** class doesn't exist **")
        else:
            new_obj = BaseModel()
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
            # delete object and update json
            del obj_dict[obj_key]
            storage.save()

    def do_all(self, line):
        objects = storage.all()
        object_list = []
        class_list = []
        # get class list
        for key in objects.keys():
            class_list.append(key.split(".")[0])

        for key, value in objects.items():
            if (line == ""):
                object_list.append(str(value))
            else:
                if (line.split()[0] == key.split(".")[0]):
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
        classes = []
        object_to_update = None
        for key in objects.keys():
            classes.append(key.split(".")[0])
        if cls not in classes:
            print("** class doesn't exist **")
            return
        # check for empty id
        if (len(words) < 2):
            print("** instance id missing **")
            return
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
        if getattr(object_to_update, words[2], None) is None:
            print("** value missing **")
            return
        setattr(object_to_update, words[2], words[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
