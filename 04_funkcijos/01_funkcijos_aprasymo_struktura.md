# Funkcijos aprašymo struktūra

Deklaracijos sakinys `def` naudojamas apibrėžiant funkcijas Python programose. Funkcijų apibrėžimo sintaksė yra ši:

```Python
def funkcijos_pavadinimas(argumentas1, argumentas2, ...):
    # funkcijos veiksmų kodas
    # ...
```

Funkcijos pavadinimas yra pavadinimas, kuriuo vėliau galima naudoti funkciją iš kitų programos dalių. Argumentai yra reikšmės, kuriuos funkcija priima kaip įvestį, ir jie yra nurodyti tarp skliaustelių po funkcijos pavadinimu. Funkcija gali turėti bet kiek argumentų arba jų neturėti.

Pavyzdys, kaip apibrėžti funkciją, kuri priima du argumentus ir išspausdina juos į konsolę:

```Python
def spausdinti_duomenis(vardas, amzius):
    print("Vardas:", vardas)
    print("Amžius:", amzius)
```

Kai funkcija yra iškviečiama, argumentai yra perduodami funkcijai, kad ji galėtų atlikti savo veiksmus su jais. Pavyzdys, kaip iškviesti funkciją, kuri spausdina duomenis apie žmogų:

```Python
spausdinti_duomenis("Jonas", 25)
```

Spausdina

```Text
Vardas: Jonas
Amžius: 25
```

Šiame pavyzdyje du argumentai "Jonas" ir 25 perduodami funkcijai spausdinti_duomenis() kaip jos argumentai. Funkcija tiesiog išspausdina šiuos argumentus į konsolę, jos veikla neįtraukia reikšmės grąžinimo.

## `if`, `elif`, `else` funkcijoje

```Python
def skaiciaus_tipas(skaicius):
    if type(skaicius) == int:
        print("Įvestas skaičius yra sveikasis.")
    elif type(skaicius) == float:
        print("Įvestas skaičius yra trupmeninis.")
    else:
        print("Įvestas argumentas nėra skaičius.")
```

Šioje funkcijoje `if` sakinys patikrina, ar perduotas argumentas yra sveikasis skaičius, o `elif` sakinys patikrina, ar jis yra trupmeninis skaičius. Jei nei vienas iš šių sąlygų nėra tenkinamas, vykdomas `else` sakinys, kuris išveda klaidos pranešimą.

Šią funkciją galima iškviesti, pavyzdžiui, taip:

```Python
skaiciaus_tipas(10)
skaiciaus_tipas(3.14)
skaiciaus_tipas("a")
```

Tai išvestų:

```Python
Įvestas skaičius yra sveikasis.
Įvestas skaičius yra trupmeninis.
Įvestas argumentas nėra skaičius.
```

## Užduotys

### Pirma užduotis

Parašykite funkciją lyginis_nelyginis(skaicius), kuri patikrina, ar skaičius yra lyginis ar nelyginis ir išveda atitinkamą pranešimą.

### Antra užduotis

Parašykite funkciją ar_teigiamas(skaicius), kuri patikrina, ar skaičius yra teigiamas ir išveda atitinkamą pranešimą.

### Trečia užduotis

Parašykite funkciją ar_daugiau_nei(skaicius, riba), kuri patikrina, ar skaičius yra didesnis nei nurodyta riba ir išveda atitinkamą pranešimą.

# Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
  <summary>Pirma užduotis</summary>
  <hr>
  
```Python
def lyginis_nelyginis(skaicius):
    if skaicius % 2 == 0:
        print("Įvestas skaičius yra lyginis.")
    else:
        print("Įvestas skaičius yra nelyginis.")
```

</details>
<details>
  <summary>Antra užduotis</summary>
  <hr>

```Python
def ar_teigiamas(skaicius):
    if skaicius > 0:
        print("Įvestas skaičius yra teigiamas.")
    else:
        print("Įvestas skaičius nėra teigiamas.")
```

</details>
<details>
  <summary>Trečia užduotis</summary>
  <hr>

```Python
def ar_daugiau_nei(skaicius, riba):
    if skaicius > riba:
        print(f"Įvestas skaičius yra didesnis nei {riba}.")
    else:
        print(f"Įvestas skaičius nėra didesnis nei {riba}.")
```

</details>
</details>
