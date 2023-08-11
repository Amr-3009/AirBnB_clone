#!/usr/bin/python3
"""
unittest for review
"""


import unittest
from datetime import datetime
from models import review
from models.base_model import BaseModel
from models.review import Review


class TestRev(unittest.TestCase):
    """test for amentiy class"""
    def test_rev(self):
        review = Review()
        self.assertIsInstance(review,Review)
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review.id, str)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
