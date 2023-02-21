import unittest
from models.city import City

class TestCity(unittest.TestCase):
    
    def test_city_attributes(self):
        """Test that City class has the required attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))