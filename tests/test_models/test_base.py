from models.base_model import BaseModel
from datetime import datetime
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    
    def test_id_is_uuid(self):
        # Vérifie que l'id de l'objet est un UUID valide
        model = BaseModel()
        self.assertTrue(uuid.UUID(model.id))
        
    def test_created_and_updated_at_are_datetimes(self):
        # Vérifie que les attributs created_at et updated_at sont des objets datetime valides
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        
    """
    def test_save_updates_updated_at(self):
        # Vérifie que la méthode save met à jour l'attribut updated_at
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, old_updated_at)
    """    
    def test_to_dict_returns_dict(self):
        # Vérifie que la méthode to_dict renvoie un dictionnaire contenant les attributs de l'objet
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        
if __name__ == '__main__':
    unittest.main()