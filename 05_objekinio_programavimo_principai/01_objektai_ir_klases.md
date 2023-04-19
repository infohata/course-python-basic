# Objektinis programavimas

Objektinis programavimas (`OOP`) yra programavimo paradigma, kuri leidžia kurti programas, kurios yra suskirstytos į mažus savarankiškus modulius, vadinamus objektais. Objektai gali turėti savo būseną (savybes) ir elgesį (metodus). Šios savybės ir metodai yra apibrėžiami kaip klasės, kuri yra objekto "šablonas".

## Klasės sukūrimas

Klasės deklaracija yra paprasta - reikia naudoti `class` žodį, o po to klasės pavadinimą. Pvz.:

```Python
class Automobilis:
    marke = ''
    modelis = ''
    metai = ''
    spalva = ''
```

## Objekto sukūrimas

Norėdami sukurti naują objektą pagal esamą klasę, turime perduoti reikiamus argumentus:

```Python
pirmas_automobilis = Automobilis()
pirmas_automobilis.marke = 'Audi'
pirmas_automobilis.modelis = 'A6'
pirmas_automobilis.metai = 2019
pirmas_automobilis.spalva = 'balta'
```

Dabar `pirmas_automobilis` kintamasis yra objektas, kuris saugo duomenis apie automobilį pagal mūsų nurodytus parametrus. Galime pasiekti objekto atributus:

```Python
print(pirmas_automobilis.marke)  # Audi
print(pirmas_automobilis.modelis)  # A6
print(pirmas_automobilis.metai)  # 2019
print(pirmas_automobilis.spalva) # balta
```

## Savybių pakeitimas

Objekto savybes galima pakeisti priskiriant naują reikšmę objekto kintamajam, pvz.:

```Python
pirmas_automobilis.metai = 2015

print(pirmas_automobilis.metai) # 2015
```

## Savybės pagal nutylėjimą

Savybė pagal nutylėjimą yra klasės atributas, kuriam yra priskirta numatyta reikšmė, kuri bus naudojama, jei objektui nėra priskirta jokia kita reikšmė. Galime pakeisti automobilio klasę, pvz.:

```Python
class Automobilis:
    marke = ''
    modelis = ''
    metai = 2023
    spalva = 'pilka'

antras_automobilis = Automobilis()
antras_automobilis.marke = 'BMW'
antras_automobilis.modelis = 'X5'
antras_automobilis.metai = 2001
print(antras_automobilis.metai) # 2021
print(antras_automobilis.spalva) # pilka
```

## Skirtingas kiekis savybių

Klasės, kurios objektai gali būti inicijuoti su skirtingu kiekiu savybių, yra naudingos tuo atveju, kai norime suteikti vartotojui galimybę nurodyti tik dalį objekto savybių, o likusios savybės būtų priskiriamos pagal nutylėjimą, pvz.:

```Python
print(pirmas_automobilis.marke, pirmas_automobilis.spalva) # Audi balta
print(antras_automobilis.marke, antras_automobilis.spalva) # BMW pilka
```

## Objekto metodai

Metodas yra funkcija, apibrėžta klasės viduje. Norint sukurti metodą, reikia jį apibrėžti kaip funkciją ir pridėti prie klasės:

```Python
class Automobilis:
    marke = ''
    modelis = ''
    metai = 2023
    spalva = 'pilka'

    def vaziuoti(self):
        print('Važiuoja')

    def pypseti(self, zinute='Pyp', kiekis=1):
        print(zinute * kiekis)

antras_automobilis.vaziuoti() # Važiuoja
antras_automobilis.pypseti() # Pyp
antras_automobilis.pypseti('Pyyyp ', 3) # Pyyyp Pyyyp Pyyyp
```

## `init` konstruktorius

Jeigu norite, kad klasę naudoti būtų daug lanksčiau, galite naudoti `init` konstruktorių. `__init__` yra specialus metodas, kuris kviečiamas, kai sukuriamas naujas objektas pagal klasę. Galima perrašyti jau turimą klasę, pvz.:

```Python
class Automobilis:
    def __init__(self, marke, modelis, metai=2023, spalva='pilka'):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai
        self.spalva = spalva
```

Konstruktorius `__init__` privalo turėti parametrą `self`, nes jis nurodo, kad savybės yra susijusios su objektu, kuris bus sukuriamas iš šios klasės.

Žinodami klasės konstruktorių, galime lengvai sukurti naują objektą tiesiog nustatant norimas reikšmes, pvz.:

```Python
trecias_automobilis = Automobilis('Mercedes', 'C-Class', 2021, 'geltona')
print(trecias_automobilis.marke)  # Mercedes
print(trecias_automobilis.modelis)  # C-Class
print(trecias_automobilis.metai)  # 2021
print(trecias_automobilis.spalva) # geltona
```

## Metodai su skirtingu kiekiu savybių, *args, **kwargs

Galima apibrėžti metodus su skirtingu kiekiu argumentų. Tam galima naudoti `*args` arba `**kwargs` sintaksę.

`*args` naudojami, kai norime perduoti nežinomą skaičių argumentų į metodą, pvz.:

```Python
class Automobilis:
    def __init__(self, marke, modelis, *args):
        self.marke = marke
        self.modelis = modelis
        self.papildomi = args

    def isvesti_papildomus(self):
        print(self.papildomi)

automobilis = Automobilis('Audi', 'A4', '2022', 'Juoda', 'Automatinė', 'GPS')
automobilis.isvesti_papildomus() # ('2022', 'Juoda', 'Automatinė', 'GPS')
```

`**kwargs` naudojami, kai norime perduoti nežinomą skaičių argumentų su raktų-vardinių argumentų poromis:

```Python
class Automobilis:
    def __init__(self, marke, modelis, **kwargs):
        self.marke = marke
        self.modelis = modelis
        self.papildomi = kwargs

    def isvesti_papildomus(self):
        print(self.papildomi)

automobilis = Automobilis('Audi', 'A4', metai=2022, spalva='Juoda', transmisija='Automatinė', gps=True)
automobilis.isvesti_papildomus() # {'metai': 2022, 'spalva': 'Juoda', 'transmisija': 'Automatinė', 'gps': True}
```

## Kaip pakeisti objekto spausdinimą

Objektų spausdinimui galima naudoti `__str__` metodą, kuris yra skirtas gražinti objekto stringo reprezentaciją. Šis metodas kviečiamas, kai objektas yra spausdinamas arba naudojamas kaip stringo argumentas. Jei `__str__` metodas neaprašytas klasėje, naudojamas numatytasis metodas, kuris tiesiog spausdina objekto klasės pavadinimą ir jo atminties vietą:

```Python
print(antras_automobilis) # <__main__.Automobilis object at 0x7fdfc8347e80>
```

Aprašius `__str__` metodą gauname aiškesnę objekto informaciją:

```Python
class Automobilis:
    def __init__(self, marke, modelis, metai=2023, spalva='pilka'):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai
        self.spalva = spalva

    def __str__(self):
        return f'{self.marke} {self.modelis}: {self.metai} metai, spalva {self.spalva}'

antras_automobilis = Automobilis("BMW", "X5", 2021)

print(antras_automobilis) # BMW X5: 2021 metai, spalva pilka
```

## Simbolių eilutė kaip objektas

Simbolių eilutė (`string`) reprezentuoja tekstinę informaciją ir gali būti apdorojama bei manipuliuojama įvairiais būdais, naudojant metodus ir funkcijas. Pvz.:

```Python
pasisveikinimas = 'Sveikas, pasauli'
```

Kaip bet kuris kitas objektas, string gali būti atvaizduotas naudojant `type()` funkciją:

```Python
print(type(pasisveikinimas)) # <class 'str'>
```

Taip pat galime patikrinti string objekto atminties vietą naudodami `id()` funkciją:

```Python
print(id(pasisveikinimas)) # 139804279643856
```

Galime suskaidyti teksto eilutę į atskirus žodžius, naudojant `split()` metodą:

```Python
print(pasisveikinimas.split()) # ['Sveikas,', 'pasauli']
```

Galime paversti string objektą didžiosiomis raidėmis, naudodami `upper()` metodą:

```Python
print(pasisveikinimas.upper()) # SVEIKAS, PASAULI
```

String objektai yra nuoseklūs, jų simboliai yra tvarkomi kaip seka. Galime pasiekti atskirus string simbolius indeksuojant simbolių eilutę:

```Python
print(pasisveikinimas[0]) # S
print(pasisveikinimas[9]) # p
```

## Objektai sąraše ar žodyne

Klasės objektai gali būti saugomi ne tik kaip atskiri kintamieji, bet ir kaip sąrašo ar žodyno elementai. Tai gali būti naudinga, jei reikia apdoroti daug objektų ir juos tvarkingai organizuoti.

Objektų saugojimas ir iteravimas sąraše:

```Python
automobiliai = []

pirmas_automobilis = Automobilis('Audi', 'A6', 2019, 'balta')
antras_automobilis = Automobilis("BMW", "X5", 2021)
ketvirtas_automobilis = Automobilis('Volkswagen', 'Golf')

automobiliai.append(pirmas_automobilis)
automobiliai.append(antras_automobilis)
automobiliai.append(ketvirtas_automobilis)

for automobilis in automobiliai:
    print(automobilis)
```

Rezultatas:

```Text
Audi A6: 2019 metai, spalva balta
BMW X5: 2021 metai, spalva pilka
Volkswagen Golf: 2023 metai, spalva pilka
```

Objektus taip pat galime saugoti žodyne, jei norime prieinamumo pagal raktą, pvz.:

```Python
automobiliai = {}

automobiliai['Petras'] = Automobilis('Toyota', 'Corolla', 2022, 'raudona')
automobiliai['Jonas'] = Automobilis('Volkswagen', 'Golf')
automobiliai['Anatanas'] = Automobilis('Audi', 'A6', spalva='balta')

for savininkas, automobilis in automobiliai.items():
    print(f"{savininkas}: {automobilis}")
```

Rezultatas:

```Text
Petras: Toyota Corolla: 2022 metai, spalva raudona
Jonas: Volkswagen Golf: 2023 metai, spalva pilka
Anatanas: Audi A6: 2023 metai, spalva balta
```

## Užduotys

### Pirma užduotis

- Sukurti naują klasę Darbuotojas, turinčią savybes vardas, pavardė, pareigos ir atlyginimas (su numatyta minimalia alga)
- Sukurti naują objektą darbuotojas
- Atspausdinkite darbuotojo pareigas ir atlyginimą.
- Pakeisti darbuotojo atlyginimą.
- Atspausdinkite pilną darbuotojo informaciją.

### Antra užduotis

- Sukurkite klasę "Gyvūnas" su savybėmis: vardas, amžius ir svoris.
- Sukurkite `__str__` metodą patogiam informacijos apie gyvūną grąžinimui
- Sukurkite metodus padidinti ir sumažinti svorį.
- Sukurkite metodą `gimtadienis`, padidinantį amžių.
- Sukurkite objektą su jūsų pasirinktomis reikšmėmis.
- Atspausdinkite objektą.
- Pakeiskite kelis kartus gyvūno svorį ir amžių naudojant sukurtus metodus ir po kiekvieno pakeitimo atspausdinkite.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos, atlyginimas=1000):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas

    def __str__(self):
        return f'{self.vardas} {self.pavarde}, pareigos: {self.pareigos}, atlyginimas: {self.atlyginimas}'

darbuotojas = Darbuotojas('Jonas', 'Jonaitis', 'Programuotojas', 2000)

print('Darbuotojo pareigos:', darbuotojas.pareigos)
print('Darbuotojo atlyginimas:', darbuotojas.atlyginimas)

darbuotojas.atlyginimas = 2500

print('Darbuotojas:', darbuotojas)
```

Rezultatas:

```Text
Darbuotojo pareigos: Programuotojas
Darbuotojo atlyginimas: 2000
Darbuotojas: Jonas Jonaitis, pareigos: Programuotojas, atlyginimas: 2500
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
class Gyvunas:
    def __init__(self, vardas, amzius, svoris):
        self.vardas = vardas
        self.amzius = amzius
        self.svoris = svoris
    
    def padidinti_svori(self, kiek):
        self.svoris += kiek
    
    def sumazinti_svori(self, kiek):
        self.svoris -= kiek

    def gimtadienis(self):
        self.amzius += 1
        
    def __str__(self):
        return f'Gyvūnas vardu {self.vardas} yra {self.amzius} metų ir sveria {self.svoris} kg'

gyvunas = Gyvunas('Reksas', 5, 20)
print(gyvunas)

gyvunas.padidinti_svori(5)
print(gyvunas)

gyvunas.gimtadienis()
print(gyvunas)

gyvunas.sumazinti_svori(3)
print(gyvunas)
```

Rezultatas:

```Text
Gyvūnas vardu Reksas yra 5 metų ir sveria 20 kg
Gyvūnas vardu Reksas yra 5 metų ir sveria 25 kg
Gyvūnas vardu Reksas yra 6 metų ir sveria 25 kg
Gyvūnas vardu Reksas yra 6 metų ir sveria 22 kg
```

</details>
</details>
