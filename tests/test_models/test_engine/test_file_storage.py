#!/usr/bin.python3
"""
    Module of Unittest for models/engine/file_storage
"""


import unittest
import os
import json
from datetime import datetime
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_basic(unittest.TestCase):
    """ Test instantiation of the FileStorage class"""

    def test_FileStorage_normal(self):
        # test class Filestorage
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_AnormalArg(self):
        # test Filestorage if arg
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_Storage(self):
        # test if storage
        self.assertEqual(type(models.storage), FileStorage)

    def test_filepath_str(self):
        # test file_path string file.json
        self.assertTrue(str, FileStorage._FileStorage__file_path)

    def test_fileStorage_FilePath_str(self):
        # test filestorage.__file_path is str
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_fileStorage__objects_dict(self):
        # test filestorage.__objects is dict
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestFileStorage_MethodAll(unittest.TestCase):
    """ Test method all of the FileStorage class"""

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_all(self):
        # test output is dict
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_withArg(self):
        # test if try to use all with args
        with self.assertRaises(TypeError):
            models.storage.all(89)

    def test_all_with_objects(self):
        # test if the dictionary is stored in __objects.
        file_storage = FileStorage()
        base_model = BaseModel()
        objects = file_storage.all()
        self.assertIn("{}.{}".format(
            base_model.__class__.__name__, base_model.id), objects)
        self.assertEqual(objects["{}.{}".format(
            base_model.__class__.__name__, base_model.id)], base_model)

    def test_add_objects(self):
        # test if add an objects in dict __objects with a key nameclass.id
        file_storage = FileStorage()
        base_model = BaseModel()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertEqual(file_storage._FileStorage__objects[key], base_model)


class TestFileStorage_MethodNew(unittest.TestCase):
    """ Test method new of the FileStorage class"""

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_new(self):
        # create 1 instance of Class and subclass
        base1 = BaseModel()
        usr1 = User()
        state1 = State()
        place1 = Place()
        cyty1 = City()
        amenity1 = Amenity()
        review1 = Review()
        # storage all instance
        models.storage.new(base1)
        models.storage.new(usr1)
        models.storage.new(state1)
        models.storage.new(place1)
        models.storage.new(cyty1)
        models.storage.new(amenity1)
        models.storage.new(review1)
        # test for each key in storage and value
        self.assertIn("BaseModel." + base1.id, models.storage.all().keys())
        self.assertIn(base1, models.storage.all().values())
        self.assertIn("User." + usr1.id, models.storage.all().keys())
        self.assertIn(usr1, models.storage.all().values())
        self.assertIn("State." + state1.id, models.storage.all().keys())
        self.assertIn(state1, models.storage.all().values())
        self.assertIn("Place." + place1.id, models.storage.all().keys())
        self.assertIn(place1, models.storage.all().values())
        self.assertIn("City." + cyty1.id, models.storage.all().keys())
        self.assertIn(cyty1, models.storage.all().values())
        self.assertIn("Amenity." + amenity1.id, models.storage.all().keys())
        self.assertIn(amenity1, models.storage.all().values())
        self.assertIn("Review." + review1.id, models.storage.all().keys())
        self.assertIn(review1, models.storage.all().values())

        def test_new_with_objects(self):
            file_storage = FileStorage()
            base_model = BaseModel()
            objects = file_storage.all()
            self.assertIn("{}.{}".format(
                base_model.__class__.__name__, base_model.id), objects)
            self.assertEqual(objects["{}.{}".format(
                base_model.__class__.__name__, base_model.id)], base_model)

    def test_new_Args(self):
        # if use new with arg
        with self.assertRaises(TypeError):
            models.storage.new(User(), 45)

    def test_new_None(self):
        # if use new with None
        with self.assertRaises(AttributeError):
            models.storage.new(None)


class TestFileStorage_MethodSave(unittest.TestCase):
    """ Test method save of the FileStorage class"""

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_Arg(self):
        # test if save with args
        with self.assertRaises(TypeError):
            models.storage.save(456)


class TestFileStorage_MethodReload(unittest.TestCase):
    """ Test method save of the FileStorage class"""

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_reload_Arg(self):
        # if test reload with args
        with self.assertRaises(TypeError):
            models.storage.reload("user123")

    def test_reload(self):
        # test reload method
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload2(self):
        base = BaseModel()
        models.storage.save()
        base_key = "{}.{}".format(base.__class__.__name__, base.id)
        models.storage.all().clear()
        self.assertNotIn(base_key, models.storage.all())
        models.storage.reload()
        self.assertIn(base_key, models.storage.all())


if __name__ == "__main__":
    unittest.main()
