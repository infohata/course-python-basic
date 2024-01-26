import unittest

def divide(x, y):
    return x / y

def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

from matuojam_primes import is_prime


class TestIsPrime(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

    def test_not_prime(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))


class TestAssertMethods(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(3 + 2, 5, "nelygus")

    def test_assertTrue(self):
        self.assertTrue(3 < 4, "neteisinga")

    def test_assertFalse(self):
        self.assertFalse(3 > 4, "turi buti neteisingai")

    def test_assertIs(self):
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b)

    def test_assertIsNone(self):
        self.assertIsNone(None)

    def test_integer_division(self):
        self.assertEqual(divide(10, 5), 10 // 5)


class MyClass:
    def __init__(self, x):
        self.x = x

    def add(self, y):
        self.x += y
        return self.x


class TestMyClass(unittest.TestCase):
    def setUp(self): 
        self.obj = MyClass(5)
        self.obj.add(5)

    def test_add(self):
        self.assertEqual(self.obj.add(3), 13)

    def test_add_more(self):
        self.assertEqual(self.obj.add(5), 15)
        self.assertEqual(self.obj.add(-10), 5)


if __name__ == "__main__":
    unittest.main()
