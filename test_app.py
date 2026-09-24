import unittest
from app import health_message

class TestApp(unittest.TestCase):
    def test_health(self):
        self.assertIn("healthy", health_message())

if __name__ == "__main__":
    unittest.main()
