import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))

    def test_id(self):
        hello = State()
        self.assertEqual(str, type(hello.id))
