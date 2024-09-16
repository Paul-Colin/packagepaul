import unittest

from packagepaul.main import packagepaul, test 

class TestMain(unittest.TestCase):
    def test_something(self):
        self.assertEqual(18,test)

if __name__ == '__main__': 
    unittest.TestCase