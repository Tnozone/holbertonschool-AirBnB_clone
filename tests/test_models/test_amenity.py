import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        self.amenity = Amenity()

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_name(self):
        self.assertEqual(self.amenity.name, "")

    def test_str(self):
        s = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                  self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), s)

    def test_to_dict(self):
        d = self.amenity.to_dict()
        self.assertTrue(isinstance(d, dict))
        self.assertEqual(d['__class__'], 'Amenity')
        self.assertEqual(d['name'], self.amenity.name)


if __name__ == '__main__':
    unittest.main()