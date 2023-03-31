# Neriboti argumentai *args, **kwargs

`*args` yra specialus Python sintaksės elementas, kuris leidžia perduoti bet kokį kiekį pozicinių argumentų į funkciją. `*args` sukuria `tuple` iš visų perduotų pozicinių argumentų, kurie gali būti naudojami kaip bet kuris kitas `tuple`.

Pavyzdys:

```Python
def spausdinti_args(*args):
    for arg in args:
        print(arg)

spausdinti_args(1, 2, 3, "Labas", "Pasauli")
```

Šis kodas išvestų:

```Python
1
2
3
Labas
Pasauli
```

Sumavimo funkcijos pavyzdys su `*args`:

```Python
def suma(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(suma(1, 2, 3))  # 6
print(suma(4, 5, 6, 7))  # 22
```

Funkcija, kuri sujungia ir atspausdina visus *args elementus, pavyzdys:

```Python
def sujungti(*args):
    sujungtas = ""
    for arg in args:
        sujungtas += str(arg)
    print(sujungtas)

sujungti("Labas", " ", "Pasauli")  # Labas Pasauli
sujungti(1, 2, 3, 4)  # 1234
```

Funkcija, kuri grąžina visus perduotus *args elementus, kurie yra didesni nei nurodytas skaičius, pavyzdys:

```Python
def didesni(skaicius, *args):
    didesni_elementai = []
    for arg in args:
        if arg > skaicius:
            didesni_elementai.append(arg)
    return didesni_elementai

print(didesni(3, 1, 2, 3, 4, 5))  # [4, 5]
print(didesni(10, 1, 2, 3, 4, 5))  # []
```

Funkcija, kuri gražina *args elemento eilutės ilgį, pavyzdys:

```Python
def eilutes_ilgis(*args):
    ilgiai = []
    for arg in args:
        ilgis = len(str(arg))
        ilgiai.append(ilgis)
    return ilgiai

print(eilutes_ilgis("Labas", "Pasauli"))  # [5, 7]
print(eilutes_ilgis(123, 4567, 89))  # [3, 4, 2]
```

`**kwargs` yra dar viena speciali Python sintaksės elementas, kuris leidžia perduoti bet kokią raktą ir reikšmę funkcijai. `**kwargs` sukuria žodyną, kuriame raktai yra perduoti raktai ir reikšmės yra perduotos reikšmės.

Pavyzdys:

```Python
def spausdinti_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

spausdinti_kwargs(vardas="Jonas", amzius=30, miestas="Vilnius")
```

Šis kodas išvestų:

```Python
vardas: Jonas
amzius: 30
miestas: Vilnius
```

Funkcija, kuri grąžina nurodyto elemento reikšmę, pavyzdys:

```Python
def reiksme(**kwargs):
    if "elementas" in kwargs:
        return kwargs["elementas"]
    else:
        return None

print(reiksme(vardas="Jonas", elementas="LAIKAS"))  # LAIKAS
print(reiksme(miestas="Vilnius", amzius=30))  # None
```

Funkcija, kuri sumuoja `**kwargs` elementų reikšmes, pavyzdys:

```Python
def suma_kwargs(**kwargs):
    suma = 0
    for value in kwargs.values():
        suma += value
    return suma

print(suma_kwargs(skaicius1=10, skaicius2=20, skaicius3=30))  # 60
print(suma_kwargs(amzius=20, dienos=365, valanda=60))  # 445
```

Kai kuriose situacijose reikia turėti funkciją, kuri priima tiek pozicinius argumentus, tiek ir argumentus, kurie nėra aprašyti funkcijos deklaracijoje. Tokios funkcijos gali būti sukurtos naudojant `*args` ir `**kwargs` kartu su paprastais argumentais.

Pavyzdys:

```Python
def spausdinti_argumentus(vardas, *args, **kwargs):
    print(f"Vardas: {vardas}")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

spausdinti_argumentus("Jonas", 1, 2, 3, miestas="Vilnius", amzius=30)
```

Šis kodas išvestų:

```Python
Vardas: Jonas
1
2
3
miestas: Vilnius
amzius: 30
```

Taigi, `*args` leidžia perduoti neribotą kiekį pozicinių argumentų, o `**kwargs` leidžia perduoti neribotą kiekį raktų ir reikšmių argumentų. Galima kombinuoti šiuos elementus su įprastais argumentais funkcijose, kad būtų gautas didesnis funkcionalumas ir lankstumas.

## Užduotys

### Pirma užduotis

Parašykite funkciją, kuri grąžina didžiausią *args elemento reikšmę.

### Antra užduotis

Parašykite funkciją, kuri grąžina **kwargs elemento raktus, kurie yra nurodyti funkcijos kvietime, pavyzdžiui: 

```Python
print(raktai(vardas="Jonas", amzius=30, miestas="Vilnius", metai=2023))  


# kvietime galite nurodyti tik vardą, amžių bei miestą, kad grąžintų: {'vardas': 'Jonas', 'amzius': 30, 'miestas': 'Vilnius'}
```

### Trečia užduotis

Parašykite funkciją, kuri sujungia *args sąrašą ir **kwargs elementus į vieną sarašą.

### Ketvirta užduotis

Sukurkite funkciją, kuri iš sąrašo išrenka didžiausią skaičių ir grąžina jį.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
def didziausias(*args):
    if len(args) == 0:
        return None
    didziausia_reiksme = args[0]
    for arg in args:
        if arg > didziausia_reiksme:
            didziausia_reiksme = arg
    return didziausia_reiksme

print(didziausias(1, 2, 3, 4, 5))  # 5
print(didziausias(-5, 10, 3, -2))  # 10
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
def raktai(**kwargs):
    nurodyti_raktai = {}
    for key in kwargs:
        if key in ["vardas", "amzius", "miestas"]:
            nurodyti_raktai[key] = kwargs[key]
    return nurodyti_raktai

print(raktai(vardas="Jonas", amzius=30, miestas="Vilnius", metai=2023))  # {'vardas': 'Jonas', 'amzius': 30, 'miestas': 'Vilnius'}
print(raktai(pavadinimas="Python"))  # {}
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
def sujungtas_sarasas(*args, **kwargs):
    visi_elementai = list(args)
    visi_elementai += list(kwargs.values())
    return visi_elementai
```

</details>
</details>
