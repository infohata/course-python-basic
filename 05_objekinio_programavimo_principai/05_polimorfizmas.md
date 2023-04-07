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

## Metodo iškvietimas

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
