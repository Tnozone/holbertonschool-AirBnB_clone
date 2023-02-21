import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_review_attributes(self):
        """Test that attributes of Review class are correctly set"""

        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

if __name__ == '__main__':
    unittest.main()