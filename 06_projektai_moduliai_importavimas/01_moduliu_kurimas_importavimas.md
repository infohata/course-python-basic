# Modulių kūrimas, importavimas

Modulis yra Python programavimo kalbos sąvoka, apibūdinanti vieną failą, kuriame yra Python kodas. Moduliai padeda organizuoti ir suskirstyti kodą į atskiras dalis pagal funkcionalumą, kad jis būtų lengviau suprantamas ir tvarkingas.

Tereikia sukurti naują Python failą (su .py plėtiniu) ir parašyti kodą jame. Pvz., sukūrę failą pavadinimu mano_modulis.py, mes sukuriame naują modulį, vadinamą mano_modulis.

Pavyzdys:

mano_modulis.py:

```Python
def pasisveikinti(vardas):
    return f"Sveikas, {vardas}!"

def sudetis(x, y):
    return x + y

class ManoKlase:
    def __init__(self, x):
        self.x = x

    def kvadratas(self):
        return self.x ** 2
```

Šiame pavyzdyje mes sukūrėme modulį mano_modulis, kuriame yra funkcijos pasisveikinti ir sudetis, taip pat klasė ManoKlase. Kad naudotume šio modulio funkcijas ir klases kitame faile, turime jį importuoti.

## Funkcijos arba klasės importavimas

Python leidžia importuoti konkrečias funkcijas ar klases iš modulių ar paketų. Tai padeda užtikrinti, kad importuojate tik tai, ko jums reikia, ir taip sumažinate atminties naudojimą.
Pavyzdys:

```Python
from mano_modulis import ManoKlase
from math import sqrt
```

💡 `math` modulis yra standartinė Python biblioteka, skirta matematikos funkcijoms ir konstantoms. Funkcija `sqrt` yra kvadratinės šaknies funkcija. Ji priima vieną skaičių kaip argumentą ir grąžina jo kvadratinę šaknį.

## Importuotų objektų pervadinimas su "as"

Kartais gali būti naudinga pervadinti importuotą objektą (modulį, funkciją ar klasę), kad jis būtų trumpesnis arba aiškesnis. Tai galima padaryti naudojant "as" raktažodį.
Pavyzdys:

```Python
import random as belenkas
from mano_modulis import IlgasKlasesPavadinimas as IKP
from calendar import isleap as ar_keliamieji
```

## Iš modulio importuojame viską su `*`

Python leidžia importuoti visus modulio ar paketo elementus naudojant `*`. Nors tai gali būti patogu, šis būdas gali sukelti pavadinimų konfliktus, jei keli moduliai turi elementų su vienodais pavadinimais.

Pavyzdys:

```Python
from math import *
```

## `dir()` funkcija

Python `dir()` funkcija grąžina sąrašą, kuriame yra modulio ar paketo narių pavadinimai. Tai gali būti naudinga norint sužinoti, ką galima importuoti iš modulio ar paketo.

Pavyzdys:

```Python
import math
print(dir(math))
```

## Paketai, subpaketai ir init.py failai

**Paketai** yra būdas organizuoti Python kodo modulius į struktūruotą hierarchiją. Paketai leidžia lengvai suskirstyti projekto funkcionalumą į susijusias dalis, taip padidinant kodo tvarką ir supratimą.

Python paketas yra paprastai direktorija, kurioje yra init.py failas. Paketas gali turėti modulius, subpaketus ir jų init.py failus.

**Subpaketai** yra paketų direktorijos, esančios kituose paketuose. Jie taip pat turi `__init__.py` failą ir gali turėti savo modulius bei kitus subpaketus.

**`__init__.py` failai** yra specialūs Python failai, kuriuos interpretatorius naudoja, kad nustatytų direktoriją kaip paketą ar subpaketą. init.py failai gali būti tušti arba turėti kodą, pvz., importuoti kai kuriuos modulius, priskirti kintamuosius arba apibrėžti funkcijas ir klases. Importuojant paketą, `__init__.py` failai yra visada paleidžiami.

### Paketų pavadinimų taisyklės

<!-- prašosi redagavimo -->
Vengti didžiųjų raidžių. Katalogai negali prasidėti skaičiais, negali turėti tarpų, nelotyniškų raidžių ir t.t. Gera logika naudoti kintamųjų pavadinimų sudarymo taisykles.

### Projekto pavyzdys

Įsivaizduokime, kad turime šią katalogų ir failų struktūrą:

```text
projektas/
    __init__.py
    main.py
    geometrija/
        __init__.py
        plotas.py
        perimetras.py
        dvimate/
            __init__.py
            apskritimas.py
            kvadratas.py
```

`projektas` yra pagrindinis paketas, kuris turi modulį `main.py` ir subpaketą `geometrija`. `geometrija` subpaketas turi modulius `plotas.py` ir `perimetras.py` bei subpaketą `dvimate`, kuris turi modulius `apskritimas.py` ir `kvadratas.py`. Atkreipkite dėmesį, kad `dvimate` vadinti `2D` būtų nors gal ir patogiau, bet negalima.

## Absoliutus importavimas

Absoliutus importavimas naudoja visą kelią nuo pagrindinio paketo arba modulio iki importuojamo elemento. Jis paprastai yra aiškesnis ir lengviau suprantamas.

Pavyzdys:

```Python
from projektas.geometrija.plotas import trikampio_plotas
```

## Reliatyvus importavimas

Reliatyvus importavimas naudoja taškus nurodyti paketų ar modulių hierarchiją atsižvelgiant į esamą vietą. Jis gali padėti išlaikyti perkeliamumą tarp projektų ir sumažinti kodo kartojimąsi.

Pavyzdys:

```Python
from .plotas import trikampio_plotas
```

## Importas iš projekto paketų

Importuojant modulius iš paketų ir subpaketų, naudojama taškinė sintaksė:

```Python
from projektas.geometrija.plotas import trikampio_plotas
from projektas.geometrija.dvimate.apskritimas import apskritimo_plotas
```

`init.py` failų panaudojimas:
Tarkime, kad `projektas/geometrija/__init__.py` failas turi šį kodą:

```Python
from .plotas import *
from .perimetras import *
from .dvimate.apskritimas import *
from .dvimate.kvadratas import *
```

Dabar galime importuoti visas funkcijas tiesiog importuodami `geometrija` subpaketą:

```Python
from projektas.geometrija import trikampio_plotas, apskritimo_plotas
```

## Užduotys

### Pirma užduotis

Sukurkite naują Python modulį, pavadinimu matematika.py, kuriame būtų šios funkcijos:

* daugyba(x, y): grąžina dviejų skaičių x ir y sandaugą
* dalyba(x, y): grąžina dviejų skaičių x ir y dalmenį

Tada importuokite šį modulį kitame Python faile ir panaudokite jo funkcijas skaičiavimams atlikti.

### Antra užduotis

Sukurkite paketą geometrija, kuris turėtų šiuos modulius:

* apskritimas.py: turintis funkciją apskritimo_plotas(r) skirtą apskaičiuoti apskritimo plotą
* kvadratas.py: turintis funkciją kvadrato_plotas(a) skirtą apskaičiuoti kvadrato plotą

Importuokite šiuos modulius kitame faile, pakeiskite funkcijų pavadinimus pasitelkiant `as` ir panaudokite funkcijas skaičiavimams atlikti.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
  <summary>Pirma užduotis</summary>
  <hr>
  
matematika.py

```Python
def daugyba(x, y):
    return x * y

def dalyba(x, y):
    if y != 0:
        return x / y
    else:
        return "Klaida: dalyba iš nulio negalima"
```

main.py

```Python
import matematika

print(matematika.daugyba(4, 5))
print(matematika.dalyba(10, 2))
```

</details>
<details>
  <summary>Antra užduotis</summary>
  <hr>

```Python
geometrija/
    __init__.py
    apskritimas.py
    kvadratas.py
```

apskritimas.py

```Python
def apskritimo_plotas(r):
    import math
    return math.pi * (r ** 2)
```

kvadratas.py

```Python
def kvadrato_plotas(a):
    return a * a
```

app.py

```Python
from geometrija.apskritimas import apskritimo_plotas as a_plotas
from geometrija.kvadratas import kvadrato_plotas as k_plotas

print(a_plotas(5))
print(k_plotas(4))
```

</details>
</details>
