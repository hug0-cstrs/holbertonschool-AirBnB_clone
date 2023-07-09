#!/usr/bin/python3
"""
Class that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """ Class that serializes and deserializes JSON objects """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        from models.base_model import BaseModel
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dictionary, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised) """
        from models import base_model
        from models import user
        from models import amenity
        from models import city
        from models import place
        from models import review
        from models import state

        class_dict = {"BaseModel": base_model, "Amenity": amenity,
                      "City": city, "Place": place,
                      "Review": review, "State": state, "User": user}

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                reloaded_objects = {}
                reloaded_objects = json.load(file)
                for key, value in reloaded_objects.items():
                    class_name = value['__class__']
                    if class_name in class_dict:
                        cls = getattr(class_dict[class_name], class_name)

                    obj = cls(**value)
                    self.__objects[key] = obj
