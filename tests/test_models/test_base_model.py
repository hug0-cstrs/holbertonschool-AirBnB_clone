#!/usr/bin.python3
"""
    Module of Unittests for models/base_model.py
"""


import unittest
from models.base_model import BaseModel
import os
from datetime import datetime
import models
from unittest.mock import patch


class TestBaseModel_Attribut(unittest.TestCase):

    def test_no_args(self):
        # test if no arg instantiated
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_twoModel_uniqID(self):
        # test if 2 creation not the same ID
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()
        self.assertNotEqual(basemodel1.id, basemodel2.id)

    def test_publicID(self):
        # test that ID is attribut string
        basemodel3 = BaseModel()
        self.assertEqual(type(basemodel3.id), str)
        # test ID can be modify
        basemodel3.id = "123123123"
        self.assertEqual("123123123", basemodel3.id)

    def test_publicCreated_at(self):
        # test that created_at is type datetime
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)
        # test created_at can be modify
        bm.created_at = '2022-02-22T10:02:02.02'
        self.assertEqual("2022-02-22T10:02:02.02", bm.created_at)

    def test_publicUpdate_at(self):
        # test that update_at is public and type datetime
        basemodel3 = BaseModel()
        self.assertIsInstance(basemodel3.updated_at, datetime)
        # test updated_at can be modify
        basemodel3.updated_at = '2022-02-22T10:02:02.02'
        self.assertEqual("2022-02-22T10:02:02.02", basemodel3.updated_at)


class TestBaseModel_MethodStr(unittest.TestCase):

    def test_returnStrMethod(self):
        # test format return [class] (id) {dict attribut}
        basemodel4 = BaseModel()
        basemodel4.id = "123"
        basemodel4.created_at = '2022-02-22T02:02:02.02'
        bm4_str = basemodel4.__str__()
        # test classe + new ID
        self.assertIn("[BaseModel] (123)", bm4_str)
        # test new ID in dict attributs
        self.assertIn("'id': '123'", bm4_str)
        # test created_at if change
        answer = "'created_at': " + "'2022-02-22T02:02:02.02'"
        self.assertIn(answer, bm4_str)

        def test_str(self):
            # test format output str method
            bm2 = BaseModel()
            with patch('builtins.print') as mock_print:
                expected_output = f"[BaseModel] ({bm2.id}) {bm2.__dict__}"
                str(bm2)
            mock_print.assert_called_with(expected_output)


class TestBaseModel_MethodSave(unittest.TestCase):

    @classmethod
    def setUp(self):
        """ Remove json file if exist"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_saveNewInstance(self):
        # test if create store in storage
        self.assertIn(BaseModel(), models.storage.all().values())

    @patch.object(models.storage, 'save')
    def test_save(self, mock_save):
        bm3 = BaseModel()
        old_updated_at = bm3.updated_at
        bm3.save()
        self.assertNotEqual(old_updated_at, bm3.updated_at)
        mock_save.assert_called_once()


class TestBaseModel_MethodToDict(unittest.TestCase):

    def test_toDict(self):
        # test return is dict
        basemodel = BaseModel()
        self.assertTrue(dict, type(basemodel.to_dict()))

    def test_toDict_rightKeys(self):
        # test if dict contains key id, created_at, updated_at, __class__
        basemodel = BaseModel()
        self.assertIn("id", basemodel.to_dict())
        self.assertIn("created_at", basemodel.to_dict())
        self.assertIn("updated_at", basemodel.to_dict())
        self.assertIn("__class__", basemodel.to_dict())

    def test_toDict_newField(self):
        # test if dict contains new field
        basemodel = BaseModel()
        basemodel.name = "Betty"
        basemodel.blaze = "Boop"
        self.assertIn("name", basemodel.to_dict())
        self.assertIn("blaze", basemodel.to_dict())

    def test_toDict_datetimeSTR(self):
        # test if created_at and updated_at are str.
        basemodel = BaseModel()
        basemodel_dict = basemodel.to_dict()
        self.assertEqual(str, type(basemodel_dict["created_at"]))
        self.assertEqual(str, type(basemodel_dict["updated_at"]))
