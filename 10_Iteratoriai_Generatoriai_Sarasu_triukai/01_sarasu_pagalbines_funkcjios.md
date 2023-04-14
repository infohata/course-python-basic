# Sąrašų pagalbinės funkcjios

## `lambda`

Tai specialus žodis Python programavimo kalboje, leidžiantis greitai ir paprastai sukurti anonimines funkcijas. Anoniminės funkcijos yra tokios, kurios neturi vardo ir dažniausiai naudojamos tik kartą kode.

## `map()`

Tai funkcija, kuri taiko nurodytą funkciją kiekvienam sąrašo elementui.

Pavyzdys:

```Python
sarasas = [1, 2, 3, 4, 5]
rezultatas = map(lambda x: x ** 2, sarasas)
print(list(rezultatas))  # [1, 4, 9, 16, 25]

def kvadratas(x):
    return x ** 2

rezultatas = map(kvadratas, sarasas)
print(list(rezultatas))  # [1, 4, 9, 16, 25]
```

Pavyzdys, kai naudojami keli kintamieji:

```Python
sarasas1 = [1, 2, 3, 4, 5]
sarasas2 = [5, 4, 3, 2, 1]
rezultatas = map(lambda x, y: x + y, sarasas1, sarasas2)
print(list(rezultatas))  # [6, 6, 6, 6, 6]

def sudetis(x, y):
    return x + y

rezultatas = map(sudetis, sarasas1, sarasas2)
print(list(rezultatas))  # [6, 6, 6, 6, 6]
```

## `filter()`

Funkcija, leidžianti atrinkti sąrašo elementus pagal nurodytą sąlygą.

Pavyzdys:

```Python
sarasas = [1, 2, 3, 4, 5]
rezultatas = filter(lambda x: x % 2 == 0, sarasas)
print(list(rezultatas))  # [2, 4]
```

## `reduce()`

Ši funkcija yra iš `functools` modulio, ir ji leidžia sukaupti sąrašo elementus, taikant nurodytą funkciją. Kitaip tariant, `reduce()` pereina per sąrašą, naudodamas funkciją, kuri priima du argumentus, paeiliui pritaikydama funkciją elementams ir kaupiant rezultatą.

Pavyzdys:

```Python
from functools import reduce
import operator

sarasas = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, sarasas)
print(suma)  # 15
```

Pavyzdys:

```Python
from functools import reduce

sarasas = [1, 2, 3, 4, 5]
maksimalus = reduce(lambda x, y: x if x > y else y, sarasas)
print(maksimalus)  # 5
```

## Statistinės funkcijos

- `sum()`: funkcija, grąžinanti sąrašo elementų sumą.
- `max()`: funkcija, grąžinanti didžiausią sąrašo elementą.
- `min()`: funkcija, grąžinanti mažiausią sąrašo elementą.
- `mean()`: funkcija, grąžinanti vidurkį. Galite ją gauti su `statistics.mean()`.
- `median()`: funkcija, grąžinanti medianą. Galite ją gauti su `statistics.median()`.

```Python
import statistics

sarasas = [1, 2, 3, 4, 5]
print(sum(sarasas))  # 15
print(max(sarasas))  # 5
print(min(sarasas))  # 1
print(statistics.mean(sarasas))  # 3.0
print(statistics.median(sarasas))  # 3
```

## `sort()`

Tai yra sąrašo metodas, kuris išrūšiuoja sąrašo elementus. `sort()` priima kelis pasirinktinius parametrus, tokius kaip `key` ir `reverse`.

Pavyzdys:

```Python
sarasas = [3, 1, 4, 1, 5, 9, 2]
sarasas.sort()
print(sarasas)  # [1, 1, 2, 3, 4, 5, 9]
```

Jei norite rūšiuoti sąrašą atvirkščia tvarka, galite nurodyti `reverse=True`:

```Python
sarasas = [3, 1, 4, 1, 5, 9, 2]
sarasas.sort(reverse=True)
print(sarasas)  # [9, 5, 4, 3, 2, 1, 1]
```

Galite naudoti `key` parametrą, kad nurodytumėte, pagal ką rūšiuoti sąrašą:

```Python
eilutes_sarasas = ["vienas", "du", "trys", "keturi", "penki"]
eilutes_sarasas.sort(key=len)
print(eilutes_sarasas)  # ['du', 'trys', 'vienas', 'keturi', 'penki']
```

## `sorted()`

Tai yra Python įterpimo funkcija, kuri rūšiuoja sąrašą ir grąžina naują, rūšiuotą sąrašą, nepakeisdama pradinio. `sorted()` taip pat priima pasirinktinius parametrus, tokius kaip `key` ir `reverse`.

Pavyzdys:

```Python
sarasas = [3, 1, 4, 1, 5, 9, 2]
rūšiuotas_sarasas = sorted(sarasas)
print(rūšiuotas_sarasas)  # [1, 1, 2, 3, 4, 5, 9]
```

## Objektų rūšiavimas sąraše

Tarkime, turime Studentas klasę, kuri turi vardą, pavardę ir pažymių sąrašą. Norime rūšiuoti Studentas objektų sąrašą pagal jų vidurkius:

```Python
class Studentas:
    def __init__(self, vardas, pavarde, pazymiai):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pazymiai = pazymiai

    def vidurkis(self):
        return sum(self.pazymiai) / len(self.pazymiai)

studentai = [
    Studentas("Jonas", "Jonaitis", [8, 9, 7]),
    Studentas("Petras", "Petraitis", [10, 9, 10]),
    Studentas("Ona", "Onaitė", [6, 8, 7]),
]

rūšiuoti_studentai = sorted(studentai, key=lambda x: x.vidurkis(), reverse=True)
for studentas in rūšiuoti_studentai:
    print(f"{studentas.vardas} {studentas.pavarde} - {studentas.vidurkis()}")
```

Šioje programoje, `sorted()` funkcija su key parametru `x.vidurkis()` nurodo, kad sąrašas studentai turi būti rūšiuojamas pagal Studentas objektų vidurkius, o `reverse=True` parametras nurodo, kad rūšiavimas turėtų būti atvirkštinis.

## `attrgetter()`

Tai yra funkcija iš `operator` modulio, kuri leidžia sukurti `key` funkciją pagal objekto atributus.

Pavyzdys:

```Python
from operator import attrgetter

class Studentas:
    def __init__(self, vardas, pavarde, pazymiai):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pazymiai = pazymiai

    def vidurkis(self):
        return sum(self.pazymiai) / len(self.pazymiai)

studentai = [
    Studentas("Jonas", "Jonaitis", [8, 9, 7]),
    Studentas("Petras", "Petraitis", [10, 9, 10]),
    Studentas("Ona", "Onaitė", [6, 8, 7]),
]

rūšiuoti_studentai = sorted(studentai, key=attrgetter("vardas"))
for studentas in rūšiuoti_studentai:
    print(f"{studentas.vardas} {studentas.pavarde}")
```

`attrgetter()` funkcija nusako, kad rūšiuojame objektus pagal "vardas" atributą.

Jei norite rūšiuoti pagal kelis atributus, galite pateikti kelių atributų pavadinimus kaip argumentus `attrgetter()` funkcijai:

```Python
rūšiuoti_studentai = sorted(studentai, key=attrgetter("pavarde", "vardas"))
for studentas in rūšiuoti_studentai:
    print(f"{studentas.pavarde} {studentas.vardas}")
```

`attrgetter()` funkcija rūšiuos studentus pagal pavardę, o tada pagal vardą, kadangi `key` funkcija rūšiuoja elementus nuo kairės į dešinę.
