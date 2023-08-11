#!/usr/bin/python3
"""File Storage Testing"""


import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """file storage unit test"""
    def test_file_storage(self):
        fs = FileStorage()
        base_mod = BaseModel()
        fs.new(base_mod)
        self.assertIsInstance(fs, FileStorage)
        self.assertIsInstance(fs.all(), dict)
        self.assertIn("{}.{}".format("BaseModel", base_mod.id), fs.all())


if __name__ == '__main__':
    unittest.main()
