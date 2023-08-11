#!/usr/bin/python3
"""
unittest for city
"""


import unittest
from datetime import datetime
from models import city
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """test for amentiy class"""
    def test_city(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city.id, str)
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")


if __name__ == '__main__':
    unittest.main()
