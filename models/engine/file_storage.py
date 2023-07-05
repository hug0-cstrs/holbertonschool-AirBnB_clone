#!/usr/bin/python3
"""
Class that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import os
from models.base_model import BaseModel
from models.base_model import User
from models.base_model import State
from models.base_model import City
from models.base_model import Amenity
from models.base_model import Place
from models.base_model import Review


class FileStorage:
    """ Class that serializes and deserializes JSON objects """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dumps(dictionary, f)

    def reload(self):
        """ Deserializes __objects from the JSON file """
        my_dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                other_dict = json.loads(f.read())
                for key, val in other_dict.items():
                    self.new(my_dict[val['__class__']](**val))
