#!/usr/bin/python3
""" Entry point of the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """
    class HBNB for command lines
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """don't make nothing"""
        pass

    def do_EOF(self, args):
        """end_of_file"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
