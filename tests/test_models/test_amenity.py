import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        self.amenity = Amenity()

    def test_name(self):
        self.assertEqual(self.amenity.name, "")


if __name__ == '__main__':
    unittest.main()