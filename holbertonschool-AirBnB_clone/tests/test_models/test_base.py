import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_attributes(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
    
    def test_save(self):
        model = BaseModel()
        updated_at_before = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, updated_at_before)

    def test_str(self):
        model = BaseModel()
        self.assertIn(type(model).__name__, str(model))
        self.assertIn(model.id, str(model))

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)