from fridge import Fridge
import unittest


class TestFridge(unittest.TestCase):
    def setUp(self) -> None:
        self.fridge = Fridge()
        self.fridge.add("milk", 2)
        self.fridge.add("potato", 2.5)

    def test_add(self):
        self.fridge.add("sausage", 0.5)
        self.assertEqual(self.fridge.contents['sausage'], 0.5)
        self.fridge.add("potato", 0.5)
        self.assertEqual(self.fridge.contents['potato'], 3.0)

    def test_remove(self):
        self.fridge.remove("milk", 1)
        self.assertEqual(self.fridge.contents['milk'], 1)
        self.fridge.remove("carrot", 0.3)
        self.assertRaises(KeyError, self.fridge.contents['carrot'], 'carrot')


if __name__ == "__main__":
    unittest.main()
