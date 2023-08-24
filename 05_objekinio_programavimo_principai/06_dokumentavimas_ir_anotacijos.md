# Dokumentavimas ir Anotacijos

## Docstrings (dokumentavimas)

Docstrings yra eilutės, kurios rašomos virš modulio, klasės, funkcijos ar metodo ir aprašo jų paskirtį, veikimą, parametrus ir grąžinamas reikšmes. Docstrings rašomi tarp trijų kabučių (t.y. '''docstring''' arba """docstring"""), kai modulio, klasės, funkcijos ar metodo apibrėžimo eilutės prasideda nuo naujos eilutės.

Docstrings yra galingas dokumentavimo įrankis, kuris padeda kitiems programuotojams suprasti jūsų kodo veikimą. Be to, docstrings yra labai pasiteisina, kai naudojate interaktyvią Python aplinką arba automatinį dokumentavimą.

Štai keli pavyzdžiai, kaip galite naudoti docstrings Python programavimo kalboje:

## Docstring modulio aprašymui:

```Python
'''Modulis, skirtas duomenų apdorojimui'''
import pandas as pd

def skaityti_duomenis(failo_pavadinimas):
    '''
    Funkcija, kuri skaito duomenis iš CSV formato failo.
    
    Argumentai:
    failo_pavadinimas (str): CSV formato failo pavadinimas
    
    Grąžinamos reikšmės:
    pd.DataFrame: lentelė su duomenimis
    
    '''
    duomenys = pd.read_csv(failo_pavadinimas)
    return duomenys
```

Šiame pavyzdyje modulis ir funkcija turi docstrings. Modulio docstring trumpai aprašo modulio paskirtį, o funkcijos docstring aprašo funkcijos paskirtį, argumentus ir grąžinamas reikšmes.

## Docstring klasės aprašymui

```Python
class Studentas:
    '''Klasė, skirta studentų duomenims laikyti'''
    
    def __init__(self, vardas, pavarde, amzius):
        '''
        Konstruktorius, skirtas sukurti naują Studentas objektą.
        
        Argumentai:
        vardas (str): studento vardas
        pavarde (str): studento pavardė
        amzius (int): studento amžius
        
        Grąžinamos reikšmės:
        None
        '''
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        
    def pilnas_vardas(self):
        '''
        Funkcija, kuri sugeneruoja studento pilną vardą.
        
        Grąžinamos reikšmės:
        str: studento pilnas vardas
        '''
        return f'{self.vardas} {self.pavarde}'
```

Šiame pavyzdyje klasės metodo docstring aprašo, kad funkcija pilnas_vardas() grąžina studento pilną vardą, kuris yra eilutės tipo duomenų tipas.

## Docstring funkcijos aprašymui

```Python
def suma(a, b):
    '''
    Funkcija, kuri suskaičiuoja dviejų skaičių sumą.
    
    Argumentai:
    a (int): pirmasis skaičius
    b (int): antrasis skaičius
    
    Grąžinamos reikšmės:
    int: sumos reikšmė
    
    '''
    return a + b
```

Šiame pavyzdyje funkcija turi docstring, kuris aprašo funkcijos paskirtį, argumentus ir grąžinamas reikšmes.

## Docstring metodo aprašymui

Šiame pavyzdyje klasės metodo docstring aprašo metodo paskirtį ir grąžinamas reikšmes.

```Python
class Automobilis:
    '''Klasė, skirta automobilių duomenims laikyti'''
    
    def __init__(self, marke, modelis, metai):
        '''
        Konstruktorius, skirtas sukurti naują Automobilis objektą.
        
        Argumentai:
        marke (str): automobilio markė
        modelis (str): automobilio modelis
        metai (int): automobilio gamybos metai
        
        Grąžinamos reikšmės:
        None
        '''
        self.marke = marke
        self.modelis = modelis
        self.metai = metai
        
    def info(self):
        '''
        Funkcija, kuri atspausdina automobilio informaciją.
        
        Grąžinamos reikšmės:
        None
        '''
        print(f'{self.marke} {self.modelis}, {self.metai} metai')
```

Šiame pavyzdyje klasės metodo docstring aprašo metodo paskirtį ir grąžinamas reikšmes.

Kaip matote, docstrings yra naudingas dokumentavimo įrankis, kuris padeda kitiems programuotojams suprasti jūsų kodo veikimą. Juos rekomenduojama naudoti kiekvienoje Python programoje.

❗ Svarbu pastebėti, kad docstring formatas nėra standartizuotas. Dažniausiai naudojamas formatas yra [PEP 257](https://peps.python.org/pep-0257/), kuris aprašo, kaip turėtų būti struktūruojamas docstring tekstas. Tačiau galite naudoti bet kokį savo pasirinktą formatą, kuris atitinka jūsų poreikius ir yra lengvai suprantamas kitų programuotojų.

## Anotacijos

Python anotacijos yra papildoma informacija apie kintamųjų, funkcijų ir metodų tipus, kuri yra pridedama tiesiogiai prie jų apibrėžimų. Šios anotacijos gali būti naudingos programuotojams, kadangi jos gali padėti geriau suprasti kodo funkcionalumą, palengvinti programavimo klaidų suradimą ir gali būti naudingos statinio kodo analizėje.

Norint naudoti anotacijas Python kode, reikia pridėti jas prie kintamųjų, funkcijų ar metodų apibrėžimų kaip papildomą argumentą, kuris aprašo tipą. Štai keletas pavyzdžių, kaip tai galima padaryti:

```Python
def sum_numbers(a: int, b: int) -> int:
    return a + b
```

Ši funkcija turi du argumentus a ir b, kurie yra sveikieji skaičiai (int), o grąžinamas reikšmės tipas yra taip pat sveikasis skaičius (int).

```Python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

Ši klasė turi du kintamuosius name ir age, kurie yra atitinkamai eilutės (str) ir sveikieji skaičiai (int).

## Klasės anotacija su tipais parametrų ir grąžinimo reikšmės:

```Python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def get_age(self) -> int:
        return self.age
```

Metodo anotacija su keliomis reikšmėmis grąžinimo tipui ir parametramis:

```Python
import math


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self, radius: float) -> float:
        """
        A function to calculate the area of a circle.
        Returns the area of the circle.
        """
        return math.pi * radius ** 2
```

❗ Python anotacijos nėra privalomos, tačiau jos gali padėti geriau suprasti kodo funkcionalumą, palengvinti programavimo klaidų suradimą ir gali būti naudingos statinio kodo analizėje. Taigi, jei norite pasinaudoti Python anotacijomis savo kode, jums reikia tiesiog pridėti papildomą argumentą prie kintamųjų, funkcijų ar metodų apibrėžimų, kuris aprašo tipą.
