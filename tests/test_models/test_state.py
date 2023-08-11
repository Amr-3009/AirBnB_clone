#!/usr/bin/python3
"""
unittest for state
"""


import unittest
from datetime import datetime
from models import state
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """test for amentiy class"""
    def test_state(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state.id, str)
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
