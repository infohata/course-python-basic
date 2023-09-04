# Dekoratoriai

Python programavimo kalboje dekoratoriai yra aukštesnio rango funkcijos, naudojamos modifikuoti ar papildyti funkcijų ar metodų elgesį, nekeičiant jų kodo. Aukštesnio rango funkcijos yra tokios funkcijos, kurios priima kitas funkcijas kaip argumentus arba grąžina funkcijas kaip rezultatus.

## Dekoratoriaus deklaracija, wrapper'is

Dekoratorius yra funkcija, kuri priima kitą funkciją kaip argumentą ir grąžina naują funkciją, kuri papildomai apjungia ar modifikuoja esamos funkcijos elgesį. Wrapper (apgaubianti) funkcija yra ta, kuri būna sukuriama ir grąžinama dekoratoriaus funkcijos metu.

Pavyzdys:

```Python
def dekoratorius(funkcija):
    def wrapper(*args, **kwargs):
        print("Prieš funkcijos iškvietimą")
        rezultatas = funkcija(*args, **kwargs)
        print("Po funkcijos iškvietimo")
        return rezultatas
    return wrapper
```

Dekoratoriaus pavyzdys:

```Python
def pasisveikinimas(funkcija):
    def wrapper(vardas):
        print(f"Sveiki, {vardas}!")
        funkcija(vardas)
    return wrapper

@pasisveikinimas
def atsisveikinimas(vardas):
    print(f"Viso gero, {vardas}!")

atsisveikinimas("Jonas")
```

Šiame pavyzdyje dekoratorius sveikinimas priima funkciją `atsisveikinimas` kaip argumentą ir grąžina `wrapper` funkciją. "wrapper" funkcija atspausdina sveikinimo tekstą, tada iškviečia atsisveikinimas funkciją su tuo pačiu vardu. Taigi, kai iškviečiama `atsisveikinimas("Jonas")`.

Dar vienas pavyzdys: 

```Python
def tikrinti_teigiamus(funkcija):
    def wrapper(*args, **kwargs):
        if all(arg > 0 for arg in args):
            rezultatas = funkcija(*args, **kwargs)
        else:
            rezultatas = "Klaida: visi argumentai turi būti teigiami"
        return rezultatas
    return wrapper

@tikrinti_teigiamus
def daugyba(x, y):
    return x * y

rezultatas1 = daugyba(3, 5)
print(f"Daugybos rezultatas: {rezultatas1}")

rezultatas2 = daugyba(-2, 4)
print(f"Daugybos rezultatas: {rezultatas2}")
```

Šiame pavyzdyje `tikrinti_teigiamus` yra dekoratorius, kuris priima funkciją daugyba kaip argumentą ir grąžina `wrapper` funkciją. wrapper funkcija tikrina, ar visi perduoti argumentai yra teigiami. Jei taip, iškviečiama daugyba funkcija su perduotais argumentais ir grąžinamas rezultatas. Jei ne, grąžinamas klaidos pranešimas.

## Dekoratorių pavyzdžiai Python programavimo kalboje

## `@property` dekoratorius

`@property` dekoratorius naudojamas apibrėžiant getter metodus klasės atributams. Jis leidžia prieiti prie funkcijos rezultato kaip prie klasės atributo, o ne kaip prie metodo.

```Python
class Zmogus:
    def __init__(self, vardas, pavarde):
        self._vardas = vardas
        self._pavarde = pavarde

    @property
    def pilnas_vardas(self):
        return f"{self._vardas} {self._pavarde}"
```

## @staticmethod dekoratorius

`@staticmethod` dekoratorius leidžia apibrėžti statinius metodus klasėje. Statiniai metodai gali būti iškviesti klasės lygmeniu, nesant objekto egzemplioriaus, ir jie nepriklauso nuo objekto būsenos.

```Python
class Matematika:
    @staticmethod
    def sudetis(x, y):
        return x + y

rezultatas = Matematika.sudetis(3, 5)
print(rezultatas)
```

## @classmethod dekoratorius

`@classmethod` dekoratorius leidžia apibrėžti klasės metodus, kurie priima klasę kaip pirmąjį argumentą, vadinamą "cls". Klasės metodai gali būti naudojami klasės ar objekto lygmeniu, bet visada gražina klasės atributus.

```Python
class Automobilis:
    _gamintojas = "Toyota"

    @classmethod
    def gamintojas(cls):
        return cls._gamintojas

print(Automobilis.gamintojas())
```

## Dekoratorių docstring'ai

Docstring'ai yra ilgesni komentarai, aprašantys funkcijos veikimą, parametrus ir grąžinamus rezultatus. Jie rašomi tarp trijų kabučių ir privalo būti funkcijos pradžioje, prieš pat jos kodą.
Pavyzdys:

```Python
def my_decorator(func):
    """
    Dekoratorius, kuris atspausdina pranešimą prieš ir po funkcijos vykdymo.

    Args:
        func (callable): Funkcija, kurią reikia dekoruoti.
    """
    def wrapper(*args, **kwargs):
        print("Funkcija bus iškviesta")
        result = func(*args, **kwargs)
        print("Funkcija buvo iškviesta")
        return result
    return wrapper
```

## Dekoratorių anotacijos

Anotacijos yra užuomina apie kintamųjų tipus. Jos padeda geriau suprasti, kokius duomenų tipus funkcija priima ir grąžina. Anotacijos yra neprivalomos ir neturi įtakos programos veikimui, tačiau padeda suprasti ir skaityti kodą.

Pavyzdys:

```Python
from typing import Callable, Any

def my_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs) -> Any:
        print("Funkcija bus iškviesta")
        result = func(*args, **kwargs)
        print("Funkcija buvo iškviesta")
        return result
    return wrapper
```

## Dekoratorių @wraps() naudojimas

Dekoratoriaus viduje sukuriama vidinė funkcija (paprastai vadinama wrapper), kuri sukviečia pradinę funkciją. Tačiau šis elgesys gali sukelti problemų, nes vidinės funkcijos atributai gali "užgožti" pradinės funkcijos atributus. Norint išvengti šios problemos, galima naudoti functools.wraps() dekoratorių.

Pavyzdys:

```Python
from functools import wraps
from typing import Callable, Any

def my_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print("Funkcija bus iškviesta")
        result = func(*args, **kwargs)
        print("Funkcija buvo iškviesta")
        return result
    return wrapper

@my_decorator
def example_function(a: int, b: int) -> int:
    """
    Funkcija, skirta sudėti du skaičius ir grąžinti rezultatą.

    Args:
        a (int): Pirmasis skaičius.
        b (int): Antrasis skaičius.
    Returns:
        int: Skaičių suma.
    """
    return a + b

print(example_function(3, 5))  # Output: Funkcija bus iškviesta, Funkcija buvo iškviesta, 8
print(example_function.__name__)  # Output: example_function
print(example_function.__doc__)  # Output: Funkcija, skirta sudėti du skaičius ir grąžinti rezultatą...
```

Šiame pavyzdyje `@wraps(func)` dekoratorius naudojamas wrapper funkcijai, kad išlaikytų pradinės funkcijos (šiuo atveju example_function) metaduomenis. Be `@wraps(func)`, `example_function.__name__` ir `example_function.__doc__` grąžintų vidinės `wrapper` funkcijos vardą ir docstring'ą. Su `@wraps(func)` dekoratoriumi, grąžinami teisingi pradinės funkcijos metaduomenys.

## Dekoratoriaus su parametrais sukūrimas

Dekoratoriai su parametrais leidžia jums perduoti papildomus parametrus dekoratoriui, kad jūsų dekoratorius būtų lankstesnis ir lengviau pritaikomas skirtingose situacijose. Norint sukurti dekoratorių su parametrais, reikia sukurti dar vieną išorinę funkciją, kuri grąžina dekoratorių. Taip pat galite naudoti kelis dekoratorius ant vienos funkcijos, kad pritaikytumėte kelis elgsenos pakeitimus.

Pavyzdys:

```Python
from functools import wraps
from typing import Callable, Any

def repeat_decorator(times: int):
    def actual_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator

@repeat_decorator(3)
def print_message(message: str) -> None:
    print(message)

print_message("Labas!")  # Output: Labas! Labas! Labas!
```

Šiame pavyzdyje `repeat_decorator` funkcija priima times parametrą, kuris nurodo, kiek kartų dekoruota funkcija turi būti iškviesta. Vidinė funkcija `actual_decorator` yra grąžinama išorinės funkcijos ir veikia kaip įprastas dekoratorius.

## Keli dekoratoriai ant funkcijos

Galite naudoti kelis dekoratorius ant vienos funkcijos, tačiau turėkite omenyje, kad jie bus pritaikyti tam tikra tvarka. Pirmasis dekoratorius bus pritaikytas paskutinis, antrasis dekoratorius bus pritaikytas prieš paskutinį ir t.t.

Pavyzdys:

```Python
from functools import wraps
from typing import Callable, Any

def print_before_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print("Funkcija bus iškviesta")
        return func(*args, **kwargs)
    return wrapper

def print_after_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        print("Funkcija buvo iškviesta")
        return result
    return wrapper

@print_before_decorator
@print_after_decorator
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(3, 5)  # Output: Funkcija bus iškviesta, Funkcija buvo iškviesta
print(result)  # Output: 8
```

Šiame pavyzdyje `add_numbers` funkcija yra dekoruota dviem dekoratoriais: `print_before_decorator` ir `print_after_decorator`.

## Užduotys

### Pirma užduotis

Sukurkite klasę Studentas su atributais vardas, pavarde ir amzius. Pridėkite tris metodus:

- pilnas_vardas(): Grąžina pilną studento vardą, naudojant @property dekoratorių.
- ar_pilnametis(): Grąžina True, jei studento amžius yra didesnis arba lygus 18, ir False, jei ne. Naudokite @staticmethod dekoratorių.
- sukurti_studenta(cls, vardas: str, pavarde: str, amzius: int): Grąžina naują Studentas objektą. Naudokite @classmethod dekoratorių.
- Sukurkite keletą studentų objektų, naudojant klasės metodą sukurti_studenta(), ir išbandykite visus metodus.

### Antra užduotis

Parašykite dekoratorių, kuris:

- visus dekoruotos funkcijos tekstinius argus ir kwargus paverčia didžiosiomis raidėmis.
- visus funkcijos teksinius rezultatus paverčia didžiosiomis raidėmis.

### Trečia užduotis

- Parašykite funkciją rasti pirminį skaičių
- Parašykite neribotą pirminių skaičių generatorių
- Parašykite dekoratorių matuoti funkcijos laikui
- Padarykite funkciją, kuri turi ciklą printinimui pirminių skaičių sekos radimui iki tol, kol einamo pirminio sekos skaičiaus radimas tuks ilgiau negu 0,01 sekundės.
- išspausdinkite viso proceso trukmę, panaudojant dekoratorių

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
class Studentas:
    def __init__(self, vardas, pavarde, amzius):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius

    @property
    def pilnas_vardas(self):
        return f"{self.vardas} {self.pavarde}"

    @staticmethod
    def ar_pilnametis(amzius):
        return amzius >= 18

    @classmethod
    def sukurti_studenta(cls, vardas: str, pavarde: str, amzius: int):
        return cls(vardas, pavarde, amzius)


# Sukurkite keletą studentų objektų, naudojant klasės metodą sukurti_studenta()
studentas1 = Studentas.sukurti_studenta("Jonas", "Jonaitis", 20)
studentas2 = Studentas.sukurti_studenta("Petras", "Petraitis", 17)

# Išbandykite visus metodus
print(studentas1.pilnas_vardas)  # Output: "Jonas Jonaitis"
print(studentas2.pilnas_vardas)  # Output: "Petras Petraitis"

print(Studentas.ar_pilnametis(studentas1.amzius))  # Output: True
print(Studentas.ar_pilnametis(studentas2.amzius))  # Output: False
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
from functools import wraps
def make_upper(func):
    """ This decorator makes all function arguments and keyword arguments upper case if they are text, then makes the result upper case if it is text """
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) == str:
                arg = arg.upper()
        for kwarg in kwargs:
            if type(kwarg) == str:
                kwargs[kwarg] = kwargs[kwarg].upper()
        result = func(*args, **kwargs)
        if type(result) == str:
            result = result.upper()
        return result
    return wrapper

# testing the above decorator with function, which makes text lowecase, with a debug print
@make_upper
def make_lower(string="Hello World"):
    print(f"making '{string}' lowercase")
    return string.lower()

# testing of the decorated function
print(make_lower())
print(make_lower("it works!"))
```
</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
from time import time

def rasti_pirmini(skaicius):
    if skaicius < 2:
        return False
    for sk in range(2, skaicius):
        if skaicius % sk == 0:
            return False
    return True

def pirminiu_sk_generatorius():
    skaicius = 2
    while True:
        if rasti_pirmini(skaicius):
            yield skaicius
        skaicius += 1

def matuoti_laika(funkcija):
    def wrapper(*args, **kwargs):
        startas = time()
        rezultatas = funkcija(*args, **kwargs)
        pabaiga = time()
        print(f"Vykdymo laikas: {pabaiga - startas} s..")
        return rezultatas
    return wrapper

@matuoti_laika
def pirminiu_seka_iki_laiko():
    pirm_sk_gen = pirminiu_sk_generatorius()
    sekantis_pirminis = next(pirm_sk_gen)
    while True:
        startas = time()
        pirminis = sekantis_pirminis
        sekantis_pirminis = next(pirm_sk_gen)
        prabeges_laikas = time() - startas
        print(prabeges_laikas)
        if prabeges_laikas > 0.01:
            break
        print(pirminis)
            
pirminiu_seka_iki_laiko()
```

</details>
</details>
