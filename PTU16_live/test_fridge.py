import unittest
from PTU16_live.fridge import Fridge


class TestFridgeAdd(unittest.TestCase):
    def setUp(self) -> None:
        self.fridge = Fridge()

    def test_add(self):
        self.fridge.add("obuoliai", 3)
        self.assertTrue(self.fridge.check("obuoliai", 3))
        self.assertFalse(self.fridge.check("obuoliai", 4))


class TestFridgeRemove(unittest.TestCase):
    def setUp(self) -> None:
        self.fridge = Fridge()
    
    def test_remove_partial(self):
        self.fridge.add("ananasai", 3)
        self.fridge.remove("ananasai", 2)
        self.assertTrue(self.fridge.check("ananasai", 1))
        self.assertFalse(self.fridge.check("ananasai", 2))

    def test_remove_full(self):
        self.fridge.add("morkos", 7)
        self.fridge.remove("morkos", 7)
        self.assertFalse(self.fridge.check("morkos", 1))
        self.assertFalse('morkos' in self.fridge.contents)

    def test_remove_too_much(self):
        self.fridge.add("kava", 2)
        self.fridge.remove("kava", 3)
        self.assertTrue('kava' in self.fridge.contents)
        self.assertTrue(self.fridge.check("kava", 2))


if __name__ == "__main__":
    unittest.main()
