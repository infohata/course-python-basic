# Išimtys

## `TypeError`

Viena iš klaidų, kurias gali sukelti netinkamo tipo duomenų naudojimas, yra `TypeError`. Pvz, kai bandome sudėti skirtingus duomenų tipus:

```Python
skaicius = 42
vardas = "John"
rezultatas = vardas + skaicius # TypeError: can only concatenate str (not "int") to str
```

Klaidos tvarkymui naudojame `try` ir `except` blokus, kurie leidžia apdoroti išimtis ir tęsti programos vykdymą:

```Python
skaicius = 42
vardas = "John"
try:
    rezultatas = vardas + skaicius
except TypeError:
    print("Klaida: negalima sudėti 'str' ir 'int' tipų duomenų") # Klaida: negalima sudėti 'str' ir 'int' tipų duomenų
```

## `NameError`

Neegzistuojančio kintamojo naudojimas sukelia `NameError`, pvz.:

```Python
a = 10
print(b) # NameError: name 'b' is not defined
```

Šis kodas sukurs `NameError`, kadangi kintamasis `b` nebuvo apibrėžtas anksčiau programoje. Viena iš būdų šios klaidos tvarkymui yra naudoti `try` ir `except` blokus:

```Python
a = 10
try:
    print(b)
except NameError:
    print("Klaida: kintamasis nebuvo apibrėžtas") # Klaida: kintamasis nebuvo apibrėžtas
```

## `ValueError`, ZeroDivisionError

`ValueError` klaidą sukelia bandymas konvertuoti reikšmę į teisingą tipą, bet tai negali būti padaryta dėl neteisingų arba negalimų reikšmių, pvz.:

```Python
try:
    x = int('abc')
except ValueError:
    print("Klaida: negalima konvertuoti reikšmės į skaičių") # Klaida: negalima konvertuoti reikšmės į skaičių
```

`ZeroDivisionError` klaidą sukelia bandymas padalinti skaičių iš nulio. Tai yra neleistina matematinė operacija, todėl išmeta šią klaidą, kai bandote ją atlikti. Pvz.:

```Python
try:
    x = 1/0
except ZeroDivisionError:
    print("Klaida: negalima dalinti iš nulio") # Klaida: negalima dalinti iš nulio
```

## `IndexError` sąrašams, KeyError žodynams

`IndexError` klaidą sukelia bandymas pasiekti sąrašo elementą, kuris neegzistuoja pagal nurodytą indeksą, pvz:

```Python
sarasas = [1, 2, 3]

try:
    print(sarasas[3])
except IndexError:
    print("Klaida: indeksas viršija sąrašo ribas") # Klaida: indeksas viršija sąrašo ribas
```

`KeyError` klaidą sukelia bandymas pasiekti žodyno rakto reikšmę, kuris neegzistuoja, pvz:

```Python
zodynas = {"a": 1, "b": 2, "c": 3}

try:
    print(zodynas["d"])
except KeyError:
    print("Klaida: rakto reikšmė neegzistuoja žodyne") # Klaida: rakto reikšmė neegzistuoja žodyne
```

## `AttributeError` objektams

`AttributeError` išimtis iškyla, kai programa bando pasiekti atributą, kuris neegzistuoja objekte arba klasėje, pvz.:

```Python
class Asmuo:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

zmogus = Asmuo("Jonas", 25)
print(zmogus.vardas)  # Jonas
print(zmogus.pavarde)  # AttributeError: 'Asmuo' object has no attribute 'pavarde'
```

Norint apsaugoti programą nuo `AttributeError` išimčių, galime naudoti `try except` bloką:

```Python
try:
    print(zmogus.pavarde)
except AttributeError:
    print("Klaida: `pavarde` atributas neegzistuoja") # Klaida: `pavarde` atributas neegzistuoja
```

## `hasattr()` funkcija objekto atributo patikrinimui

`hasattr()` funkcija leidžia patikrinti, ar objekte yra nurodytas atributas. Ji priima objekto ir atributo pavadinimą kaip argumentus ir grąžina `True`, jei atributas egzistuoja, ir `False`, jei ne. Pvz.:

```Python
if hasattr(zmogus, 'pavarde'):
    print(zmogus.pavarde)
else:
    print("Klaida: `pavarde` atributas neegzistuoja") # Klaida: `pavarde` atributas neegzistuoja
```

## `except Exception as e` bendrinė klasės objektas, jo `__class__.__name__` gavimas

`Exception` yra bendrinis `try except` blokas, kuris gaudys bet kokios rūšies išimtis. Tai yra naudinga, kai nenorite apibrėžti kiekvienos išimties atskirai, bet norite jas visas sugauti viename bloke.

Galima keisti išimčių pavadinimus naudojant `as` raktažodį tam, kad sutrumpinti ilgą klaidos pavadinimą į trumpesnį arba lengviau suprantamą pavadinimą. Pavyzdžiui nurodytas kintamasis gali būti naudojamas kaip argumentas, kuriuo remiantis spausdinamas klaidos pranešimas:

```Python
try:
    x = 1 / 0
except Exception as e:
    print("Išimtis:", e) # Išimtis: division by zero
```

Kai programa iškelia išimtį, galima gauti išimties klasės pavadinimą naudojant `__class__.__name__`. Tai leidžia tiksliau identifikuoti išimtis ir atlikti reikiamus veiksmus pagal situaciją. Pvz.:

```Python
try:
    x = 1 / 0
except Exception as e:
    print("Išimtis:", e.__class__.__name__) # Išimtis: ZeroDivisionError
```

## Užduotys
