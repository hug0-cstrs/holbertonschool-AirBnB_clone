#!/usr/bin/python3
"""
fun console AirB&B proyect
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import sys
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class HBNB for command lines
    """
    prompt = "(hbnb) "
    class_dict = {"BaseModel": BaseModel, "Amenity": Amenity,
                  "City": City, "Place": Place,
                  "Review": Review, "State": State, "User": User}

    def emptyline(self):
        """don't make nothing"""
        pass

    def do_create(self, classe_name=None):
        """Creates a new instance of BaseModel"""
        if not classe_name:
            print("** class name missing **")
            return

        if classe_name not in self.class_dict:
            print("** class doesn't exist **")
            return

        object = self.class_dict[classe_name]()
        object.save()
        print(object.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return
        else:
            classe_name = args_list[0]
            if classe_name not in self.class_dict:
                print("** class doesn't exist **")
                return

        if len(args_list) < 2:
            print("** instance id missing **")
            return
        else:
            obj_id = args_list[1]
            key = str(classe_name) + "." + str(obj_id)
            object = storage.all()
            if key not in object:
                print("** no instance found **")
                return
            else:
                print(object[key])
                return

    def do_destroy(self, arg):
        """ Deletes an instance passed """

        args_list = arg.split()

        if not arg:
            print("** class name missing **")
            return

        classe_name = args_list[0]
        if classe_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        id = args_list[1]
        key = str(classe_name) + "." + str(id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        else:
            del objects[key]
            storage.save()
            return

    def do_all(self, args):
        """Prints all instances or instances of a specific class"""
        objects = storage.all()
        if not args:
            for obj in objects.values():
                print(str(obj))
        else:
            class_name = args.split()[0]
            if class_name not in self.class_dict:
                print("** class doesn't exist **")
                return
            else:
                instance = []
                for obj in objects.values():
                    for value in self.class_dict.values():
                        if isinstance(obj, value):
                            instance.append(str(obj))
                print(instance)

    def do_update(self, args):
        """ Updates an instance based on the class name and id """

        args_list = args.split()

        if not args_list:
            print("** class name missing **")
            return
        else:
            classe_name = args_list[0]
            if classe_name not in self.class_dict:
                print("** class doesn't exist **")
                return

        if len(args_list) < 2:
            print("** instance id missing **")
            return
        else:
            id = args_list[1]
            key = str(classe_name) + "." + str(id)
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
                return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        else:
            attribute_name = args_list[2]

        if len(args_list) < 4:
            print("** value missing **")
            return
        else:
            attribute_value = args_list[3]

        setattr(objects[key], attribute_name, attribute_value)
        storage.save()
        return

    def do_EOF(self, args):
        """end_of_file"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
