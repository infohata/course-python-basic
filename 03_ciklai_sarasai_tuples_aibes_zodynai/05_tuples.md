# `tuple`

`tuple` yra nekeičiamas ir tvarkingas Python duomenų tipas, panašus į sąrašą, kuris gali saugoti bet kokio tipo elementus. Tai reiškia, kad po sukūrimo, tuplės elementai negali būti pakeisti ar pašalinti.

## `tuple` kūrimas

`tuple` sukūrimas yra labai panašus į sąrašo sukūrimą, tik naudojama skliaustelių pora `()` vietoj laužtinių skliaustų `[]`:

```Python
vieno_elemento_tuple = (1,)
print(vieno_elemento_tuple) # (1,)
print(type(vieno_elemento_tuple)) # <class 'tuple'>
```

❗Pastaba: tuščia tuplė neturi prasmės, todėl tuščios tuplės aprašyti neina.

```Python
skaiciu_tuple = (1, 2, 3, 4, 5)
print(skaiciu_tuple) # (1, 2, 3, 4, 5)
```

```Python
misri_tuple = (1, 'du', 3.0, [4, 5], True)
print(misri_tuple) # (1, 'du', 3.0, [4, 5], True)
```

## `tuple` sujungimas

Norint sujungti du ar daugiau `tuple`, galima naudoti `+` operatorių. Šis operatorius sujungia `tuple` reikšmes ir grąžina naują `tuple` su visais elementais. Pvz.:

```Python
pirmas_tuple = (1, 2, 3)
antras_tuple = ('a', 'b', 'c')
trecias_tuple = (True, False)

naujas_tuple = pirmas_tuple + antras_tuple + trecias_tuple

print(naujas_tuple)
```

Rezultatas:

```Text
(1, 2, 3, 'a', 'b', 'c', True, False)
```

## Kaip pasiekti `tuple` elementus

Tuple elementai yra pasiekiami naudojant indeksus, taip pat kaip ir sąrašuose. Indeksai prasideda nuo nulio, o paskutinis elementas yra pasiekiamas naudojant indeksą -1:

```Python
misrus_tuple = (1, 'du', 3.0, [4, 5], True)

print(misrus_tuple[0]) # 1
print(misrus_tuple[3]) # [4, 5]
print(misrus_tuple[-1]) # True
```

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

## Patikrinti ar elementas yra `tuple`

Galite patikrinti, ar `tuple` turi elementą naudodami `in` operatorių. Šis operatorius grąžins `True`, jei elemento reikšmė yra `tuple`, ir `False`, jei elemento reikšmės nėra `tuple`. Pvz.:

```Python
raidziu_tuple = ('a', 'b', 'c', 'a', 'd')

print('a' in raidziu_tuple)  # True
print('e' in raidziu_tuple)  # False
```

## Iteravimas

`tuple` yra iteruojamas objektas, tai reiškia, kad jo elementus galite pereiti vieną po kito naudodami `for` ciklą arba `while` ciklą.

`for` ciklo pvz:

```Python
raidziu_tuple = ('a', 'b', 'c', 'a', 'd')

for raide in raidziu_tuple:
    print(raide)
```

Rezultatas:

```Text
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

Rezultatas:

```Text
a
b
c
a
d
```

Kaip matote, `while` cikle naudojame `len()` funkciją, kad sužinotume, kiek `tuple` turi elementų. Tada, naudodami kintamąjį `i`, per kiekvieną iteraciją gautume reikšmę, kurią spausdintume, ir padidintume `i` reikšmę vienetu, kad galėtume per eiti per kitą `tuple` elementą.

## Užduotys

- Sukurkite du `tuple`, kurie susideda iš jūsų mėgstamų grupių pavadinimų. Sujunkite juos į vieną naują `tuple`.
- Atspausdinkite naują `tuple`.
- Atspausdinkite visus `tuple` elementus atskirose eilutėse.
- Patikrinkite ar kuri nors grupė yra `tuple`.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<hr>

```Python
megstamos_grupes = ('Metallica', 'Deep Purple', 'Dio', 'Pearl Jam')
megstamiausios_grupes = ('Queen', 'AC/DC', 'Led Zeppelin')

visos_grupes = megstamos_grupes + megstamiausios_grupes

print(visos_grupes)

for grupe in visos_grupes:
    print(grupe)

print('Black Sabbath' in visos_grupes)
```

Rezultatas:

```Text
('Metallica', 'Deep Purple', 'Dio', 'Pearl Jam', 'Queen', 'AC/DC', 'Led Zeppelin')
Metallica
Deep Purple
Dio
Pearl Jam
Queen
AC/DC
Led Zeppelin
False
```

</details>