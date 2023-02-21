#!/usr/bin/python3
"""tests pour FileStorage"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """Unittest por FileStorage"""

    my_model = BaseModel()

    def test_instanciates(self):
        """Test correct FileSotrage instance"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

     def test_file_path(self):
        """Test __file path works"""
        path = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(path))

    def test_object(self):
        """Test __object est type dict apres deserialization"""
        object_dict = FileStorage._FileStorage__objects
        self.assertEqual(dict, type(object_dict))

    def test_all(self):
        """Test FileStorage: all()"""
        dict_return = {}
        FileStorage.all(None)
        self.assertEqual(os.path.isfile('file.json'), True)

if __name__ == "__main__":
    unittest.main()
