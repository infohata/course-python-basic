# `tuple`

`tuple` yra nekeičiamas ir tvarkingas Python duomenų tipas, kuris gali saugoti bet kokio tipo elementus. Jis panašus į 
sąrašą, tačiau yra nekeičiamas - tai reiškia, kad kai kartą sukuriamas, jo elementai negali būti pakeisti ar pašalinti.


<br>

## `tuple` kūrimas

`tuple` sukūrimas yra labai panašus į sąrašo sukūrimą, tik naudojama skliaustelių pora `()` vietoj laužtinių skliaustų `[]`:

```Python
tuscias_tuple = ()
print(tuscias_tuple) # ()
```

```Python
vieno_elemento_tuple = (1,)
print(vieno_elemento_tuple) # (1,)
print(type(vieno_elemento_tuple)) # <class 'tuple'>
```

```Python
skaiciu_tuple = (1, 2, 3, 4, 5)
print(skaiciu_tuple) # (1, 2, 3, 4, 5)
```

```Python
misrus_tuple = (1, 'du', 3.0, [4, 5], True)
print(misrus_tuple) # (1, 'du', 3.0, [4, 5], True)
```

<br>

## `tuple` sujungimas

Norint sujungti du ar daugiau `tuple`, galima naudoti `+` operatorių. Šis operatorius sujungia `tuple` reikšmes ir grąžina naują `tuple` su visais elementais. Pvz.:

```Python
pirmas_tuple = (1, 2, 3)
antras_tuple = ('a', 'b', 'c')
trecias_tuple = (True, False)

naujas_tuple = pirmas_tuple + antras_tuple + trecias_tuple

print(naujas_tuple)
```

<br>

## Kaip pasiekti `tuple` elementus

Tuple elementai yra pasiekiami naudojant indeksus, taip pat kaip ir sąrašuose. Indeksai prasideda nuo nulio, o paskutinis elementas yra pasiekiamas naudojant indeksą -1:

```Python
misrus_tuple = (1, 'du', 3.0, [4, 5], True)

print(misrus_tuple[0]) # 1
print(misrus_tuple[3]) # [4, 5]
print(misrus_tuple[-1]) # True
```

Šis kodas atspausdins:

```
(1, 2, 3, 'a', 'b', 'c', True, False)
```

<br>

## `tuple` dalijimas

`tuple` galite dalinti (`slicing`) naudodami tuos pačius metodus, kaip ir su sąrašais. Galite nurodyti pradžios ir pabaigos indeksus, taip pat žingsnio dydį, kad gautumėte tik norimą dalį `tuples`. Pvz.:

```Python
raidziu_tuple = ('a', 'b', 'c', 'd', 'e', 'f')
print(raidziu_tuple[2:4])  # ('c', 'd')
print(raidziu_tuple[0:3:2])  # ('a', 'c')
print(raidziu_tuple[:4])  # ('a', 'b', 'c', 'd')
print(raidziu_tuple[2::2])  # ('c', 'e')
print(raidziu_tuple[::-1])  # ('f', 'e', 'd', 'c', 'b', 'a')
```

<br>

## `tuple` metodai

`tuple` yra nekeičiamas objektas, todėl jame nėra daug metodų kaip, pavyzdžiui, sąraše. Tačiau yra keletas naudingų metodų.

`count(x)` - grąžina, kiek kartų nurodytas elementas pasikartoja `tuple`.

```Python
raidziu_tuple = ('a', 'b', 'c', 'a', 'd')

print(raidziu_tuple.count('a'))  # 2
```

`index(x)` - grąžina indeksą pirmajam nurodyto elemento atvejui `tuple`.

```Python
raidziu_tuple = ('a', 'b', 'c', 'a', 'd')

print(raidziu_tuple.index('a'))  # 0
```

<br>

## Patikrinti ar elementas yra `tuple`

Galite patikrinti, ar `tuple` turi elementą naudodami `in` operatorių. Šis operatorius grąžins `True`, jei elemento reikšmė yra `tuple`, ir `False`, jei elemento reikšmės nėra `tuple`. Pvz.:

```Python
raidziu_tuple = ('a', 'b', 'c', 'a', 'd')

print('a' in raidziu_tuple)  # True
print('e' in raidziu_tuple)  # False
```

<br>

## Iteravimas

`tuple` yra iteruojamas objektas, tai reiškia, kad jo elementus galite pereiti vieną po kito naudodami `for` ciklą arba `while` ciklą.

`for` ciklo pvz:

```Python
raidziu_tuple = ('a', 'b', 'c', 'a', 'd')

for raide in raidziu_tuple:
    print(raide)
```

Šis kodas atspausdins:

```
a
b
c
a
d
```

`while` ciklo pvz:

```Python
raidziu_tuple = ('a', 'b', 'c', 'a', 'd')

i = 0
while i < len(raidziu_tuple):
    print(raidziu_tuple[i])
    i += 1
```

Šis kodas atspausdins:

```
a
b
c
a
d
```

Kaip matote, `while` cikle naudojame `len()` funkciją, kad sužinotume, kiek `tuple` turi elementų. Tada, naudodami kintamąjį `i`, per kiekvieną iteraciją gautume reikšmę, kurią spausdintume, ir padidintume `i` reikšmę vienetu, kad galėtume per eiti per kitą `tuple` elementą.

<br>

# Užduotys