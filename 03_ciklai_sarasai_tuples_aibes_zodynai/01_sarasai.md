# Sąrašai

Sąrašai (`lists`) yra objektų rinkiniai, kurie gali būti priskirti kintamiesiems ir manipuliuojami programos metu. Jie yra dinaminiai ir gali būti atnaujinami arba praplėsti, kai programa vykdoma.

## Sąrašų kūrimas

Python leidžia sukurti sąrašus naudojant laužtinius skliaustus `[ ]`. Sąrašo elementus atskiriame kableliais `,`. Pvz.:

```Python
tuscias_sarasas = []
skaiciu_sarasas = [1, 2, 3, 4, 5]
zodziu_sarasas = ['obuolys', 'kriaušė', 'bananas']
misrus_sarasas = ['obuolys', 2, 1.4, 'kriaušė', True, 'bananas']
```

Sąraše `skaiciu_sarasas` yra skaičiai, `zodziu_sarasas` - žodžiai, o  `misrus_sarasas` - mišrūs objektai. Pastebime, kad sąraše gali būti skirtingi objektai, jie nėra apribojami vieno tipo duomenų.

Sąrašą taip pat galima sukurti naudojant `list()` funkciją ir perduodant jai elementus. Pvz.:

```Python
tuscias_sarasas = list()
```

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

❗ Pastebėkite, kad naudojant neigiamus indeksus -1 yra paskutinis sąrašo elementas.

## Sąrašų dalijimas

Sąrašus taip pat galima dalinti (`slicing`), kad gautumėte tik dalį sąrašo. Norėdami tai padaryti, naudokite `:` simbolius. Galima nurodyti pradinį indeksą ir galinį indeksą laužtiniuose skliaustuose. Kai nenurodomas pradinis indeksas, Python automatiškai priskiria pradinį indeksą 0. Kai nenurodomas galinis indeksas, Python automatiškai priskiria galinį indeksą sąrašo pabaigos indeksui. Taip pat galima naudoti neigiamus indeksus, kad pradėtumėte skaičiavimą sąrašo pabaigos pusėje. Pvz.:

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

## Sąrašų elementų keitimas

Sąrašo elementus galima keisti priskiriant naują reikšmę konkrečiam indeksui. Pvz.:

```Python
sarasas = ['obuolys', 'kriaušė', 'bananas']
sarasas[1] = 'avokadas'
print(sarasas)   # ['obuolys', 'avokadas', 'bananas']
```

Taip pat galima keisti daugiau nei vieną elementą vienu metu, naudojant dalijimą. Pvz.:

```Python
sarasas = ['obuolys', 'kriaušė', 'bananas', 'apelsinas', 'persimonas']
sarasas[1:4] = ['ananasas', 'mangas']
print(sarasas)   # ['obuolys', 'ananasas', 'mangas', 'persimonas']
```

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

## Sąrašų ilgio matavimas

`len()` grąžina sąrašo elementų skaičių. Tai yra naudinga, kai norime sužinoti, kiek elementų yra sąraše.

```Python
sarasas = [1, 2, 3, 4, 5]
print(len(sarasas)) # 5
```

## Patikrinti ar elementas yra sąraše

Norint patikrinti, ar elementas yra sąraše, galima naudoti `in` raktinį žodį. Šis žodis patikrina, ar elementas yra sąraše, ir grąžina `True`, jei taip, ir `False`, jei ne.

```Python
sarasas = ['obuolys', 'bananas', 'kriause']
print('obuolys' in sarasas) # True
print('melionas' in sarasas) # False
```

## Užduotys

### Pirma užduotis

- Sukurkite sąrašą su bent penkiais jūsų mėgstamų maisto produktų pavadinimais.
- Atspausdinkite visą sąrašą.

### Antra užduotis

- Atspausdinkite sąrašo pirmą elementą.
- Atspausdinkite sąrašo trečią elementą.
- Atspausdinkite sąrašo paskutinį elementą.

### Trečia užduotis

- Atspausdinkite sąrašo pirmus tris elementus.
- Atspausdinkite sąrašo paskutinius du elementus.
- Atspausdinkite tris elementus iš sąrašo vidurio.
- Atspausdinkite sąrašo kas antrą elementą.

### Ketvirta užduotis

Atlikite žemiau nurodytus veiksmus su turimu sąrašu ir po kiekvieno veiksmo, sąrašą atspausdinkite:

- Pridėkite dar vieną mėgstamo maisto pavadinimą į sąrašo galą.
- Įterpkite naują maisto produktą į sąrašo ketvirtą vietą.
- Pakeiskite antrąjį sąrašo elementą kitu mėgstamo maisto pavadinimu.
- Ištrinkite pirmąjį sąrašo elementą.
- Ištrinkite sąrašo trečią elementą.
- Suraskite sąraše kurio nors elemento indeksą.
- Atspausdinkite sąrašą atvirkštine tvarka.
- Pabandykite papildomai panaudoti kitus metodus.

### Penkta užduotis

- Patikrinkite sąrašo ilgį.

### Šešta užduotis

- Patikrinkite ar tam tikras produktas yra sąraše.

## Atsakymai į užduotis

<details><summary>❗ Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
maisto_produktai = ['obuoliai', 'sūris', 'kepta duona', 'mėsa', 'bulvės']
print(maisto_produktai)
```

Rezultatas:

```Text
['obuoliai', 'sūris', 'kepta duona', 'mėsa', 'bulvės']
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
print(maisto_produktai[0])
print(maisto_produktai[2])
print(maisto_produktai[-1])
```

Rezultatas:

```Text
obuoliai
kepta duona
bulvės
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
print(maisto_produktai[:3])
print(maisto_produktai[-2:])
print(maisto_produktai[1:4])
print(maisto_produktai[::2])
```

Rezultatas:

```Text
['obuoliai', 'sūris', 'kepta duona']
['mėsa', 'bulvės']
['sūris', 'kepta duona', 'mėsa']
['obuoliai', 'kepta duona', 'bulvės']
```

</details>
<details>
<summary>Ketvirta užduotis</summary>
<hr>

```Python
maisto_produktai.append('bananai')
print(maisto_produktai)

maisto_produktai.insert(3, 'avokadas')
print(maisto_produktai)

maisto_produktai[1] = 'varškė'
print(maisto_produktai)

del maisto_produktai[0]
print(maisto_produktai)

maisto_produktai.pop(2)
print(maisto_produktai)

print(maisto_produktai.index('bulvės'))

maisto_produktai.reverse()
print(maisto_produktai)
```

Rezultatas:

```Text
['obuoliai', 'sūris', 'kepta duona', 'mėsa', 'bulvės', 'bananai']
['obuoliai', 'sūris', 'kepta duona', 'avokadas', 'mėsa', 'bulvės', 'bananai']
['obuoliai', 'varškė', 'kepta duona', 'avokadas', 'mėsa', 'bulvės', 'bananai']
['varškė', 'kepta duona', 'avokadas', 'mėsa', 'bulvės', 'bananai']
['varškė', 'kepta duona', 'mėsa', 'bulvės', 'bananai']
3
['bananai', 'bulvės', 'mėsa', 'kepta duona', 'varškė']
```

</details>
<details>
<summary>Penkta užduotis</summary>
<hr>

```Python
print(len(maisto_produktai))
```

Rezultatas:

```Text
5
```

</details>
<details>
<summary>Šešta užduotis</summary>
<hr>

```Python
print('abrikosas' in maisto_produktai)
```

Rezultatas:

```Text
False
```

</details>
