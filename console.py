#!/usr/bin/python3
"""Console interface module"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
