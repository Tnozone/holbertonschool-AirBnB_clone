#!/usr/bin/python3
"""CONSOLE DE LA CONSOLE AIRBNB"""


import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand qui herite cmd.Cmd"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()