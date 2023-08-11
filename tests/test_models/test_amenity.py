#!/usr/bin/python3
"""
unittest for amenity
"""


import unittest
from datetime import datetime
from models import amenity
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmen(unittest.TestCase):
    """test for amentiy class"""
    def test_amen(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity.id, str)
        self.assertEqual(Amenity.name, "")


if __name__ == '__main__':
    unittest.main()
