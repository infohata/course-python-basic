# Žodynai

Žodynai yra viena iš pagrindinių Python duomenų struktūrų, kurias galima naudoti kaip raktų ir reikšmių porų kolekcijas. Kiekvienas raktas turi priskirtą reikšmę, kurią galima pasiekti naudojant šio rakto pavadinimą.

## Žodynų kūrimas

Žodynus galima sukurti naudojant riestinius skliaustus `{}`. Kiekvienas raktas ir reikšmė yra atskirti dvitaškiais, o kelių raktų/reikšmių kombinacijos atskiriamos kableliais. Pvz.:

```Python
zodynas = {'raktas1': 'reiksme1', 'raktas2': 'reiksme2'}
print(zodynas) # {'raktas1': 'reiksme1', 'raktas2': 'reiksme2'}
```

## Pasiekti konkretų žodyno įrašą

Norint pasiekti konkretų žodyno įrašą, reikia tiesiog nurodyti raktą laužtiniuose skliaustuose:

```Python
zmones = {'Jonas': 24, 'Petras': 32}
print(zmones['Petras']) # 32
print(zmones['Jonas']) # 24
```

## Pridėti žodyno įrašą

Žodyno įrašo pridėjimui galima naudoti paprastą priskyrimo operatorių `=`, raktą nurodant po žodyno kintamojo pavadinimo laužtiniuose skliaustuose. Pvz.:

```Python
zmones = {'Jonas': 24, 'Petras': 32}
zmones['Ona'] = 28
print(zmones) # {'Jonas': 24, 'Petras': 32, 'Ona': 28}
```

## Pakeisti konkretų žodyno įrašą

Norint pakeisti žodyno įrašą, reikia prie žodyno kintamojo pavadinimo laužtiniuose skliaustuose nurodyti jau esamą raktą ir priskirti naują reikšmę:

```Python
zmones = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
zmones['Petras'] = 33
print(zmones) # {'Jonas': 24, 'Petras': 33, 'Ona': 28}
```

## Ištrinti konkretų žodyno įrašą

Norint ištrinti žodyno įrašą, reikia naudoti `del` komandą prieš žodyno kintamąjį su raktu laužtiniuose skliaustuose, kurio reikšmės norime ištrinti iš žodyno.

```Python
zmones = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
del zmones['Ona']
print(zmones) # {'Jonas': 24, 'Petras': 32}
```

## Žodynų metodai

Žodynų metodai leidžia atlikti veiksmus su žodynu ir manipuliuoti jo turiniu. Štai keletas dažniausiai naudojamų metodų:

`.keys()` grąžina visus žodyno raktažodžius.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
raktažodžiai = zodynas.keys()
print(raktažodžiai) # dict_keys(['Jonas', 'Petras', 'Ona'])
```

`.values()` grąžina visas žodyno reikšmes.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
reiksmes = zodynas.values()
print(reiksmes) # dict_values([24, 32, 28])
```

`.items()` grąžina visus žodyno raktažodžių ir reikšmių porų sąrašą.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
poros = zodynas.items()
print(poros) # dict_items([('Jonas', 24), ('Petras', 32), ('Ona', 28)])
```

`.get()` grąžina reikšmę, atitinkančią nurodytą raktą. Jei raktas nerastas, grąžina numatytąją reikšmę (nurodoma atskiru argumentu) arba `None`.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
reiksme = zodynas.get('Jonas')
print(reiksme) # 24
print(zodynas.get('Juozas', 0)) # 0
print(zodynas.get('Juozas')) # None
```

`pop()` pašalina ir grąžina reikšmę, atitinkančią nurodytą raktą. Jei raktas nerastas, grąžina numatytąją reikšmę (nurodoma atskiru argumentu) arba išmeta klaidą.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
reiksme = zodynas.pop('Petras')
print(reiksme) # 32
nerasta = zodynas.pop('Juozas', 0) 
print(nerasta) # 0
print(zodynas) # {'Jonas': 24, 'Ona': 28}
```

`clear()` išvalo žodyno turinį.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
zodynas.clear()
print(zodynas) # {}
```

## Užduotys

### Pirma užduotis

- Sukurkite žodyną su bent trimis augintinių vardais ir jų amžiumi.
- Atspausdinkite visą žodyną.

### Antra užduotis

- Atspausdinkite kurio nors augintinio amžių.

### Trečia užduotis

- Pridėkite naują augintinį.

### Ketvirta užduotis

- Pakeiskite kurio nors augintinio amžių.

### Penkta užduotis

- Ištrinkite kurį nors augintinį.
- Atspausdinkite visą žodyną.

### Šešta užduotis

- Atspausdinkite visų augintinių vardus.
- Atspausdinkite visų augintinių amžius.
- Atspausdinkite visų augintinių vardų ir amžių sąrašą.
- Atspausdinkite konkretaus augintinio amžių pagal jo vardą.
- Pabandykite papildomai panaudoti kitus metodus.

### Bonus užduotis
<!-- TODO: perdaryti automobilių sąrašą į sąrašą, ir šią užduotį palikti kaip antrą/trečia. Pradžiai reikėtų duoti paprastesnę -->

- Sukurkite tuščią žodyną pavadinimu "automobiliai" ir pridėkite prie žodyno informaciją apie 3 skirtingus automobilius (nebijokite naudoti savo kūrybiškumo ir įtraukti įvairių markių, modelių, metų, spalvų ir variklių tipų).
- Išveskite žodyno informaciją apie vieną iš automobilių.
- Pakeiskite informaciją apie vieną automobilį (pavyzdžiui, pakeiskite variklio tipą).
- Pridėkite naują automobilį į žodyną.
- Pašalinkite informaciją apie vieną automobilį iš žodyno.
- Išveskite kiek yra automobilių žodyne.
- Patikrinkite ar tam tikras automobilis yra žodyne.
- Išvalykite žodyną.

## Atsakymai į užduotis

<details><summary>❗ Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
augintiniai = {'Reksas': 3, 'Lakis': 2, 'Pūkelis': 7}
print(augintiniai)
```

Rezultatas:

```Text
{'Reksas': 3, 'Lakis': 2, 'Pūkelis': 7}
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
print(augintiniai['Reksas'])
```

Rezultatas:

```Text
3
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
augintiniai['Pupa'] = 1
print(augintiniai)
```

Rezultatas:

```Text
{'Reksas': 3, 'Lakis': 2, 'Pūkelis': 7, 'Pupa': 1}
```

</details>
<details>
<summary>Ketvirta užduotis</summary>
<hr>

```Python
augintiniai['Lakis'] = 4
print(augintiniai)
```

Rezultatas:

```Text
{'Reksas': 3, 'Lakis': 4, 'Pūkelis': 7, 'Pupa': 1}
```

</details>
<details>
<summary>Penkta užduotis</summary>
<hr>

```Python
del augintiniai['Pūkelis']
print(augintiniai)
```

Rezultatas:

```Text
{'Reksas': 3, 'Lakis': 4, 'Pupa': 1}
```

</details>
<details>
<summary>Šešta užduotis</summary>
<hr>

```Python
vardai = augintiniai.keys()
print(vardai)

amzius = augintiniai.values()
print(amzius)

augintiniu_sarasas = augintiniai.items()
print(augintiniu_sarasas)

suo = augintiniai.get('Reksas')
print(suo)
```

Rezultatas:

```Text
dict_keys(['Reksas', 'Lakis', 'Pupa'])
dict_values([3, 4, 1])
dict_items([('Reksas', 3), ('Lakis', 4), ('Pupa', 1)])
3
```

</details>
<details>
<summary>Bonus užduotis</summary>
<hr>

```Python
automobiliai = {
    '1': {
        'marke': 'Audi',
        'modelis': 'A6',
        'metai': 2020,
        'spalva': 'Juoda',
        'variklis': 'Benzinas'
    },
    '2': {
        'marke': 'Tesla',
        'modelis': 'Model S',
        'metai': 2018,
        'spalva': 'Raudona',
        'variklis': 'Elektra'
    },
    '3': {
        'marke': 'Ferrari',
        'modelis': '488 GTB',
        'metai': 2019,
        'spalva': 'Geltona',
        'variklis': 'Benzinas'
    }
}
print("Automobilis nr.2:", automobiliai['2'])
automobiliai['3']['variklis'] = 'Elektra'
print("Automobilis nr.3 po variklio pakeitimo:", automobiliai['3'])
automobiliai['4'] = {
    'marke': 'BMW',
    'modelis': 'M5',
    'metai': 2022,
    'spalva': 'Mėlyna',
    'variklis': 'Dyzelis'
}
del automobiliai['1']
print("Automobilių skaičius žodyne:", len(automobiliai))
print("Ar žodyne yra Audi A6?", 'Audi A6' in [automobiliai[auto]['marke'] + ' ' + automobiliai[auto]['modelis'] for auto in automobiliai])
automobiliai.clear()
print("Išvalytas žodynas:", automobiliai)
```

Rezultatas:

```Text
Automobilis nr.2: {'marke': 'Tesla', 'modelis': 'Model S', 'metai': 2018, 'spalva': 'Raudona', 'variklis': 'Elektra'}
Automobilis nr.3 po variklio pakeitimo: {'marke': 'Ferrari', 'modelis': '488 GTB', 'metai': 2019, 'spalva': 'Geltona', 'variklis': 'Elektra'}
Automobilių skaičius žodyne: 3
Ar žodyne yra Audi A6? False
Išvalytas žodynas: {}
```

</details>