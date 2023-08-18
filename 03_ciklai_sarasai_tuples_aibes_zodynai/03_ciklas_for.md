# Ciklai `for`

`for` ciklas yra Python programavimo kalbos ciklas, kuris leidžia iteruoti tam tikrą rinkinį elementų, pvz., sąrašus, žodynus ir kt.

❗ Iteracija yra bendras terminas, naudojamas programavimo ir kompiuterinių mokslų srityse, kuris reiškia procesą, kai tam tikros operacijos yra atliekamos kartojant tas pačias instrukcijas daug kartų su skirtingais duomenimis. Tai yra proceso dalis, kurio metu programos vykdomas kodas yra kartojamas tam tikrą skaičių kartų arba tol, kol yra patenkinama tam tikra sąlyga.

`for` cikle yra nurodomas kintamasis (ar kintamieji), kuriame saugomas kiekvieno žingsio iteracijos elementas. Ciklo blokas rašomas su atitraukimu nuo kairės pusės ir yra vykdomas kiekvienam rinkinio iteracijos žingsniui.

## Ciklas su sąrašu

Pavyzdžiui, jei turime sąrašą skaičių ir norime atspausdinti kiekvieną skaičių, galime naudoti `for` ciklą kaip parodyta žemiau:

```Python
skaiciai = [1, 2, 3, 4, 5]

for skaicius in skaiciai:
    print(skaicius)
```

Rezultatas:

```Text
1
2
3
4
5
```

Taip pat galima susumuoti visas sąrašo reiškmes:

```Python
skaiciai = [2, 6, 7, 9, 41, 4, 46, 789]

skaiciu_suma = 0

for skaicius in skaiciai:
    skaiciu_suma += skaicius

print(skaiciu_suma) # 904
```

## `for` ciklas su žodynu

Taip pat galime naudoti `for` ciklą su žodynu. Yra keli variantai kaip tai galima padaryti.

Šis ciklas iteruos per žodyno raktus (`keys`) ir grąžins kiekvieną raktą atskirai. Pvz.:

```Python
amzius = {'Rokas': 20, 'Andrius': 34, 'Laura': 25}

for irasas in amzius:
    print(irasas)
```

Rezultatas:

```Text
Rokas
Andrius
Laura
```

Cikle galime naudoti žodyno metodą `.values()`, tada ciklas iteruos per žodyno reikšmes (`values`) ir grąžins kiekvieną reikšmę atskirai. Pvz.:

```Python
amzius = {'Rokas': 20, 'Andrius': 34, 'Laura': 25}

for irasas in amzius.values():
    print(irasas)
```

Rezultatas:

```Text
20
34
25
```

Kai nurodome raktą, reikšmę ir `.items()`, ciklas iteruos per žodyno raktus, reikšmes ir grąžins kiekvieną raktą ir reikšmę atskirai. Pvz.:

```Python
amzius = {'Rokas': 20, 'Andrius': 34, 'Laura': 25}

for raktas, reiksme in amzius.items():
    print(raktas, reiksme)
```

Rezultatas:

```Text
Rokas 20
Andrius 34
Laura 25
```

Taip pat galima kreiptis į žodyno elementus su raktu cikle. Ypač rekomenduojama keičiant reiškmes:

```Python
amzius = {'Rokas': 20, 'Andrius': 34, 'Laura': 25}

for irasas in amzius:
    print("Dabar", irasas, amzius[irasas])
    amzius[irasas] += 1
    print("Po pakeitimo", irasas, amzius[irasas])
```

Rezultatas:

```Text
Dabar Rokas 20
Po pakeitimo Rokas 21
Dabar Andrius 34
Po pakeitimo Andrius 35
Dabar Laura 25
Po pakeitimo Laura 26
```

## `for` ciklas su `range` funkcija

`range()` funkcija sugeneruoja seką skaičių nuo pradžios iki pabaigos. Galime naudoti `for` ciklą su `range` funkcija, kad atliktume tam tikrus veiksmus su kiekvienu skaičiumi šioje sekoje.

```Python
for skaicius in range(1, 6):
    print(skaicius)
```

Rezultatas:

```Text
1
2
3
4
5
```

## Ciklas nutraukimo komanda `break`

Kai naudojame `break` komandą, ciklas baigiasi ir programa tęsiasi nuo kito kodo bloko, kuris yra po ciklo bloko. Pvz.:

```Python
skaiciai = [1, 2, 3, 4, 5]

for skaicius in skaiciai:
    if skaicius == 3:
        break
    print(skaicius)
```

Rezultatas:

```Text
1
2
```

Kaip matote, programa nutraukė ciklą, kai buvo pasiektas skaičius "3", ir neatspausdino kitų skaičių, kurie buvo sąraše po jo.

## Ciklo žingsnio tolimesnio vykdymo praleidimo komanda `continue`

Kai naudojame `continue` komandą, programa praleidžia šią iteraciją ir tęsia su kitu rinkinio elementu. Pvz.:

```Python
skaiciai = [1, 2, 3, 4, 5]

for skaicius in skaiciai:
    if skaicius == 3:
        continue
    print(skaicius)
```

Rezultatas:

```Text
1
2
4
5
```

Kaip matote, programa praleido skaičių "3" ir tęsė su likusiais skaičiais sąraše.

## Ciklo `for` pabaigos `else` blokas

`else` blokas yra naudojamas norint atlikti tam tikrus veiksmus, kai `for` ciklas pasiekia savo pabaigą.

```Python
skaiciai = [1, 2, 3, 4, 5]

for skaicius in skaiciai:
    print(skaicius)
else:
    print('Ciklo vykdymas baigtas.')
```

Rezultatas:

```Text
1
2
3
4
5
Ciklo vykdymas baigtas
```

Jeigu ciklas buvo nutrauktas su `break` komanda, `else` sąlygos blokas nebus vykdomas.

## Sąrašų iteravimas su indeksu

`enumerate()` funkcija naudojama kartu su `for` ciklu gražina poras, kurių kiekvienos poros pirmasis elementas yra elemento indeksas, o antrasis - elementas paties sąrašo. Pvz.:

```Python
sarasas = ['a', 'b', 'c', 'd', 'e']
for indeksas, reiksme in enumerate(sarasas):
    print(indeksas, reiksme)
```

Rezultatas:

```Text
0 a
1 b
2 c
3 d
4 e
```

## Ciklas cikle

Ciklo cikle konstrukcija leidžia kurti ciklus, kuriuose vienas ar kelias vidiniai ciklai yra vykdomi kiekvienai išorinio ciklo iteracijai. Tai ypač naudinga, kai turime kokią nors duomenų struktūrą, kurią reikia išgryninti arba apdoroti sudėtingu būdu. Pvz.:

```Python
spalvos = ['raudonas', 'geltonas', 'mėlynas']
dydziai = ['mažas', 'vidutinis', 'didelis']

for spalva in spalvos:
    for dydis in dydziai:
        print(dydis, spalva, 'šikšnosparnis')
```

Rezultatas:

```Text
mažas raudonas šikšnosparnis
vidutinis raudonas šikšnosparnis
didelis raudonas šikšnosparnis
mažas geltonas šikšnosparnis
vidutinis geltonas šikšnosparnis
didelis geltonas šikšnosparnis
mažas mėlynas šikšnosparnis
vidutinis mėlynas šikšnosparnis
didelis mėlynas šikšnosparnis
```

## Užduotys

### Pirma užduotis

- Sukurkite sąrašą su bent penkiais elementais
- Atspausdinkite jį naudodami `for` ciklą

### Antra užduotis

Sukurti programą, kuri:

- Leistų vartotojui po vieną įvesti 5 žodžius
- Pridėtų įvestus žodžius į sąrašą
- Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
- Iššūkis 💡: padarykite, kad programa leistų įvesti norimą žodžių kiekį

Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index

### Trečia užduotis

Sukurti programą, kuri:

- Leistų vartotojui įvesti metus
- Atspausdintų "Keliamieji metai", jei taip yra
- Atspausdintų "Nekeliamieji metai", jei taip yra

### Ketvirta užduotis

- Perdaryti trečią užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų.

### Penkta užduotis

- Išnaudojant ciklą cikle, išspausdinkite visą šaldytuvo skyrių turinį. Šaldytuvas yra skyrių žodynas, kur skyrius yra produktų žodynas. Produkto reikįmė yra kiekis.

## Atsakymai į užduotis

<details><summary>❗ Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
savaite = ['pirmadienis', 'antradienis', 'trečiadienis', 'ketvirtadienis', 'penktadienis', 'šeštadienis', 'sekmadienis']

for diena in savaite:
    print(diena)
```

Rezultatas:

```Text
pirmadienis
antradienis
trečiadienis
ketvirtadienis
penktadienis
šeštadienis
sekmadienis
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
zodziai = []

for zodis in range(5):
    zodziai.append(input('Įveskite žodį: '))

for numeris, zodis in enumerate(zodziai):
    print(f'{numeris + 1}: {zodis}, simbolių kiekis: {len(zodis)}')
print('Žodžių kiekis:', len(zodziai))
```

Rezultatas:

```Text
Įveskite žodį: Labas
Įveskite žodį: rytas
Įveskite žodį: studentai
Įveskite žodį: Kaip
Įveskite žodį: sekasi?
1: Labas, simbolių kiekis: 5
2: rytas, simbolių kiekis: 5
3: studentai, simbolių kiekis: 9
4: Kaip, simbolių kiekis: 4
5: sekasi?, simbolių kiekis: 7
Žodžių kiekis: 5
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
metai = int(input('Įveskite metus: '))
if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
    print('Keliamieji metai')
else:
    print('Nekeliamieji metai')
```

Rezultatas:

```Text
Įveskite metus: 2024
Keliamieji metai
```

</details>
<details>
<summary>Ketvirta užduotis</summary>
<hr>

```Python
for metai in range(2000, 2100):
    if metai % 400 == 0:
        print(metai)
    elif metai % 100 == 0:
        continue
    elif metai % 4 == 0:
        print(metai)
    else:
        continue
```

Rezultatas:

```Text
2000
2004
2008
2012
2016
2020
2024
2028
2032
2036
2040
2044
2048
2052
2056
2060
2064
2068
2072
2076
2080
2084
2088
2092
2096
```

</details>
</details>
