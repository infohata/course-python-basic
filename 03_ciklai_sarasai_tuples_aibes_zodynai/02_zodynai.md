# Žodynai

Žodynai yra viena iš pagrindinių Python duomenų struktūrų, kurias galima naudoti kaip raktų ir reikšmių porų kolekcijas. Kiekvienas raktas turi priskirtą reikšmę, kurią galima pasiekti naudojant šio rakto pavadinimą.

<br>

## Žodynų kūrimas

Žodynus galima sukurti naudojant laužtinius skliaustus `{}` ir atskyrus juos kableliais. Kiekvienas raktas ir reikšmė yra atskirti dvitaškiais. Pvz.:

```Python
zodynas = {'raktas1': 'reiksme1', 'raktas2': 'reiksme2'}
print(zodynas) # {'raktas1': 'reiksme1', 'raktas2': 'reiksme2'}
```

<br>

## Pridėti žodyno įrašą

Žodyno įrašo pridėjimui galima naudoti paprastą priskyrimo operatorių `=`. Pvz.:

```Python
zmones = {'Jonas': 24, 'Petras': 32}
zmones['Ona'] = 28
print(zmones) # {'Jonas': 24, 'Petras': 32, 'Ona': 28}

```

<br>

## Pasiekti konkretų žodyno įrašą

Norint pasiekti konkretų žodyno įrašą, reikia tiesiog nurodyti raktą:

```Python
zmones = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
print(zmones['Petras']) # 32
print(zmones['Ona']) # 28
```

<br>

## Pakeisti konkretų žodyno įrašą

Norint pakeisti žodyno įrašą, reikia nurodyti jau esamą raktą ir priskirti naują reikšmę, kuri bus priskirta tam pačiam raktui:

```Python
zmones = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
zmones['Petras'] = 33
print(zmones) # {'Jonas': 24, 'Petras': 33, 'Ona': 28}

```

<br>

## Ištrinti konkretų žodyno įrašą

Norint ištrinti žodyno įrašą, reikia naudoti `del` komandą su raktu, kurio reikšmės norime ištrinti iš žodyno.

```Python
zmones = {'Jonas': 24, 'Petras': 32, 'Ona': 28}
del zmones['Ona']
print(zmones) # {'Jonas': 24, 'Petras': 32}
```

<br>

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

<br>

# Užduotys