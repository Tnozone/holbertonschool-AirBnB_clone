import unittest
from models.base_model import BaseModel
from datetime import datetime
import time

class TestBaseModel(unittest.TestCase):
    
    def setUp(self):
        self.model = BaseModel()

    def test_has_id(self):
        self.assertTrue(hasattr(self.model, 'id'))

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_has_created_at(self):
        self.assertTrue(hasattr(self.model, 'created_at'))

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_has_updated_at(self):
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        time.sleep(0.0001)  # Attendre un peu
        self.model.save()
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(self.model.to_dict(), dict)

    def test_to_dict_includes_class_name(self):
        self.assertEqual(self.model.to_dict()['__class__'], 'BaseModel')

    def test_to_dict_includes_created_at(self):
        self.assertIn('created_at', self.model.to_dict())

    def test_to_dict_includes_updated_at(self):
        self.assertIn('updated_at', self.model.to_dict())

    def test_to_dict_created_at_is_str(self):
        self.assertIsInstance(self.model.to_dict()['created_at'], str)

    def test_to_dict_updated_at_is_str(self):
        self.assertIsInstance(self.model.to_dict()['updated_at'], str)

    def test_str_returns_string(self):
        self.assertIsInstance(str(self.model), str)

    def test_str_includes_class_name(self):
        self.assertIn('BaseModel', str(self.model))

    def test_str_includes_id(self):
        self.assertIn(self.model.id, str(self.model))

    def test_save(self):
        """testing save"""
        i = self.value()
        i.save()
        key = self.name + "." + i.
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

if __name__ == '__main__':
    unittest.main()
