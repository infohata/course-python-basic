# Sąrašų pagalbinės funkcjios, Sąrašo apibrėžimas

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

💡 _`map()` ir `filter()` taip pat yra pagalbinės fukcijos, jas  prisiminti galite [čia](https://github.com/eglemot/course-python-basic/blob/3bcc9234f71c0782e83dec76239de7490b3986ab/04_funkcijos/06_anonimines_funkcijos.md)_

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

rusiuoti_studentai = sorted(studentai, key=lambda x: x.vidurkis(), reverse=True)
for studentas in rusiuoti_studentai:
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

---

# Sąrašo apibrėžimas (List comprehension)

List comprehension yra trumpas būdas kurti sąrašus naudojant `for` ciklą ir galimą sąlygą.

## Sąrašo kėlimas laipsniu

```Python
skaiciai = [1, 2, 3, 4, 5]
laipsniai = 3
pakelta_skaiciai = [x ** laipsniai for x in skaiciai]
print(pakelta_skaiciai)  # Rezultatas: [1, 8, 27, 64, 125]
```

## Sąrašo filtravimas pagal loginę sąlygą

```Python
skaiciai = [1, 2, 3, 4, 5]
salyga = lambda x: x % 2 == 0
filtruoti_skaiciai = [x for x in skaiciai if salyga(x)]
print(filtruoti_skaiciai)  # Rezultatas: [2, 4]
```

## Sąrašo apibrėžimas pritaikant lambda funkciją

```Python
skaiciai = [1, 2, 3, 4, 5]
dvigubas_skaiciai = [(lambda x: x * 2)(x) for x in skaiciai]
print(dvigubas_skaiciai)  # Rezultatas: [2, 4, 6, 8, 10]
```

## Sąrašo apibrėžimo pakeitimas generatoriaus apibrėžimu

```Python
skaiciai = [1, 2, 3, 4, 5]
laipsniai = 3
pakelta_skaiciai_gen = (x ** laipsniai for x in skaiciai)

for pakeltas in pakelta_skaiciai_gen:
    print(pakeltas)

# Rezultatas:
# 1
# 8
# 27
# 64
# 125
```

## Užduotys

### Pirma užduotis

Sukurkite programą, kuri naudoja `lambda`, `map()` ir `filter()` funkcijas, kad atrinktų sąrašo elementus, didesnius už 10, ir padidintų juos dvigubai. Palyginkite šį rezultatą su tuo, ką gautumėte naudodami "list comprehension".

### Antra užduotis

Parašykite programą, kuri naudoja `reduce()` funkciją, kad rastų sąrašo elementų sandaugą.

### Trečia užduotis

Naudodamiesi `statistics` moduliu, apskaičiuokite ir išveskite sąrašo elementų sumą, vidurkį, medianą, mažiausią ir didžiausią elementą.

### Ketvirta užduotis

Sukurkite programą, kuri naudoja `sort()` arba `sorted()` funkcijas, kad rūšiuotų sąrašą skaičių pagal jų liekanas dalinant iš 3 (atsižvelgiant į key parametrą).

### Penkta užduotis

Sukurkite programą, kuri naudoja `lambda`, `filter()` ir `reduce()` funkcijas, kad apskaičiuotų vidurkį tų sąrašo skaičių, kurie yra lyginiai. Palyginkite šį rezultatą su tuo, ką gautumėte naudodami "list comprehension".

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
sarasas = [5, 12, 7, 18, 4, 15]

# Atrinkti ir padidinti dvigubai skaičius, didesnius už 10
result = map(lambda x: x * 2, filter(lambda x: x > 10, sarasas))
print(list(result))  # [24, 36, 30]

# Su paprastomis funkcijomis ir `for` ciklais
result = [x * 2 for x in sarasas if x > 10]
print(result)  # [24, 36, 30]

```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
from functools import reduce

sarasas = [1, 2, 3, 4, 5]

# Rasti sandaugą
sandauga = reduce(lambda x, y: x * y, sarasas)
print(sandauga)  # 120
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
import statistics

sarasas = [1, 2, 3, 4, 5]

print(sum(sarasas))  # 15
print(statistics.mean(sarasas))  # 3.0
print(statistics.median(sarasas))  # 3
print(min(sarasas))  # 1
print(max(sarasas))  # 5
```

</details>
<details>
<summary>Ketvirta užduotis</summary>
<hr>

```Python
sarasas = [3, 1, 4, 1, 5, 9, 2]

result = sorted(sarasas, key=lambda x: x % 3)
print(result)  # [3, 9, 1, 4, 1, 5, 2]
```

</details>
<details>
<summary>Penkta užduotis</summary>
<hr>

```Python
from functools import reduce

sarasas = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, sarasas)) / len(list(filter(lambda x: x % 2 == 0, sarasas)))
print(result)  # 3.0

# Su paprastomis funkcijomis ir `for` ciklais
result = sum(x for x in sarasas if x % 2 == 0) / len([x for x in sarasas if x % 2 == 0])
print(result)  # 3.0
```

</details>
</details>
