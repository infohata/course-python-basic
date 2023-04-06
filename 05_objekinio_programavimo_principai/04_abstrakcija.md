# Abstrakcija

Abstrakcija leidžia apibrėžti klasę ir jos metodus taip, kad jie būtų paprasti naudoti, siekiant paslėpti sudėtingumą ir sudaryti galimybę perrašyti funkcionalumą atsižvelgiant į konkrečią situaciją. Pavyzdžiui sukuriame abstraktų metodą, kuris apibrėžiamas klasėje kaip neimplementuotas metodas (`pass`):

```Python
class Automobilis:
    def __init__(self, marke, modelis, metai=2023, spalva='pilka'):
        self.marke = marke
        self.modelis = modelis
        self.__metai = metai
        self.__spalva = spalva

    def __greitis(self):
        pass
```

Neimplementuotas metodas gali būti perrašytas kiekvienoje išvestinėje klasėje pagal konkretų poreikį:

```Python
class SportinisAutomobilis(Automobilis):
    def greitis(self):
        print('Šis automobilis gali važiuoti iki 300 km/h')


class IstorinisAutomobilis(Automobilis):
    def greitis(self):
        print('Šis automobilis gali važiuoti iki 100 km/h')

ferrari = SportinisAutomobilis('Ferrari', '458 Italia', metai=2021, spalva='raudona')
ford = IstorinisAutomobilis('Ford', 'Model T', 1927, spalva='juoda')

ferrari.greitis() # Šis automobilis gali važiuoti iki 300 km/h
ford.greitis() # Šis automobilis gali važiuoti iki 100 km/h
```

## Užduotys
