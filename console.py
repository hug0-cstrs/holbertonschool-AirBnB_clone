#!/usr/bin/python3
""" Entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    class HBNB for command lines
    """
    prompt = "(hbnb) "

    valid_classes = [
        'BaseModel', 'User'
    ]

    def emptyline(self):
        """don't make nothing"""
        pass

    def do_EOF(self, args):
        """end_of_file"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
        else:
            class_name = args.split()[0]
            if class_name not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            else:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            obj_key = args_list[0] + "." + args_list[1]
            obj_dict = storage.all()
            if obj_key in obj_dict:
                print(obj_dict[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on class name and id"""

        args_list = args.split()
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            obj_key = args_list[0] + "." + args_list[1]
            obj_dict = storage.all()
            if obj_key in obj_dict:
                del obj_dict[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not
        on the class name
        """
        obj_dict = storage.all()
        if not args:
            print([str(obj) for obj in obj_dict.values()])
        else:
            class_name = args.split()[0]
            if class_name not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in obj_dict.values()
                       if isinstance(obj, BaseModel)])

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif len(args_list) == 2:
            print("** attribute name missing **")
        elif len(args_list) == 3:
            print("** value missing **")
        else:
            obj_key = args_list[0] + "." + args_list[1]
            obj_dict = storage.all()
            if obj_key in obj_dict:
                instance = obj_dict[obj_key]
                attribute_name = args_list[2]
                attribute_value = args_list[3]
                if hasattr(instance, attribute_name):
                    attribute_type = type(getattr(instance, attribute_name))
                    try:
                        casted_value = attribute_type(attribute_value)
                        # permet de convertir la valeur de l'attribut spécifié
                        setattr(instance, attribute_name, casted_value)
                        # Si la convertion a réussi, met à jour l'attribut
                        # dans l'instance avec la nouvelle valeur
                        instance.save()
                    except ValueError:
                        print("** value must be of type {} **"
                              .format(attribute_type.__name__))
                else:
                    print("** attribute doesn't exist **")
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
