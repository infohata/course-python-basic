# Funkcija su grąžinama reikšme `return`

Funkcija su grąžinama reikšme (`return`) yra funkcija, kuri apdoroja tam tikrą įvestį ir grąžina rezultatą. Grąžinama reikšmė gali būti bet kokio tipo - skaičius, eilutė, sąrašas ar netgi kitas objektas. Grąžinti reikšmę iš funkcijos yra būtina, jei norite naudoti funkcijos apdorotus duomenis kitur programos eigoje.

Funkcija su grąžinama reikšme apibrėžiama `return` sakiniu. Grąžinama reikšmė nurodoma iš kart po `return`, o jei funkcija turi daugiau nei vieną grąžinamą reikšmę, jos gali būti grąžinamos per `tuple` arba sąrašą.

Pavyzdys, kaip apibrėžti funkciją, kuri grąžina skaičiaus kėlimą kvadratu:

```Python
def kvadratu(x):
    return x**2
```

Ši funkcija priima skaičių x kaip argumentą, kelia jį kvadratu ir grąžina gautą rezultatą.

Pavyzdys, kaip iškvieti funkciją ir gauti jos grąžinamą reikšmę:

```Python
rezultatas = kvadratu(5)
print(rezultatas)  # išvestų: 25
```

Šiame pavyzdyje funkcija kvadratu yra iškviesta su argumentu 5, o jos grąžinama reikšmė (25) yra priskirta kintamajam rezultatas, kuris vėliau yra išvestas naudojant print funkciją.

Dar vienas pavyzdys:

```Python
def suma(x, y):
    rezultatas = x + y
    return rezultatas

atsakymas = suma(10, 2)
print(atsakymas)  # išvestų: 12
```

Ši funkcija suma priima du argumentus: x ir y, tuomet juos sudeda ir grąžina sumą naudodama return sakinį.

## Daugiau negu vieno kintamojo grąžinimas per `tuple` arba sąrašą (`list`)

Norint grąžinti du kintamuosius, galima jų reikšmes sudėti į `tuple` ir grąžinti jį iš funkcijos, pavyzdžiui:

```Python
def skaiciu_suma_ir_sandauga(a, b):
    suma = a + b
    sandauga = a * b
    return (suma, sandauga)

rezultatas = skaiciu_suma_ir_sandauga(2, 3)
print(rezultatas)  # išvestų (5, 6)
```

Šiuo atveju `skaiciu_suma_ir_sandauga` funkcija grąžina du kintamuosius - suma ir sandauga, sudėtas į tuple. Tuomet rezultatas kintamasis priskiriamas tuple reikšmei, grąžintai iš funkcijos, ir išvedamas į ekraną.

Rezultatą taip pat galima priimti į skirtingus kintamuosius:

```Python
suma, sandauga = skaiciu_suma_ir_sandauga(2, 3)
print(suma)     # 5
print(sandauga) # 6
```

Taip pat galima grąžinti **sąrašą**:

```Python
def teigiami_ir_neigiami_skaiciai(skaiciai):
    teigiami = []
    neigiami = []
    for skaicius in skaiciai:
        if skaicius > 0:
            teigiami.append(skaicius)
        else:
            neigiami.append(skaicius)
    return [teigiami, neigiami]

skaiciai = [2, -4, 5, -1, -2]
rezultatas = teigiami_ir_neigiami_skaiciai(skaiciai)
print(rezultatas)  # išvestų [[2, 5], [-4, -1, -2]]
```

Šiuo atveju `teigiami_ir_neigiami_skaiciai` funkcija grąžina du sąrašus - `teigiami` ir `neigiami`, kuriuos sudaro atitinkamai teigiami ir neigiami skaičiai iš pradinio sąrašo. Tuomet rezultatas kintamasis priskiriamas sąrašo reikšmei, grąžintai iš funkcijos, ir išvedamas į ekraną.

❗ Svarbu atkreipti dėmesį, kad grąžinamas objektas turi būti išsaugotas kaip tuple arba sąrašas, kad galėtų būti naudojamas kaip toks, t.y. galima išgauti reikšmes su indeksavimu ar kitiems objektų manipuliacijoms, o ne kaip keli atskiri kintamieji. Taip pat galima naudoti ir žodyną `dict`.

## Užduotys

### Pirma užduotis

Sukurkite funkciją, kuri priima sąrašą ir grąžina naują sąrašą atvirkščia tvarka.

### Antra užduotis

Sukurkite funkciją, kuri apskaičiuoja trikampio plotą pagal kraštinių ilgius ir grąžina jį.

### Trečia užduotis

Sukurkite funkciją, kuri iš sąrašo išrenka žodžius, kurie yra nurodyto ilgio ir grąžina sąrašą su tais žodžiais.

### Ketvirta užduotis

Sukurkite funkciją, kuri iš sąrašo išrenka didžiausią skaičių ir grąžina jį.

### Penkta užduotis

Sukurti funkciją, kuri iš žodžių sąrašo išrenka žodžius, kurie prasideda nurodyta raide ir grąžina sąrašą su tais žodžiais.

### Šešta užduotis

Sukurkite funkciją, kuri iš eilutės išrenka visus žodžius, kurių ilgis yra lyginis, ir grąžina sąrašą su tais žodžiais.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
def sarasas_atvirksciai(sarasas):
    return sarasas[::-1]
```

Rezultatas:

```Python
>>> sarasas = [1, 2, 3, 4, 5]
>>> sarasas_atvirksciai(sarasas)
[5, 4, 3, 2, 1]
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

s = (a + b + c) / 2, kur a, b ir c yra trikampio kraštinių ilgiai

plotas = √(s * (s - a) * (s - b) * (s - c))

```Python
def trikampio_plotas(a, b, c):
    s = (a + b + c) / 2  # pusė perimetro
    plotas = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return plotas

a = 3
b = 4
c = 5
trikampio_plotas = trikampio_plotas(a, b, c)
print(trikampio_plotas)  # išvestų: 6.0
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
def rinkti_zodzius_pagal_ilgi(sakinys, ilgis):
    zodziai = sakinys.split()
    ilgio_zodziai = []
    for zodis in zodziai:
        if len(zodis) == ilgis:
            ilgio_zodziai.append(zodis)
    return ilgio_zodziai

sakinys = "Labas vakaras, kaip sekasi?"
ilgis = 7
zodziai = rinkti_zodzius_pagal_ilgi(sakinys, ilgis)
print(zodziai)  # išvestų: ['vakaras', 'sekasi?']
```

</details>
<details>
<summary>Ketvirta užduotis</summary>
<hr>

```Python
def didziausias_skaicius(skaiciai):
    didziausias = skaiciai[0]
    for skaicius in skaiciai:
        if skaicius > didziausias:
            didziausias = skaicius
    return didziausias

skaiciai = [4, 2, 7, 1, 9, 5]
didziausias = didziausias_skaicius(skaiciai)
print(didziausias)  # išvestų: 9
```

</details>

<details>
<summary>Penkta užduotis</summary>
<hr>

```Python
def rinkti_zodzius_pagal_raide(zodziai, raide):
    raides_zodziai = []
    for zodis in zodziai:
        if zodis[0] == raide:
            raides_zodziai.append(zodis)
    return raides_zodziai

zodziai = ["automobilis", "arklys", "avokadas", "bananas", "briedis"]
raide = "a"
a_zodziai = rinkti_zodzius_pagal_raide(zodziai, raide)
print(a_zodziai)  # išvestų: ['automobilis', 'avokadas']
```

</details>
<details>
<summary>Šešta užduotis</summary>
<hr>

```Python
def rinkti_lyginio_ilgio_zodzius(tekstas):
    zodziai = tekstas.split()
    lyginio_ilgio_zodziai = []
    for zodis in zodziai:
        if len(zodis) % 2 == 0:
            lyginio_ilgio_zodziai.append(zodis)
    return lyginio_ilgio_zodziai

tekstas = "Labas Vakare, kaip sekasi?"
lyginio_ilgio_zodziai = rinkti_lyginio_ilgio_zodzius(tekstas)
print(lyginio_ilgio_zodziai)  # išvestų: ['Vakare,', 'kaip']
```

</details>
</details>