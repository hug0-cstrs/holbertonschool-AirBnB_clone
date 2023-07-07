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
from models import theClasses
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class HBNB for command lines
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """don't make nothing"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
        else:
            class_name = args.split()[0]
            if class_name not in ["BaseModel"]:
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
        elif args_list[0] not in ["BaseModel"]:
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
        elif args_list[0] not in ["BaseModel"]:
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
        """Prints all instances or instances of a specific class"""
        obj_dict = storage.all()
        if not args:
            print([str(obj) for obj in obj_dict.values()])
        else:
            class_name = args.split()[0]
            if class_name not in ["BaseModel"]:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in obj_dict.values()
                       if isinstance(obj, BaseModel)])

    def do_update(self, args):
        """ Updates an instance based on the class name and id """

        if not args:
            print("** class name missing **")
            return

        token = args.split()

        if token[0] not in theClasses:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                ob_id = val.id
                if ob_name == token[0] and ob_id == token[1].strip('"'):
                    if len(token) == 2:
                        print("** attribute name missing **")
                    elif len(token) == 3:
                        print("** value missing **")
                    else:
                        setattr(val, token[2], token[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_EOF(self, args):
        """end_of_file"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True


if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop()
