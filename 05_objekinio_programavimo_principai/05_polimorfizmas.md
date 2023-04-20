# Polimorfizmas

Polimorfizmas yra vienas iš objektinio programavimo principų, kuris leidžia vienai funkcijai ar metodui veikti su skirtingais objektais. Tai reiškia, kad keli objektai gali būti naudojami taip pat, nors jie turi skirtingus tipus arba implementacijas.

Polimorfizmas padeda padidinti programos lankstumą, patogumą ir tvarkingumą, nes kodas yra daug lengviau pritaikomas pokyčiams.

## Metodo perrašymas

Metodo perrašymasa yra galimybė perrašyti tėvinių klasės metodą paveldėtoje klasėje ir suteikti jam naują implementaciją. Tai yra galima dėl to, kad paveldėtoje klasėje jau yra aprašytas tėvinės klasės metodas su tokiu pat pavadinimu.

Metodų perrašymas leidžia mums turėti specializuotas klases, kurios gali keisti arba praplėsti tėvinės klasės funkcionalumą, nepakeičiant tėvinės klasės. Metodas paveldėtoje klasėje gali turėti ir papildomų argumentų, kurie nėra būtini tėvinėje klasėje.

```Python
class Automobilis:
    def __init__(self, marke, modelis):
        self.marke = marke
        self.modelis = modelis

    def greitis(self):
        print('Šis automobilis važiuoja leistinu greičiu')


class SportinisAutomobilis(Automobilis):
    def greitis(self):
        print('Šis automobilis gali važiuoti iki 300 km/h')


class IstorinisAutomobilis(Automobilis):
    def greitis(self):
        print('Šis automobilis gali važiuoti iki 100 km/h')


def informacija(automobilis):
    automobilis.greitis()
```

Iškvietę sukurtą funkciją su skirtingoms klasės priklausančiais objektais, gausime skirtingą rezultatą:

```Python
ferrari = SportinisAutomobilis('Ferrari', '458 Italia')
ford = IstorinisAutomobilis('Ford', 'Model T')
audi = Automobilis("Audi", "A4")

informacija(ferrari) # Šis automobilis gali važiuoti iki 300 km/h
informacija(ford) # Šis automobilis gali važiuoti iki 100 km/h
informacija(audi) # Šis automobilis važiuoja leistinu greičiu
```

## Paveldėto metodo iškvietimas

Kai norite panaudoti paveldėtus tėvinės klasės metodus ir savybes, tačiau tuo pat metu norite pakeisti jų veikimą naudojama `super()` funkcija. Tai leidžia mums išlaikyti tėvinės klasės funkcionalumą, tuo pat metu pridedant savo papildomą funkcionalumą. Pvz.:

```Python
class Automobilis:
    def __init__(self, marke, modelis):
        self.marke = marke
        self.modelis = modelis

    def greitis(self):
        print('Šis automobilis važiuoja leistinu greičiu')


class SportinisAutomobilis(Automobilis):
    def greitis(self):
        super().greitis()
        print('Šis automobilis gali važiuoti iki 300 km/h')


def informacija(automobilis):
    automobilis.greitis()
```

Iškvietę sukurtą funkciją su objektu, kuris paveldi tėvinės klasės metodą, gausime toki rezultatą:

```Python
ferrari = SportinisAutomobilis('Ferrari', '458 Italia')

informacija(ferrari)    # Šis automobilis važiuoja leistinu greičiu
                        # Šis automobilis gali važiuoti iki 300 km/h
```

## Užduotys

### Pirma užduotis

- Sukurkite darbuotojų klasę su savybėmis vardas, pavarde ir atlyginimas, kuri turėtų metodą atspausdinantį darbuotojo informaciją.
- Sukurkite administratoriaus klasę, kuri paveldėtų savybes iš darbuotojo klasės.
- Sukurkite vadovo klasę, kuri paveldėtų savybes iš darbuotojo klasės ir turėtų papildomą savybę "premija" bei metodą, kuris atspausdins papildytą darbuotojo informaciją.
- Sukurkite kelis kiekvienos klasės objektus ir iškvieskite informacijos spausdinimo metodą.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas=1000):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atlyginimas = atlyginimas

    def info(self):
        print(f'---\n{self.vardas} {self.pavarde}, atlyginimas: {self.atlyginimas} €')


class Administratorius(Darbuotojas):
    pass


class Vadovas(Darbuotojas):
    def __init__(self, vardas, pavarde, atlyginimas=2000, premija=0):
        super().__init__(vardas, pavarde, atlyginimas)
        self.premija = premija

    def info(self):
        super().info()
        print(f'Premija: {self.premija} €')


darbuotojas1 = Darbuotojas('Jonas', 'Jonaitis')
darbuotojas2 = Darbuotojas('Petras', 'Petraitis', 1200)
darbuotojas3 = Administratorius('Juozas', 'Juozaitis', 900)
vadovas1 = Vadovas('Antanas', 'Antanaitis', premija=500)

darbuotojai = [darbuotojas1, darbuotojas2, darbuotojas3, vadovas1]

for darbuotojas in darbuotojai:
    darbuotojas.info()
```

Rezultatas:

```Text
---
Jonas Jonaitis, atlyginimas: 1000 €
---
Petras Petraitis, atlyginimas: 1200 €
---
Juozas Juozaitis, atlyginimas: 900 €
---
Antanas Antanaitis, atlyginimas: 2000 €
Premija: 500 €
```

</details>
</details>
