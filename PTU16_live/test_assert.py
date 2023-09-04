import unittest


def dalyba(pirmas, antras):
    return pirmas // antras

def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


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

    def test_dalyba(self):
        self.assertEqual(dalyba(10, 3), 10 // 3)


class TestIsPrimeFunction(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

    def test_non_prime(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))

if __name__ == '__main__':
    unittest.main()
