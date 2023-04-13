# Klaidos iššaukimas

Klaidos iššaukimas yra svarbi programavimo koncepcija, kuri leidžia programuotojams nurodyti, kad programa susidūrė su problema ir ją reikia nutraukti. Python programavimo kalba turi daug įvairių išimčių, kurios leidžia programuotojams iššaukti klaidas ir apdoroti jas vėliau.

## Klaidos iššaukimas su `raise`

`raise` komanda leidžia iškelti klaidą programos vykdymo metu. Tai yra paprasta funkcija, kuri sukelia klaidą su nurodytu pranešimu. Pvz.:

```Python
raise ValueError("Blogas argumentas") # raise ValueError("Blogas argumentas")
```

Kadangi `raise` yra funkcija, galima ją panaudoti bet kurioje vietoje programos, kurioje reikalinga klaidos iššaukimas. Taip pat galima iškelti klaidų klases, panaudodami `raise`. Pvz.:

```Python
class ManoKlaida(Exception):
    pass

raise ManoKlaida("Nepavyko atidaryti failo") # __main__.ManoKlaida: Nepavyko atidaryti failo
```

Įprastai klaidas iškelia funkcijos, kurios jas grąžina `return` su pranešimu, kuris informuoja apie klaidą. Pvz.:

```Python
def padalinimas(x, y):
    if y == 0:
        raise ValueError("Dalyba iš nulio negalima")
    return x / y

try:
    rezultatas = padalinimas(10, 0)
except ValueError as e:
    print(e) # Dalyba iš nulio negalima
else:
    print(rezultatas)
```

## Klaidos iššaukimas su `raise Exception`

`raise` funkcija gali būti naudojama su bet kokia klaidų klase, tačiau rekomenduojama naudoti `Exception` klasę, kadangi ji yra bendra klaidų klasė ir paprastesnė apdorojimui. Pvz.:

```Python
raise Exception('Klaidos pranešimas') # Exception: Klaidos pranešimas
```

Galima perrrašyti aukščiau minėtą pavyzdį:

```Python
def padalinimas(x, y):
    if y == 0:
        raise Exception("Dalyba iš nulio negalima")
    return x / y

try:
    rezultatas = padalinimas(10, 0)
except Exception as e:
    print(e) # Dalyba iš nulio negalima
else:
    print(rezultatas)
```

## Klaidos iššaukimas su `raise ValueError`

`raise ValueError` komanda naudinga, kai reikia informuoti apie neleistiną argumentą ar reikšmę. Pvz.:

```Python
def skaiciu_kubas(skaicius):
    if not isinstance(skaicius, int):
        raise ValueError("Funkcija veikia tik su sveikais skaičiais")
    return skaicius ** 3

try:
    kubas = skaiciu_kubas(1.5)
except ValueError as e:
    print(e) # Funkcija veikia tik su sveikais skaičiais
else:
    print(kubas)
```

## Užduotys
