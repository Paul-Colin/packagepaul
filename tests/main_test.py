import unittest
from packagepaul.main import packagepaul , test
#test

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test = packagepaul(8,10)
        self.assertEqual(18, test)

    def test_something1(self):
        test = packagepaul(12,10)
        self.assertEqual(24, test)

if __name__ == '__main__':
    unittest.main()