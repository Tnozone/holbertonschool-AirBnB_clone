import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_create_instance(self):
        self.assertIsInstance(self.model, BaseModel)

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict_returns_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
