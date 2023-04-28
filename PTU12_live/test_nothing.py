import unittest

def divide(x, y):
    return x / y

class TestAssertMethods(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(3 + 2, 5)

    def test_assertTrue(self):
        self.assertTrue(3 < 5)

    def test_assertFalse(self):
        self.assertFalse(5 < 3)

    def test_assertIs(self):
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b)

    def test_assertIsNone(self):
        self.assertIsNone(None)

    def test_integer_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(2, 5), 0.4)
        self.assertAlmostEqual(divide(10, 3), 3.33333, 5)

if __name__ == '__main__':
    unittest.main()
