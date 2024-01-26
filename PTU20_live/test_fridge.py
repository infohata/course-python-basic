from fridge import Fridge
import unittest


class TestFridge(unittest.TestCase):
    def setUp(self):
        self.fridge = Fridge()

    def test_010_add(self):
        print("running add")
        self.fridge.add("something", 2.7)
        self.assertEqual(self.fridge.contents["something"], 2.7)
        self.fridge.add("anything", 3)
        self.assertEqual(self.fridge.contents["anything"], 3)
        self.fridge.add("something", 4.2)
        self.assertEqual(self.fridge.contents["something"], 6.9)

    def test_020_remove(self):
        print("running remove")
        self.fridge.add("removable", 7)
        self.fridge.remove("removable", 3.5)
        self.assertEqual(self.fridge.contents["removable"], 3.5)
        self.fridge.remove("removable", 3.5)
        self.assertFalse("removable" in self.fridge.contents.keys())

    def test_015_check(self):
        print("running check")
        self.fridge.add("checkable", 1.5)
        self.assertTrue(self.fridge.check("checkable", 1.5))
        self.assertTrue(self.fridge.check("checkable", 1))
        self.assertFalse(self.fridge.check("nothing", 99))
        self.assertFalse(self.fridge.check("something", 99))


if __name__ == "__main__":
    unittest.main()
