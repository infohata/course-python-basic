# Standartinių bibliotekų importavimas

## `import this` - "The Zen of Python" (Python'o dvasia)

"The Zen of Python" yra Python programavimo kalbos filosofijos poema, kurią parašė Tim Peters. Štai kaip ją galite pamatyti:

```Python
import this
```

Šios eilutės pagrindiniai principai yra:

Aiškumas yra geriau už paslėptį.
Paprastumas yra geriau už sudėtingumą.
Dvigubai geriau yra geriau už gerai pakankamai.
Praktiškumas nugalės teoriją.

## `import random` - atsitiktinių skaičių generatoriaus funkcijos

Python'o random biblioteka leidžia generuoti atsitiktinius skaičius, atsitiktinai pasirinkti elementus iš sąrašo ir pan. Štai keletas pavyzdžių:

```Python
import random

# Sugeneruoti atsitiktinį skaičių tarp 0 ir 1
print(random.random())

# Sugeneruoti atsitiktinį sveikąjį skaičių tarp 1 ir 10
print(random.randint(1, 10))

# Atsitiktinai pasirinkti elementą iš sąrašo
my_list = ["a", "b", "c", "d", "e"]
print(random.choice(my_list))
```

## `import math` - papildomos matematinės funkcijos

Python'o math biblioteka suteikia prieigą prie papildomų matematinių funkcijų ir konstantų, tokių kaip π (pi) ir e. Štai keletas pavyzdžių:

```Python
import math

# Apskaičiuoti sinuso reikšmę
print(math.sin(math.pi / 2))

# Apskaičiuoti faktorialą
print(math.factorial(5))

# Apskaičiuoti kvadratą
print(math.sqrt(9))
```

## `import calendar` - kalendoriaus funkcijos

Python'o calendar biblioteka leidžia dirbti su kalendoriais, pavyzdžiui, sužinoti, ar metai yra keliamieji arba kokia savaitės diena yra tam tikra data. Štai keletas pavyzdžių:

```Python
import calendar

# Tikrinti, ar metai yra keliamieji
print(calendar.isleap(2020))

# Gaukite savaitės dienos pavadinimą pagal skaičių
print(calendar.day_name[1]) # 'Tuesday'

# Gaukite mėnesio dienų skaičių
print(calendar.monthrange(2023, 4)) # (5, 30) - pirmoji balandžio diena yra šeštadienis (5), o balandžio mėnesyje yra 30 dienų

# Atspausdinti mėnesio kalendorių
print(calendar.month(2023, 4))
```

`calendar` biblioteka turi daugiau funkcijų ir savybių, kurios padės jums dirbti su datomis ir laiku. Šie pavyzdžiai yra tik pradžia. Galite rasti daugiau informacijos apie `calendar` biblioteką [Python dokumentacijoje.](https://docs.python.org/3/library/calendar.html)

## Užduotys

### Pirma užduotis

Parašykite funkciją, kuris atspausdina 10 atsitiktinių skaičių nuo 1 iki 100 ir juos išrikiuoja didėjimo tvarka.

### Antra užduotis

Sukurkite kauliukų žaidimą, kuris:

- Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
- Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
- Kitu atveju atspausdinti „Laimėjai!“
- Patarimas: Naudoti while ciklą

### Trečia užduotis

Parašykite Python funkciją, kuri priima metus ir mėnesį, o tada atspausdina šio mėnesio kalendorių bei parodo, kiek savaitgalio dienų (šeštadienių ir sekmadienių) yra tame mėnesyje.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
  <summary>Pirma užduotis</summary>
  <hr>
  
matematika.py

```Python
import random

def rusiuoti_atsitiktinius_skaicius():
    atsitiktiniai_skaiciai = [random.randint(1, 100) for _ in range(10)]
    rikiuoti_skaiciai = sorted(atsitiktiniai_skaiciai)
    print(rikiuoti_skaiciai)

rusiuoti_atsitiktinius_skaicius()
```

</details>
<details>
  <summary>Antra užduotis</summary>
  <hr>

```Python
import random

print('Bus sugeneruoti 3 skaičiai')
print('Jei vienas iš jų – 5, tu pralaimėjai!')

for skaicius in range(3):
    skaiciai = random.randint(1, 6)
    print(skaiciai)
    if skaicius == 5:
        print('Pralaimėjai...')
        break
else:
    print('Laimėjai!')
```

</details>
<details>
  <summary>Trečia užduotis</summary>
  <hr>

```Python
import calendar

def spausdinti_menesio_kalendoriu_suskaiciuojant_savaitgalius(metai, menesis):
    print(calendar.month(metai, menesis))

    _, menesio_ilgis = calendar.monthrange(metai, menesis)

    savaitgalio_dienos = 0
    for diena in range(1, menesio_ilgis + 1):
        savaites_diena = calendar.weekday(metai, menesis, diena)
        if savaites_diena == 5 or savaites_diena == 6:
            savaitgalio_dienos += 1

    print(f"Savaitgalio dienų skaičius šiame mėnesyje: {savaitgalio_dienos}")

# Pavyzdys su 2023-ųjų balandžio mėnesiu
spausdinti_menesio_kalendoriu_suskaiciuojant_savaitgalius(2023, 4)
```

</details>
</details>
