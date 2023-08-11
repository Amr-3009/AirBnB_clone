#!/usr/bin/python3
"""
unittest for user
"""


import unittest
from datetime import datetime
from models import user
from models.base_model import BaseModel
from models.user import User


class TestUsr(unittest.TestCase):
    """test for amentiy class"""
    def test_Usr(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertIsInstance(user.id, str)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
