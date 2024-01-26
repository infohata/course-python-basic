# Testavimas, testų kūrimo praktikos

## Testavimo teorija

Testavimas - tai procesas, per kurį patikrinama, ar programinės įrangos sistema atitinka reikalavimus ir veikia be klaidų. Yra du pagrindiniai testavimo būdai: rankinis ir automatizuotas.

## Rankinis testavimas

Rankinis testavimas - tai testavimo metodas, kai testuotojas atlieka testus be specializuotų įrankių pagalbos. Rankinis testavimas gali būti naudingas pradiniam programinės įrangos veikimo įvertinimui, tačiau jis yra laiko sąnašas ir gali lemti žmogiškąją klaidą.

## Automatizuotas testavimas

Automatizuotas testavimas - tai testavimo metodas, kai testai atliekami naudojant specializuotas programas ir skriptus. Python kalboje yra keletas bibliotekų, skirtų automatizuotam testavimui, pavyzdžiui, unittest, pytest ir kt.

## Biblioteka unittest

Unittest - tai standartinė Python biblioteka, skirta automatizuotam testavimui. Joje yra įvairūs metodai, padedantys rašyti testus ir patikrinti rezultatus.

## Assert metodai

Assert metodai yra unittest bibliotekos metodai, padedantys patikrinti ar rezultatas atitinka tikėtąjį.

Pavyzdys:

```Python
import unittest

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

if __name__ == '__main__':
    unittest.main()

```

Čia pateikti pavyzdžiai demonstruoja, kaip naudoti įvairius assert metodus unittest bibliotekoje:

`test_assertEqual`: patikrina, ar 3 + 2 yra lygu 5.
`test_assertTrue`: patikrina, ar sąlyga 3 < 5 yra teisinga (True).
`test_assertFalse`: patikrina, ar sąlyga 5 < 3 yra neteisinga (False).
`test_assertIs`: patikrina, ar kintamieji 'a' ir 'b' yra tas pats objektas.
`test_assertIsNone`: patikrina, ar funkcija grąžina None reikšmę.

## Testo paleidimas komandinėje eilutėje

Testą galite paleisti komandinėje eilutėje naudodami šią komandą:

```Python
python -m unittest test_example.py
```

## Testo paleidimas su `unittest.main()`

Testą taip pat galite paleisti naudodami `unittest.main()` funkciją:

```Python
if __name__ == '__main__':
    unittest.main()
```

## False positive pavyzdys

False positive - tai klaidingas teigiamas rezultatas, kai testas praeina, bet turėtų nepavykti.

Pavyzdys su nesuderinamu palyginimu:

```Python
import unittest

def divide(x, y):
    return x / y

class TestDivideFunction(unittest.TestCase):
    def test_integer_division(self):
        self.assertEqual(divide(10, 2), 10 // 2)  # False positive: 5.0 == 5

if __name__ == '__main__':
    unittest.main()
```

Šiame pavyzdyje turime false positive situaciją, nes naudojame nesuderinamas operacijas (/ ir //). Testas praeina, nes Python automatiškai paverčia 5.0 į 5 palyginimo metu. Tačiau iš tikrųjų turėtume naudoti `assertAlmostEqual`, kad patikrintume, ar rezultatai yra pakankamai artimi, o ne tiesiog lygūs.

Pavyzdys su klaidinga logika:

```Python
import unittest

def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True # Klaidinga logika nes range(2, 2) negražina nieko. Tada kodas tiesiog praleidžia 2 kaip pirminį.

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
```

Šiame pavyzdyje testas test_prime praeina dėl klaidingos logikos is_prime funkcijoje. Nors ši funkcija teisingai nustato, ar skaičius nėra pirminis, ji nepatikrina, ar skaičius yra 2. Dėl šios klaidingos logikos testas praeina, nors turėtų nepavykti.

Norint išvengti false positive, svarbu užtikrinti, kad testai būtų kruopščiai suprojektuoti ir tikrintų visus galimus scenarijus, o funkcijos būtų korektiškai įgyvendintos.

## Objektų klasių testavimas, `setUp()` metodas

`setUp()` metodas yra unittest bibliotekos metodas, kuris leidžia jums nustatyti pradines reikšmes prieš kiekvieną testą.

Pavyzdys:

```Python
import unittest

class MyClass:
    def __init__(self, x):
        self.x = x

    def add(self, y):
        return self.x + y

class TestMyClass(unittest.TestCase):
    def setUp(self): 
        self.obj = MyClass(5)

    def test_add(self):
        self.assertEqual(self.obj.add(3), 8)

if __name__ == '__main__':
    unittest.main()
```

Sukuriame testavimo klasę TestMyClass, kuri paveldi iš unittest.TestCase. TestMyClass klasėje aprašome `setUp()` metodą. Prieš kiekvieną testą sukuriamas naujas MyClass objektas su x reikšme lygia 5. test_add testas patikrina, ar add metodas veikia teisingai. Testas naudoja `assertEqual()` funkciją, kad patikrintų, ar self.obj.add(3) grąžina 8, kaip tikimasi.

## TDD (Test Driven Development) metodologija

Test Driven Development (TDD) yra programavimo metodologija, kurioje pirmiausia parašomi testai, o tik po to - pati funkcionalumo realizuojanti programinė įranga. Tai padeda iš anksto apibrėžti, koks turėtų būti funkcionalumas, ir užtikrinti, kad programinė įranga veiks pagal prieš tai nustatytus reikalavimus.

### TDD proceso etapai

- Parašyti testą, kuris dar nepavyksta.
- Parašyti minimalų kodą, kad testas praeitų.
- Refaktorizuoti kodą, kad jis atitiktų gerąją programavimo praktiką.
- Pakartoti 1-3 etapus, kol visi reikalavimai bus įgyvendinti.

Tarkime, kad turime šią TDD užduotį: Sukurti kalkuliatorių, kuris gali atlikti sudėties operaciją.

- Parašome testą, kuris dar nepavyksta

```Python
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)
```

Testas test_add tikrina, ar Calculator klasės add metodas teisingai atlieka sudėtį. Tikimasi, kad suma 3 ir 5 bus lygi 8.

- Parašome minimalų kodą, kad testas veiktų

```Python
class Calculator:
    def add(self, x, y):
        pass
```

Šiuo metu add metodas yra tuščias (naudoja pass komandą). Tai reiškia, kad jis nieko nedaro ir nieko negrąžina. Dėl šios priežasties test_add testas nepavyks, nes self.calc.add(3, 5) grąžins None, o ne 8.

- Parašome minimalų kodą, kad testas praeitų

```Python
class Calculator:
    def add(self, x, y):
        return x + y
```

Šiame etape add metodas buvo pakeistas, kad grąžintų x ir y sumą. Dabar test_add testas turėtų pavykti, nes self.calc.add(3, 5) grąžins 8, kaip tikimasi.

- Refaktorizuoti kodą, kad jis atitiktų gerąją programavimo praktiką

Šiuo atveju kodo refaktorizavimas nėra būtinas, nes klasė Calculator ir jos metodas add yra pakankamai paprasti ir aiškūs.

- Pakartoti 1-3 etapus, kol visi reikalavimai bus įgyvendinti.

Šiame pavyzdyje reikalavimas buvo įgyvendinti sudėties funkcija. Jei būtų papildomų reikalavimų (pvz., atimties, daugybos ir dalybos funkcijos), turėtumėte pakartoti TDD proceso etapus kiekvienam iš jų.

TDD procesas padeda užtikrinti, kad funkcijos veikia teisingai ir, kad jūsų kodas yra tvarkingas bei lengvai suprantamas. Be to, jis padeda išvengti galimų klaidų ir palengvina programos priežiūrą.

## Užduotys

TDD principu parašykite programą "paskolos kalkuliatorius".

- sukurkite testą paskolos kalkuliatoriaus programai, kur paskolos objektui galima nustatyti paskolos dydį, metines palūkanas ir terminą. Testavimo scenarijus turi patikrinti kelis teisingus paskolos palūkanų, pabrangimo, mokėjimo grafiko scenarijus.

- sukurkite programą, kuri veikia su aukščiau įgyvendintu testu.
