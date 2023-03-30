# Žodynai

Žodynai yra viena iš pagrindinių Python duomenų struktūrų, kurias galima naudoti kaip raktų ir reikšmių porų kolekcijas. Kiekvienas raktas turi priskirtą reikšmę, kurią galima pasiekti naudojant šio rakto pavadinimą.

## Žodynų kūrimas

Žodynus galima sukurti naudojant laužtinius skliaustus `{}` ir atskyrus juos kableliais. Kiekvienas raktas ir reikšmė yra atskirti dvitaškiais. Pvz.:

```Python
zodynas = {'raktas1': 'reiksme1', 'raktas2': 'reiksme2'}
print(zodynas) # {'raktas1': 'reiksme1', 'raktas2': 'reiksme2'}
```

## Pridėti žodyno įrašą

Žodyno įrašo pridėjimui galima naudoti paprastą priskyrimo operatorių `=`. Pvz.:

```Python
zmones = {'Jonas': 24, 'Petras': 32}
zmones['Ona'] = 28
print(zmones) # {'Jonas': 24, 'Petras': 32, 'Ona': 28}
```

## Pasiekti konkretų žodyno įrašą

Norint pasiekti konkretų žodyno įrašą, reikia tiesiog nurodyti raktą:

```Python
zmones = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
print(zmones['Petras']) # 32
print(zmones['Ona']) # 28
```

## Pakeisti konkretų žodyno įrašą

Norint pakeisti žodyno įrašą, reikia nurodyti jau esamą raktą ir priskirti naują reikšmę, kuri bus priskirta tam pačiam raktui:

```Python
zmones = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
zmones['Petras'] = 33
print(zmones) # {'Jonas': 24, 'Petras': 33, 'Ona': 28}
```

## Ištrinti konkretų žodyno įrašą

Norint ištrinti žodyno įrašą, reikia naudoti `del` komandą su raktu, kurio reikšmės norime ištrinti iš žodyno.

```Python
zmones = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
del zmones['Ona']
print(zmones) # {'Jonas': 24, 'Petras': 32}
```

## Žodynų metodai

Žodynų metodai leidžia atlikti veiksmus su žodynu ir manipuliuoti jo turiniu. Štai keletas dažniausiai naudojamų metodų:

`keys()` grąžina visus žodyno raktažodžius.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
raktažodžiai = zodynas.keys()
print(raktažodžiai) # dict_keys(['Jonas', 'Petras', 'Ona'])
```

`values()` grąžina visas žodyno reikšmes.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
reiksmes = zodynas.values()
print(reiksmes) # dict_values([24, 32, 28])
```

`items()` grąžina visus žodyno raktažodžius ir reikšmes kaip poras.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
poros = zodynas.items()
print(poros) # dict_items([('Jonas', 24), ('Petras', 32), ('Ona', 28)])
```

`get()` grąžina reikšmę, atitinkančią nurodytą raktą. Jei raktas nerastas, grąžina numatytąją reikšmę arba `None`.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
reiksme = zodynas.get('Jonas')
print(reiksme) # 24
```

`pop()` pašalina ir grąžina reikšmę, atitinkančią nurodytą raktą. Jei raktas nerastas, grąžina numatytąją reikšmę arba išmeta klaidą.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
reiksme = zodynas.pop('Petras')
print(reiksme) # 32
print(zodynas) # {'Jonas': 24, 'Ona': 28}
```

`clear()` išvalo žodyno turinį.

```Python
zodynas = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
zodynas.clear()
print(zodynas) # {}
```

# Užduotys

- Sukurkite tuščią žodyną pavadinimu "automobiliai".
- Pridėkite prie žodyno informaciją apie 3 skirtingus automobilius (nebijokite naudoti savo kūrybiškumo ir įtraukti įvairių markių, modelių, metų, spalvų ir variklių tipų).
- Išveskite žodyno informaciją apie vieną iš automobilių.
- Pakeiskite informaciją apie vieną automobilį (pavyzdžiui, pakeiskite variklio tipą).
- Pridėkite naują automobilį į žodyną.
- Pašalinkite informaciją apie vieną automobilį iš žodyno.
- Išveskite kiek yra automobilių žodyne.
- Patikrinkite ar tam tikras automobilis yra žodyne.
- Išvalykite žodyną.

## Atsakymai į užduotis

<details><summary>❗ Rodyti atsakymus</summary>
<hr>

```Python
automobiliai = {}
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