#!/usr/bin/python3
"""A test module for the BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest for class BaseModel"""
    def setUp(self):
        """Set up for the tests"""
        self.my_model = BaseModel()

    def test_init(self):
        """Test for initialization"""
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_str(self):
        """Test for str method"""
        self.assertEqual(str(self.my_model), f"[BaseModel]\
 ({self.my_model.id}) {self.my_model.__dict__}")

    def test_save(self):
        """Test for save method"""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(old_updated_at, self.my_model.updated_at)

    def test_to_dict(self):
        """Test for to_dict method"""
        model_dict = self.my_model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.my_model.id)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
