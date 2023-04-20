# Abstrakcija

Abstrakcija leidžia apibrėžti klasę, jos atributus ir metodus taip, kad juos būtų galima perpanaudoti, siekiant išvengti kodo kartojimosi ir mažinti kompleksiškumą.

## Vidinis panaudojimas

```Python
class Automobilis:
    def __init__(self, marke, modelis, metai=2023, spalva='pilka'):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai
        self.spalva = spalva
        self.max_greitis = 200
        self.__greitis = 0

    # šį privatų abstraktų metodą panaudosime keliose vietose
    def __keisti_greiti(self, greitis):
        if greitis > self.max_greitis:
            greitis = self.max_greitis
        if greitis < -10:
            greitis = -10
        self.__greitis = greitis
        return greitis

    # šį viešą abstraktų metodą irgi panaudosime keliose vietose
    def vaziuoti(self):
        greitis = self.__greitis
        if greitis > 0:
            print(f"važiuoju {self.__greitis} km/h greičiu")
        elif greitis < 0:
            print(f"važiuoju {abs(self.__greitis)} km/h greičiu atgal")
        else:
            print("stoviu")

    def didinti_greiti(self, pagreitis=10):
        # panaudojame privatų metodą maksimalaus greičio ribojimui
        self.__keisti_greiti(self.__greitis + pagreitis)
        # panaudojame vieša metodą važiavimo situacijai išvesti
        self.vaziuoti()

    def mazinti_greiti(self, pagreitis=10):
        # panaudojame privatų metodą maksimalaus greičio ribojimui
        self.__keisti_greiti(self.__greitis - pagreitis)
        # panaudojame vieša metodą važiavimo situacijai išvesti
        self.vaziuoti()
    

guolis = Automobilis("Volkswagen", "Golf")
print(guolis.marke, guolis.modelis, guolis.metai, guolis.spalva)
guolis.vaziuoti()
guolis.didinti_greiti()
guolis.didinti_greiti()
guolis.didinti_greiti(20)
guolis.didinti_greiti(170)
guolis.mazinti_greiti(100)
guolis.mazinti_greiti(50)
guolis.mazinti_greiti(50)
guolis.mazinti_greiti()
guolis.didinti_greiti()
```

Rezultatas

```Text
Volkswagen Golf 2023 pilka
stoviu
važiuoju 10 km/h greičiu
važiuoju 20 km/h greičiu
važiuoju 40 km/h greičiu
važiuoju 200 km/h greičiu
važiuoju 100 km/h greičiu
važiuoju 50 km/h greičiu
stoviu
važiuoju 10 km/h greičiu atgal
stoviu
```

## Abstrakčių savybių ir metodų panaudojimas paveldėtose klasėse

Pavyzdys - paveldėtose funkcijose mes visus metodus tiesiog naudojame:

```Python
class Elektromobilis(Automobilis):
    pass


tesla = Elektromobilis("Tesla", "Model-3")
print(tesla.marke, tesla.modelis, tesla.metai, tesla.spalva) # Tesla Model 3 2023 pilka
tesla.vaziuoti() # stoviu
tesla.didinti_greiti(100) # važiuoju 100 km/h greičiu
```

## Abstraktus `__init__` metodas su neribotais raktiniais argumentais

```Python
class Automobilis:
    def __init__(self, marke, modelis, metai=2023, spalva='pilka', **kwargs):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai
        self.spalva = spalva
        self.max_greitis = 200
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.__greitis = 0

guolis = Automobilis("Volkswagen", "Golf", kuro_tipas="benzinas", variklis="1.6ti")
print(f"{guolis.marke} {guolis.modelis}, {guolis.metai} m. {guolis.spalva}. Variklis: {guolis.variklis} {guolis.kuro_tipas}. Max. {guolis.max_greitis} km/h")
# Volkswagen Golf, 2023 m. pilka. Variklis: 1.6ti benzinas. Max. 200 km/h
astra = Automobilis("Opel", "Astra", kuro_tipas="benzinas", variklis="1.6", max_greitis=160)
print(f"{astra.marke} {astra.modelis}, {astra.metai} m. {astra.spalva}. Variklis: {astra.variklis} {astra.kuro_tipas}. Max. {astra.max_greitis} km/h")
# Opel Astra, 2023 m. pilka. Variklis: 1.6 benzinas. Max. 160 km/h
```

Čia atkreipkite dėmesį, kad numatytą reikšmę galima pakeisti per kwargs, jeigu kwargs apdorojimas vyksta po numatytos reikšmės nustatymo.

## Abstrakti funkcija informacijos apie klasės objektą spausdinimui

```Python
def informacija(obj):
    print(f"{obj.marke} {obj.modelis}, {obj.metai} m. {obj.spalva}. Variklis: {obj.variklis} {obj.kuro_tipas}. Max. {obj.max_greitis} km/h")    

informacija(guolis)
informacija(astra)
```

Rezultatas:

```Text
Volkswagen Golf, 2023 m. pilka. Variklis: 1.6ti benzinas. Max. 200 km/h
Opel Astra, 2023 m. pilka. Variklis: 1.6 benzinas. Max. 160 km/h
```

## Užduotys

### Pirma užduotis

- Parašykite klasę "Baseinas", kuri saugo informaciją apie vandens talpą ir dabartinį kiekį baseine.
- Klasė turi turėti metodus vandens papildymui ir nuleidimui bei esamo vandens kiekio patikrinimui. Vandens kiekio keitimui panaudokite abstraktų metodą.
- Sukurkite objektą ir kelis kartus iškvieskite klasės metodus.


## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
class Baseinas:

    def __init__(self, talpa, dabartinis_kiekis):
        self.__talpa = talpa
        self.__dabartinis_kiekis = dabartinis_kiekis

    def __keitimas(self, kiekis):
        self.__dabartinis_kiekis += kiekis

    def ipilti_vandens(self, kiekis):
        if self.__dabartinis_kiekis + kiekis <= self.__talpa:
            self.__keitimas(kiekis)
            print(f'Įpilta {kiekis} L vandens')
        else:
            print(f'Negalima įpilti {kiekis} L vandens, nes viršytų talpą')

    def nuleisti_vandeni(self, kiekis):
        if self.__dabartinis_kiekis - kiekis >= 0:
            self.__keitimas(-kiekis)
            print(f'Išpilta {kiekis} L vandens')
        else:
            print(
                f'Negalima išpilti {kiekis} L vandens, nes dabar yra tik {self.__dabartinis_kiekis} L'
            )

    def get_talpa(self):
        return self.__talpa
  
    def get_dabartinis_kiekis(self):
        return self.__dabartinis_kiekis


baseinas = Baseinas(1000, 300)
print(f'Baseino talpa: {baseinas.get_talpa()} L, šiuo metu baseinas užpildytas: {baseinas.get_dabartinis_kiekis()} L')

baseinas.nuleisti_vandeni(50)
baseinas.ipilti_vandens(480)
print(baseinas.get_dabartinis_kiekis())
```

Rezultatas:

```Text
Baseino talpa: 1000 L, šiuo metu baseinas užpildytas: 300 L
Išpilta 50 litrų vandens
Įpilta 480 litrų vandens
730
```
