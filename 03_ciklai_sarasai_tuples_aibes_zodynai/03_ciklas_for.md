# `for` ciklai

`for` ciklas yra Python programavimo kalbos ciklas, kuris leidžia iteruoti tam tikrą rinkinį elementų, pvz., sąrašus, žodynas ir kt.

❗ Iteracija yra bendras terminas, naudojamas programavimo ir kompiuterinių mokslų srityse, kuris reiškia procesą, kai tam tikros operacijos yra atliekamos kartojant tas pačias instrukcijas daug kartų su skirtingais duomenimis. Tai yra proceso dalis, kurio metu programos vykdomas kodas yra kartojamas tam tikrą skaičių kartų arba tol, kol yra patenkinama tam tikra sąlyga.

`for` cikle yra nurodomas kintamasis, kuriame bus saugomi kiekvieno iteracijos metu pasirinkto rinkinio elementai. Ciklo blokas rašomas su atitraukimu nuo kairės pusės ir yra vykdomas kiekvienai rinkinio elementų iteracijai.

## `for` ciklas su sąrašu

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

Taip pat galime naudoti `for` ciklą su žodynu, yra keli variantai kaip tai galima padaryti.

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

Kai naudojame `values()`, ciklas iteruos per žodyno reikšmes (`values`) ir grąžins kiekvieną reikšmę atskirai. Pvz.:

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

Kai nurodome raktą, reikšmę ir `items()`, ciklas iteruos per žodyno raktus, reikšmes ir grąžins kiekvieną raktą ir reikšmę atskirai. Pvz.:

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

## `for` ciklas su `break` komanda

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

## `for` ciklas su `continue` komanda

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

## `for` ciklas su `else` bloku

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

# Užduotys