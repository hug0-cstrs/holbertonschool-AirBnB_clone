#!/usr/bin.python3
"""
    Module of Unittests for models/user.py

"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class Test_User(unittest.TestCase):
    """
        Tests of the subclass User, it inherit from BaseModel
    """
    @classmethod
    def setUpClass(cls):
        cls.user = User()
        cls.user.email = 'james.bond@gmail.com'
        cls.user.first_name = 'James'
        cls.user.last_name = 'Bond'
        cls.user.password = '0000'

    def test_NameAttribut(self):
        # test value of attribut.
        self.assertEqual(self.user.email, "james.bond@gmail.com")
        self.assertEqual(self.user.first_name, "James")
        self.assertEqual(self.user.last_name, "Bond")
        self.assertEqual(self.user.password, "0000")

    def test_user(self):
        """ checks user's attributes """
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))
        self.assertEqual(str, type(User.password))
        self.assertEqual(str, type(User.email))

    def test_SubclassBaseModel(self):
        # test is subclass
        self.assertTrue(issubclass(User, BaseModel))
