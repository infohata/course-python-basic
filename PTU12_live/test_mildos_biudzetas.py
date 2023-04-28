import unittest
from mildos_biudzetas import Biudzetas, Pajamos, Islaidos


class TestBiudzetas(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Biudzetas()
        self.obj.ivesti_pajamas(Pajamos(200, "Testas", "Testuotojas"))
        self.obj.ivesti_pajamas(Islaidos(100, "Siuntimo Testas", "Testinis Gavejas"))

    def test_ivesti_pajamas(self):
        self.assertEqual(self.obj.zurnalas[0].suma, 200)
        self.assertEqual(self.obj.zurnalas[0].komentaras, "Testas")
        self.assertEqual(self.obj.zurnalas[0].siuntejas, "Testuotojas")

    def test_ivesti_islaidas(self):
        self.assertEqual(self.obj.zurnalas[1].suma, 100)
        self.assertEqual(self.obj.zurnalas[1].komentaras, "Siuntimo Testas")
        self.assertEqual(self.obj.zurnalas[1].gavejas, "Testinis Gavejas")

    def test_balansas(self):
        self.assertEqual(self.obj.balansas(), 100)


if __name__ == "__main__":
    unittest.main()
