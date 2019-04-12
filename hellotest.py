import unittest
from hello import hello


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(hello(), 'Hello World') 

if __name__ == "__main__":
    unittest.main()