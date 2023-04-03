# Programavimo stilius

## Naudokite 4 tarpus atitraukimui, o ne tabuliaciją

<p style="color: #03C04A;">Gerai:</p>

```Python
def suma(a, b):
    return a + b
```

<p style="color: red;">Blogai:</p>

```Python
def suma(a, b):
⇥return a + b
```

## Eilutės neturi būti ilgesnės nei 79 simboliai

<p style="color: #03C04A;">Gerai:</p>

```Python
print("Ši eilutė yra mažesnė nei 80 simbolių, todėl ji yra "
      "lengvai skaitoma.")
```

<p style="color: red;">Blogai:</p>

```Python
print("Ši eilutė yra per ilga ir viršija 80 simbolių, todėl ji yra sunkiau skaitoma ir gali sukelti problemų su mažesniais ekranais.")
```

## Naudokite tuščias eilutes funkcijoms ir klasėms atskirti, taip pat didesniems kodo blokams funkcijų viduje

<p style="color: #03C04A;">Gerai:</p>

```Python
def suma(a, b):
    return a + b

def skirtumas(a, b):
    return a - b
```

<p style="color: red;">Blogai:</p>

```Python
def suma(a, b):
    return a + b
def skirtumas(a, b):
    return a - b
```

## Komentarus rašykite atskirose eilutėse

<p style="color: #03C04A;">Gerai:</p>

```Python
# Apskaičiuoti sumą
rezultatas = suma(a, b)
```

<p style="color: red;">Blogai:</p>

```Python
rezultatas = suma(a, b)  # Apskaičiuoti sumą
```

## Naudokite docstrings

<p style="color: #03C04A;">Gerai:</p>

```Python
def suma(a, b):
    """
    Grąžina dviejų skaičių sumą.
    
    Parametrai:
    a -- pirmasis skaičius
    b -- antrasis skaičius
    """
    return a + b
```

## Naudokite tarpus aplink operatorius ir po kablelių

<p style="color: #03C04A;">Gerai:</p>

```Python
a = f(1, 2) + g(3, 4)
```

<p style="color: red;">Blogai:</p>

```Python
a=f(1,2)+g(3,4)
```

## Pavadinkite klases ir funkcijas nuosekliai

Paprastai klasėms naudojama 'UpperCamelCase', o funkcijoms ir metodams - mažosiomis_raidelemis_su_pabraukimais (lowercase_with_underscores). Pirmajam metodo argumentui visada naudokite pavadinimą "self".

<p style="color: #03C04A;">Gerai:</p>

```Python
class Automobilis:
    def vaziuoti(self, atstumas):
        pass
```

<p style="color: red;">Blogai:</p>

```Python
class automobilis:
    def Vaziuoti(self,Atstumas):
        pass
```

## Naudokite UTF-8 arba ASCII koduotę

💡 UTF-8 (Unicode Transformation Format - 8-bit) yra labai populiarus Unicode koduotės standartas, kuris gali užkoduoti visą Universal Character Set (UCS) simbolių rinkinį. Jis yra suderinamas su ASCII ir daugelyje situacijų pakeitė šį senesnį standartą. Pagrindinis UTF-8 pranašumas yra tas, kad jis gali užkoduoti ir ne-ASCII simbolius, tokius kaip diakritiką turinčius rašmenis, hieroglifus, simbolius iš skirtingų rašto sistemų ir t.t. UTF-8 yra lankstus ir efektyvus kodavimo būdas, naudojamas daugelyje interneto puslapių ir programinės įrangos.

💡 ASCII (American Standard Code for Information Interchange) yra senesnis koduotės standartas, sukurtas JAV. Jis apima tik 128 simbolius, įskaitant anglų abėcėlės raides (didžiąsias ir mažąsias), skaitmenis, kai kuriuos skyrybos ženklus ir kontrolės simbolius. ASCII buvo plačiai naudojamas ankstesniuose kompiuteriuose ir programinėje įrangoje, tačiau jo ribotas simbolių rinkinys apribojo jo tinkamumą tarptautinėje aplinkoje.

Dabar programavime dažniausiai naudojamas UTF-8 koduotės standartas, nes jis apima didelį simbolių skaičių ir yra suderinamas su ASCII. Tačiau kai kuriais atvejais (ypač kai tekstas yra tik anglų kalba) galima naudoti ir ASCII koduotę.

## Nenaudokite ne-ASCII simbolių identifikatoriuose

<p style="color: #03C04A;">Gerai:</p>

```Python
   def sveikas_pasauli():
       print("Labas pasauli!")
```

<p style="color: red;">Blogai:</p>

```Python
   def sveikas_пасаули():
       print("Labas pasauli!")
```
