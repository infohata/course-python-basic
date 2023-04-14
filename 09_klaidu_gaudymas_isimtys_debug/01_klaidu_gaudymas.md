# Klaidų gaudymas

Klaidų gaudymas yra būtinas bet kokiame programavimo darbe, kad būtų galima tvarkingai apdoroti nepageidaujamus programos veikimo sutrikimus. Python kalboje klaidų gaudymas yra realizuojamas naudojant `try` ir `except` blokus.

Klaidų gaudymas padeda programuotojams sukurti geresnį ir patikimesnį kodą, kadangi programos gali veikti teisingai ir sklandžiai net tuomet, kai atsiranda klaidų.

## `try except` blokas

`try` bloke rašoma programa, kurios vykdymas gali sukelti klaidą. `except` bloke yra nurodomas kodas, kuris bus vykdomas, jei `try` blokas sukels klaidą. Pvz.:

```Python
try:
    a = 10 / 0
except:
    print("Klaida!") # Klaida!
```

Galima nurodyti konkrečią klaidą `except` bloke (pvz. `TypeError`, `ValueError`, `ZeroDivisionError` ar kt.), tokiu atveju vykdymas eina į `except` bloką tik tada, jei `try` blokas sukelia nurodytą klaidą. Pvz.:

```Python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Negalima dalinti iš nulio!") # Negalima dalinti iš nulio!
```

## Ignoruojam klaidą su `except: pass`

Kartais nereikia daryti jokio veiksmo, kai tam tikra klaida atsiranda. Tokiu atveju galima naudoti `except: pass` konstrukciją, kuri tiesiog praleidžia klaidos apdorojimą ir tęsia programos vykdymą, pvz.:

```Python
try:
    x = 5 / 0
except ZeroDivisionError:
    pass
```

Šiame pavyzdyje `try` blokas taip pat apima dalinimąsi iš nulio, kuris yra klaidos priežastis. Tačiau `except` blokas yra tuščias, nes jame yra tik `pass`. Tai reiškia, kad programa tiesiog praleidžia klaidos apdorojimą ir tęsia vykdymą.

## `else` ir `finally` po `try except`

`else` ir `finally` yra papildomos blokų konstrukcijos, kurios gali būti pritaikytos kartu su `try` ir `except` blokais.

`else` blokas leidžia mums apibrėžti kodą, kuris bus vykdomas tik tada, kai `try` blokas yra sėkmingai baigtas, t.y. kai nebuvo iškelta jokių klaidų. `else` blokas turi būti po visų `except` blokų. Pvz.:

```Python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Negalima dalinti iš nulio!")
else:
    print("Rezultatas yra", result) # Rezultatas yra 5.0
```

`finally` blokas yra skirtas apibrėžti kodą, kuris bus vykdomas nepriklausomai nuo to, ar klaidos buvo iškeltos, ar ne. Tai gali būti naudinga atliekant kai kuriuos veiksmus, pvz., išvalant laikinuosius failus, atjungiant duomenų bazės ryšį ar pan.

```Python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Negalima dalinti iš nulio!")
finally:
    print("Programa baigta vykdyti")
```

Rezultatas:

```Text
Negalima dalinti iš nulio!
Programa baigta vykdyti
```

## Skirtingų klaidų apdorojimas vienam `try` kodo blokui su keliais `Except`

Norint apdoroti skirtingas klaidas viename `try` bloke, galima naudoti kelis `except` blokus su skirtingomis klaidomis. Pvz.:

```Python
try:
    skaicius = int(input("Įveskite skaičių: "))
    rezultatas = 10 / skaicius
except ZeroDivisionError:
    print("Negalima dalyba iš nulio")
except ValueError:
    print("Netinkamas skaičiaus formatas")
else:
    print("Rezultatas yra:", rezultatas)
```

Rezultatas:

```Text
Įveskite skaičių: 0
Negalima dalyba iš nulio

Įveskite skaičių: du
Netinkamas skaičiaus formatas

Įveskite skaičių: 3
Rezultatas yra: 3.3333333333333335
```

Be to, galima naudoti bendrą `except` bloką, kuris pagaus bet kokią klaidą, kuri nėra apdorota ankstesniuose `except` blokuose. Šis blokas dažniausiai naudojamas kaip pagalbinis, kad apsaugotų programą nuo neplanuoto elgesio.

```Python
try:
    skaicius = int(input("Įveskite skaičių: "))
    rezultatas = 10 / skaicius
except ZeroDivisionError:
    print("Negalima dalyba iš nulio")
except ValueError:
    print("Netinkamas skaičiaus formatas")
except:
    print("Įvyko klaida")
else:
    print("Rezultatas yra:", rezultatas)
```

Kombinuojant šias konstrukcijas, galima sukurti labai galingą ir lankstų klaidų valdymo mechanizmą, kuris leidžia kontroluoti programos vykdymo eigą ir užtikrinti, kad klaidos neleistų programai nulūžti arba sukeltų neplanuotą elgesį.

## Alternatyva: `if else` irgi pritaikoma

Klaidų gaudymas gali būti atliekamas ir naudojant `if else` sąlygas. Tai yra alternatyva `try except` metodui. Pvz.:

```Python
skaicius = input("Įveskite skaičių: ")

if skaicius.isdigit():
    skaicius = int(skaicius)
    if skaicius == 0:
        print("Dalyba iš nulio negalima")
    else:
        rezultatas = 10 / skaicius
        print("Rezultatas yra:", rezultatas)
else:
    print("Netinkamas skaičiaus formatas")
```

Rezultatas:

```Text
Įveskite skaičių: 0
Dalyba iš nulio negalima

Įveskite skaičių: du
Netinkamas skaičiaus formatas

Įveskite skaičių: 3
Rezultatas yra: 3.3333333333333335
```

Šis metodas turi privalumų ir trūkumų. Vienas privalumas yra tai, kad jis gali būti paprastesnis nei `try except` metodas, ypač jei norime apdoroti tik vieną klaidą. Tačiau, kai turime apdoroti daug klaidų, pavyzdžiui, jei turime apdoroti penkis skirtingus klaidų tipus, mes turime rašyti penkias atskiras sąlygas, kas gali padaryti kodą pernelyg ilgą ir neskaitomą.

## Užduotys
