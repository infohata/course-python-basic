# Iteratoriai ir Generatoriai

Iteratorius yra objektas, kuris palaiko iteraciją (kartojimą) per elementus arba reikšmes.

Iteratorius naudoja dviejų metodų rinkinį: `iter()` ir `next()`

Pavyzdys:

```Python
# Sukuriame sąrašą
my_list = [1, 2, 3, 4, 5]

# Sukuriame iteratoriaus objektą
my_iterator = iter(my_list)

# Iteruojame per iteratoriaus elementus su next() metodu
try:
    print(next(my_iterator)) # 1
    print(next(my_iterator)) # 2
    print(next(my_iterator)) # 3
    print(next(my_iterator)) # 4
    print(next(my_iterator)) # 5
    print(next(my_iterator)) # sukels StopIteration išimtį
except StopIteration:
    print("Baigta iteracija")
```

Šioje programoje mes sukūrėme sąrašą "my_list", o tada sukūrėme iteratoriaus objektą "my_iterator" naudojant `iter()` metodą. Tada mes iteruojame per iteratoriaus elementus su `next()` metodu, išvedame kiekvieną elementą ir naudojame try-except bloką, kad apdorotume `StopIteration` išimtį, kuri yra iškeliama, kai bandome iteruoti daugiau elementų, nei yra.

## Iteravimas su `for` ciklu

`for` ciklas automatiškai kviečia `iter()` metodą, kad gautų iteratoriaus objektą, ir tada kviečia `next()` metodą, kad gautų kiekvieną reikšmę iš iteratoriaus sekos.

Sukurkime sąrašą ir iteruokime per jį su for ciklu:

```Python
# Sukuriame sąrašą
mano_sarasas = [1, 2, 3, 4, 5]

# Iteruojame per sąrašą su for ciklu
for elementas in mano_sarasas:
    print(elementas)
```

```Python
# Sukuriame žodyną
mano_zodynas = {"A": 1, "B": 2, "C": 3}

# Iteruojame per žodyno raktus ir reikšmes su for ciklu
for raktas, reiksme in mano_zodynas.items():
    print(raktas, reiksme)
```

```Python
# Sukuriame tekstinę eilutę
eilute = "Labas, pasauli!"

# Iteruojame per eilutės simbolius su for ciklu
for simbolis in eilute:
    print(simbolis)
```

Kaip galite pastebėti, `for` ciklas yra patogus būdas iteruoti per iteratoriaus elementus, nes jis automatiškai kviečia `iter()` ir `next()` metodus.

## Iteravimas su `while` ciklu

`while` ciklas naudoja `next()` metodą, kad gautų kiekvieną reikšmę iš iteratoriaus sekos, ir tada apdoroja reikšmes, kol yra sukeliama `StopIteration` išimtis.

Sukurkime sąrašą ir iteruokime per jį su `while` ciklu:

```Python
# Sukuriame sąrašą
mano_sarasas = [1, 2, 3, 4, 5]

# Sukuriame iteratoriaus objektą
mano_iteratorius = iter(mano_sarasas)

# Iteruojame per iteratoriaus elementus su while ciklu
while True:
    try:
        elementas = next(mano_iteratorius)
        print(elementas)
    except StopIteration:
        break
```

Sukurkime žodyną ir iteruokime per jo raktus ir reikšmes su `while` ciklu:

```Python
# Sukuriame žodyną
mano_zodynas = {"A": 1, "B": 2, "C": 3}

# Sukuriame iteratoriaus objektą
mano_iteratorius = iter(mano_zodynas.items())

# Iteruojame per iteratoriaus elementus su while ciklu
while True:
    try:
        raktas, reiksme = next(mano_iteratorius)
        print(raktas, reiksme)
    except StopIteration:
        break
```

Sukurkime tekstinę eilutę ir iteruokime per jos simbolius su `while` ciklu:

```Python
# Sukuriame tekstinę eilutę
eilute = "Labas, pasauli!"

# Sukuriame iteratoriaus objektą
eilutes_iteratorius = iter(eilute)

# Iteruojame per iteratoriaus elementus su while ciklu
while True:
    try:
        simbolis = next(eilutes_iteratorius)
        print(simbolis)
    except StopIteration:
        break
```

## Generatoriai

Generatoriai yra specialūs Python objektai, kurie leidžia efektyviau atlikti iteracijas.

## Generatoriaus funkcija su `yield`

Generatoriaus funkcijos yra funkcijos, kurios naudoja `yield` sakinį vietoj `return`. `yield` leidžia funkcijai grąžinti vertę ir užšaldyti jos vykdymą, kol bus vėl iškviesta.

Pavyzdys:

```Python
def skaiciai_iki_n(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Sukuriamas generatorius, kuris generuoja skaičius nuo 0 iki 9
generatorius = skaiciai_iki_n(10)

for skaicius in generatorius:
    print(skaicius)
```

## Generatorius su `next()`

Pavyzdys:

```Python
def skaiciai_iki_n(n):
    i = 0
    while i < n:
        yield i
        i += 1

generatorius = skaiciai_iki_n(3)

print(next(generatorius))  # 0
print(next(generatorius))  # 1
print(next(generatorius))  # 2
print(next(generatorius))  # Sukels StopIteration klaidą
```

`next()` funkcija leidžia gauti sekantį elementą iš generatoriaus. Jei generatorius baigė generuoti visas vertes, `next()` išmes `StopIteration` klaidą.

## Generatoriaus deklaracija su `()`

Galite deklaruoti generatorių naudodami generatoriaus išraišką, kuri yra panaši į sąrašo išraišką (list comprehension), bet naudojate `()` vietoj `[]`.

Pavyzdys:

```Python
skaiciai = (x for x in range(10))

for skaicius in skaiciai:
    print(skaicius)
```

## Užduotys

### Pirma užduotis

Sukurkite iteratorių, kuris iteruoja per pateiktą sąrašą ir atspausdina visus lyginius skaičius.

### Antra užduotis

Iteruokite per žodyną, kurio raktai yra raidės, o reikšmės yra skaičiai, ir atspausdinkite tik tas raides, kurių reikšmės yra didesnės nei 4.

### Trečia užduotis

Parašykite programą, kuri naudoja generatorių, generuojantį kiekvieno žodžio ilgį iš teksto.

### Ketvirta užduotis

Sukurkite generatorių, kuris generuoja visus pirminius skaičius iki nurodyto skaičiaus n.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for skaicius in sararas:
    if skaicius % 2 == 0:
        print(skaicius)
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
zodynas = {"A": 3, "B": 5, "C": 1, "D": 6, "E": 4}

for raide, skaicius in zodynas.items():
    if skaicius > 4:
        print(raide)
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
tekstas = "Labas pasauli čia yra pavyzdinis tekstas"
zodziu_ilgiai = (len(zodis) for zodis in tekstas.split())

for ilgis in zodziu_ilgiai:
    print(ilgis)
```

</details>
<details>
<summary>Ketvirta užduotis</summary>
<hr>

```Python
def ar_pirminis(skaicius):
    if skaicius < 2:
        return False
    for i in range(2, skaicius):
        if skaicius % i == 0:
            return False
    return True

def pirminiai_iki_n(n):
    for skaicius in range(2, n + 1):
        if ar_pirminis(skaicius):
            yield skaicius

pirminiai_generatorius = pirminiai_iki_n(30)

for skaicius in pirminiai_generatorius:
    print(skaicius)
```

</details>
</details>