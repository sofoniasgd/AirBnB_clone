#!/usr/bin/python3
import cmd

class Mycmd(cmd.Cmd):
    def do_greet(self, line):
        print("hello")

    def do_printbox(self, line):
        for i in range(4):
            for j in range(4):
                print("#", end='')
            print()
        print("args=>{}".format(line))

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    Mycmd().cmdloop()
