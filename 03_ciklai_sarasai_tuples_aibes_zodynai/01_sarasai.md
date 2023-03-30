# Sąrašai

Sąrašai (`lists`) yra objektų rinkiniai, kurie gali būti priskirti kintamiesiems ir manipuliuojami programos metu. Jie yra dinaminiai ir gali būti atnaujinami arba praplėsti, kai programa vykdoma.

<br>

## Sąrašų kūrimas

Python leidžia sukurti sąrašus naudojant laužtinius skliaustus `[ ]`. Sąrašo elementus atskiriame kableliais `,`. Pvz.:

```Python
skaiciu_sarasas = [1, 2, 3, 4, 5]
zodziu_sarasas = ['obuolys', 'kriaušė', 'bananas']
misrus_sarasas = ['obuolys', 2, 1.4, 'kriaušė', True, 'bananas']
```

Pirmame sąraše skaiciu_sarasas yra skaičiai, antrame zodziu_sarasas - žodžiai, o trečiame misrus_sarasas - mišrūs objektai. Pastebime, kad sąraše gali būti skirtingi objektai, jie nėra apribojami vieno tipo duomenų.

Sąrašą taip pat galima sukurti naudojant `list()` funkciją ir perduodant jai elementus. Pvz.:

```Python
sarasas = list(('obuolys', 'kriaušė', 'bananas'))
```

<br>

## Sąrašų indeksavimas

Sąrašų elementai yra numeruojami nuo nulio. Kad galėtumėte pasiekti sąrašo elementus, tiesiog naudokite indeksavimą laužtiniuose skliaustuose. Pvz.:

```Python
sarasas = ['obuolys', 'kriaušė', 'bananas']
print(sarasas[0])   # obuolys
print(sarasas[1])   # kriaušė
print(sarasas[2])   # bananas
```

Taip pat galite pasiekti elementus atbuline tvarka, naudodami neigiamus indeksus. Pvz.:

```Python
sarasas = ['obuolys', 'kriaušė', 'bananas']
print(sarasas[-1])   # bananas
print(sarasas[-2])   # kriaušė
print(sarasas[-3])   # obuolys
```

❗Pastebėkite, kad naudojant neigiamus indeksus -1 yra paskutinis sąrašo elementas.

<br>

## Sąrašų dalijimas

Sąrašus taip pat galima dalinti (`slicing`), kad gautumėte tik dalį sąrašo. Norėdami tai padaryti, naudokite `:` simbolius. Reikia nurodyti pradinį indeksą ir galinį indeksą, tarp kurių yra laužtiniai skliaustai. Kai nenurodomas pradinis indeksas, Python automatiškai priskiria pradinį indeksą 0. Kai nenurodomas galinis indeksas, Python automatiškai priskiria galinį indeksą sąrašo pabaigos indeksui. Taip pat galima naudoti neigiamus indeksus, kad pradėtumėte skaičiavimą sąrašo pabaigos pusėje. Pvz.:

```Python
sarasas = ['obuolys', 'kriaušė', 'bananas', 'apelsinas', 'persimonas']
print(sarasas[:3])    # ['obuolys', 'kriaušė', 'bananas']
print(sarasas[2:])    # ['bananas', 'apelsinas', 'persimonas']
print(sarasas[1:4])   # ['kriaušė', 'bananas', 'apelsinas']
print(sarasas[-3:])   # ['bananas', 'apelsinas', 'persimonas']

```

Be to, galite nurodyti trečiąjį argumentą, kuris nurodo žingsnio dydį. Žingsnio dydis nurodo, kiek elementų yra praleidžiami tarp kiekvieno pasirinkto elemento. Šiuo atveju žingsnio dydis yra 2, todėl iš sąrašo išgaunami kas antras elementas, pradedant nuo pradinio indekso:

```Python
sarasas = ['obuolys', 'kriaušė', 'bananas', 'apelsinas', 'persimonas']
print(sarasas[::2])   # ['obuolys', 'bananas', 'persimonas']
```

<br>

## Sąrašų metodai

Sąrašų metodai leidžia manipuliuoti sąrašais ir atlikti įvairias operacijas, tokiu būdu keičiant sąrašų turinį.

`append()` metodas naudojamas pridėti vieną elementą į sąrašą. Šis metodas prideda elementą sąrašo pabaigoje.

```Python
sarasas = [1, 2, 3]
sarasas.append(4)
print(sarasas) # [1, 2, 3, 4]
```

`extend()` metodas naudojamas pridėti daugiau nei vieną elementą į sąrašą. Šis metodas priima kito sąrašo elementus ir prideda juos į pabaigą.

```Python
sarasas1 = [1, 2, 3]
sarasas2 = [4, 5, 6]
sarasas1.extend(sarasas2)
print(sarasas1) # [1, 2, 3, 4, 5, 6]
```

`insert()` metodas naudojamas įterpti naują elementą į sąrašą norimoje vietoje. Pirmasis argumentas yra indeksas, kuriame norite įterpti elementą, o antrasis argumentas yra elementas, kurį norite įterpti.

```Python
sarasas = [1, 2, 3]
sarasas.insert(1, 4)
print(sarasas) # [1, 4, 2, 3]
```

`remove()` metodas naudojamas pašalinti elementą iš sąrašo. Jis pašalina pirmą pasirinktą elementą, jei jis yra tame sąraše.

```Python
sarasas = [1, 2, 3, 4]
sarasas.remove(3)
print(sarasas) # [1, 2, 4]
```

`pop()` metodas naudojamas pašalinti elementą iš sąrašo pagal jo indeksą. Jis pašalina elementą ir grąžina jį kaip rezultatą. Jei jis nenurodytas, pop() pašalina paskutinį elementą.

```Python
sarasas = [1, 2, 3, 4]
paskutinis_elementas = sarasas.pop()
print(paskutinis_elementas) # 4
pirmas_elementas = sarasas.pop(0)
print(pirmas_elementas) # 1
print(sarasas) # [2, 3]
```

`index()` metodas naudojamas rasti indeksą, kuriame yra pasirinktas elementas.

```Python
sarasas = [1, 2, 3, 4]
indeksas = sarasas.index(3)
print(indeksas) # 2
```

`count()` metodas grąžina kiek kartų tam tikra reikšmė pasikartoja sąraše. Šis metodas priima vieną argumentą - reikšmę, kurią norite patikrinti.

```Python
sarasas = [1, 2, 2, 3, 4]
kiekis = sarasas.count(2)
print(kiekis) # 2
```

`sort()` metodas surikiuoja sąrašą didėjimo tvarka (nuo mažiausios iki didžiausios reikšmės).

```Python
sarasas = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sarasas.sort()
print(sarasas)  # [1, 1, 2, 3, 4, 5, 5, 6, 9]
```

Jei norime rikiuoti sąrašą atvirkštine tvarka, turime nurodyti argumentą `reverse=True`.

```Python
sarasas = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sarasas.sort(reverse=True)
print(sarasas)  # [9, 6, 5, 5, 4, 3, 2, 1, 1]
```

`reverse()` metodas atvirkštine tvarka išdėsto sąrašo elementus.

```Python
sarasas = [1, 2, 3, 6, 7, 4, 5]
sarasas.reverse()
print(sarasas)  # [5, 4, 7, 6, 3, 2, 1]
```

<br>

## Sąrašų ilgio matavimas

`len()` grąžina sąrašo elementų skaičių. Tai yra naudinga, kai norime sužinoti, kiek elementų yra sąraše.

```Python
sarasas = [1, 2, 3, 4, 5]
print(len(sarasas)) # 5
```

<br>

# Užduotys

### Pirma užduotis

- Sukurkite sąrašą, kuriame yra keli jūsų mėgstamų maisto produktų pavadinimai.
- Atspausdinkite visą sąrašą.
- Atspausdinkite sąrašo paskutinį elementą.
- Pridėkite dar vieną mėgstamo maisto pavadinimą į sąrašo galą.
- Ištrinkite pirmąjį sąrašo elementą.
- Pakeiskite antrąjį sąrašo elementą kitu mėgstamo maisto pavadinimu.
- Įtraukite du naujus maisto produktus į sąrašą, vieną pradžioje, kitą viduryje.
- Ištrinkite sąrašo trečią elementą.
- Suraskite sąraše "sriubą" indeksą.
- Įterpkite naują maisto produktą "kepta vištiena" į sąrašo ketvirtą vietą.
- Išvalykite sąrašą.

# Atsakymai į užduotis
<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
  <summary>Pirma užduotis</summary>
  <hr>

```Python
maisto_produktai = ['Cepelinai', 'Sriuba', 'Koldūnai', 'Kebabai']
print("Visas sąrašas:", maisto_produktai)
print("Sąrašo paskutinis elementas:", maisto_produktai[-1])
maisto_produktai.append('Pica')
print("Sąrašas su pridėtu elementu:", maisto_produktai)
maisto_produktai.pop(0)
print("Sąrašas be pirmojo elemento:", maisto_produktai)
maisto_produktai[1] = 'Kepsnys'
print("Sąrašas su pakeistu antruoju elementu:", maisto_produktai)
maisto_produktai.insert(0, 'Kava')
maisto_produktai.insert(2, 'Makaronai')
print("Sąrašas su įtrauktais elementais:", maisto_produktai)
maisto_produktai.pop(2)
print("Sąrašas be trečiojo elemento:", maisto_produktai)
sriubos_indeksas = maisto_produktai.index('Sriuba')
print("Sąrašo 'Sriuba' indeksas:", sriubos_indeksas)
maisto_produktai.insert(3, 'Kepta vištiena')
print("Sąrašas su įterptu nauju elementu:", maisto_produktai)
maisto_produktai.clear()
print("Išvalytas sąrašas:", maisto_produktai)

```
<p>Output:</p>

```Python
Visas sąrašas: ['Cepelinai', 'Sriuba', 'Koldūnai', 'Kebabai']
Sąrašo paskutinis elementas: Kebabai
Sąrašas su pridėtu elementu: ['Cepelinai', 'Sriuba', 'Koldūnai', 'Kebabai', 'Pica']
Sąrašas be pirmojo elemento: ['Sriuba', 'Koldūnai', 'Kebabai', 'Pica']
Sąrašas su pakeistu antruoju elementu: ['Sriuba', 'Kepsnys', 'Kebabai', 'Pica']
Sąrašas su įtrauktais elementais: ['Kava', 'Sriuba', 'Makaronai', 'Kepsnys', 'Kebabai', 'Pica']
Sąrašas be trečiojo elemento: ['Kava', 'Sriuba', 'Kepsnys', 'Kebabai', 'Pica']
Sąrašo 'Sriuba' indeksas: 1
Sąrašas su įterptu nauju elementu: ['Kava', 'Sriuba', 'Kepsnys', 'Kepta vištiena', 'Kebabai', 'Pica']
Išvalytas sąrašas: []
```
</details>