# Iteratoriai

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

## Iteratoriaus funkcija

Iteratoriaus funkcija gali būti naudinga, jei norite padaryti savo kodą daugkartinio naudojimo arba perpanaudojimo. Jūs galite naudoti iteratoriaus funkciją, kad sukurtumėte naują iteratoriaus objektą su reikiamomis savybėmis.

Sukurkime iteratoriaus funkciją, kuri gražina iteratoriaus objektą, kuris iteruoja per intervalą nuo 0 iki n:

```Python
def mano_iteratoriaus_funkcija(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Sukuriame iteratoriaus objektą su mano_iteratoriaus_funkcija funkcija
mano_iteratorius = mano_iteratoriaus_funkcija(5)

# Iteruojame per iteratoriaus elementus su for ciklu
for elementas in mano_iteratorius:
    print(elementas)
```

Ši programa naudoja "mano_iteratoriaus_funkcija" funkciją, kad sukurtų iteratoriaus objektą, kuris iteruoja per intervalą nuo 0 iki n. Mes naudojame `yield` raktažodį(naudojamas funkcijose kaip alternatyva `return`), kad galėtume grąžinti reikšmę. Tada mes iteruojame per iteratoriaus elementus su `for` ciklu ir išvedame kiekvieną elementą.

Sukurkime iteratoriaus funkciją, kuri gražina iteratoriaus objektą, kuris iteruoja per tekstinę eilutę požodžiui:

```Python
def mano_iteratoriaus_funkcija(eilute):
    zodziai = eilute.split()
    for zodis in zodziai:
        yield zodis

# Sukuriame iteratoriaus objektą su mano_iteratoriaus_funkcija funkcija
mano_iteratorius = mano_iteratoriaus_funkcija("Labas, pasauli!")

# Iteruojame per iteratoriaus elementus su for ciklu
for zodis in mano_iteratorius:
    print(zodis)
```

Ši programa naudoja "mano_iteratoriaus_funkcija" funkciją, kad sukurtų iteratoriaus objektą, kuris iteruoja per tekstinę eilutę požodžiui. Mes naudojame `split()` metodą, kad padalintume eilutę į žodžius ir tada iteruojame per kiekvieną žodį su `yield` raktažodžiu, kad grąžintume reikšmę. Tada mes iteruojame per iteratoriaus elementus su `for` ciklu ir išvedame kiekvieną žodį.
