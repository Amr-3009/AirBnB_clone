#!/usr/bin/python3
"""
unittest for basemodel
"""

import pep8
import unittest
import os
from models import base_model
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class Test_Base_Model_outputs(unittest.TestCase):
    """Test_Base_outputs"""

    def test_unique_id(self):
        """test_uuid method"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1, instance2)

    def test_id_type(self):
        """tests if id is correct"""
        instance1 = BaseModel()
        self.assertEqual('<class \'str\'>', str(type(instance1.id)))

    def test_exec_file(self):
        """test exe files"""
        read = os.access("models/base_model.py", os.R_OK)
        self.assertEqual(True, read)
        write = os.access("models/base_model.py", os.W_OK)
        self.assertEqual(True, write)
        exec = os.access("models/base_model.py", os.X_OK)
        self.assertEqual(True, exec)

    def test_save(self):
        """test for save method"""
        inst1 = BaseModel()
        before_save = inst1.updated_at
        inst1.save()
        after_save = inst1.updated_at
        self.assertNotEqual(before_save, after_save)

    def test_dict(self):
        """Tests for to_dict method"""
        inst1 = BaseModel()
        inst1_user = User()
        self.assertEqual('<class \'dict\'>', str(type(inst1.to_dict())))

        updated_expect_format = inst1.updated_at.isoformat()
        created_expect_format = inst1.created_at.isoformat()
        class_attr_value_expect = type(inst1_User).__name__
        updated_act_format = inst1.to_dict()["updated_at"]
        created_act_format = inst1.to_dict()["created_at"]
        class_attr_value_act = inst1_User.to_dict()['__class__']

        self.assertEqual(updated_expect_format, updated_act_format)
        self.assertEqual(created_expect_format, created_act_format)
        self.assertEqual(class_attr_value_expect, class_attr_vale_act)


class TestPEP8(unittest.TestCase):
    """pycodestyle"""
    def test_pep8(self):
        """pycodestyle test"""
        style = pep8.StyleGuide(quiet=True)
        base_model = "models/base_model.py"
        test_base_model = "tests/test_models/test_base_model.py"
        result = style.check_files([base_model, test_base_model])
        self.assertEqual(result.total_errors, 0)


class TestDocStrings(unittest.TestCase):
    """test docstrings"""

    def test_module(self):
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class(self):
        self.assertTrue(len(baseModel.__doc__) > 0)

    def test_method(self):
        for function in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
