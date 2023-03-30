# Kintamieji

Kintamieji yra vertybės, kurios yra saugomos ir gali būti pasiektos vėliau. Python kalboje kintamieji nėra apibrėžiami tipu, todėl jų tipas yra nustatomas automatiškai pagal priskirtą reikšmę.

Kintamieji gali būti apibrėžti sužymėjus jų pavadinimą ir priskiriant tam tikrą reikšmę, pavyzdžiui:

```Python
x = 5
```

Šiame pavyzdyje kintamasis "x" yra apibrėžtas ir priskirta reikšmė 5. Jei norite sužinoti kintamojo reikšmę, tiesiog išspausdinkite jį naudodami print() funkciją:

```Python
print(x)
```

Šis kodas išspausdins reikšmę "5", kuri yra saugoma kintamajame "x".

Kintamieji taip pat gali būti priskiriami naujoms reikšmėms, pavyzdžiui:

```Python
x = 5
x = 10
```

Po šio kodo vykdymo kintamasis "x" turės reikšmę 10, o ne 5.

Taip pat galite apibrėžti kelis kintamuosius vienu metu, pavyzdžiui:

```Python
x, y, z = 1, 2, 3
```

Šiame pavyzdyje kintamieji "x", "y" ir "z" yra apibrėžti ir priskirtos reikšmės 1, 2 ir 3 atitinkamai.

Jei norite sužinoti kintamojo tipą, galite naudoti funkciją "type()", pavyzdžiui:

```Python
x = 5
print(type(x))
```

Šis kodas išspausdins "int", nurodydamas, kad "x" yra sveikasis skaičius (integer).

## Pagrindinės taisyklės ir išimtys

### Kintamųjų pavadinimo taisyklės: 

```Python
# Pavyzdys su netinkamu kintamojo pavadinimu:
2x = 5  # neteisingas kintamojo pavadinimas
print(2x)  # klaida, nes neteisingas pavadinimas

# Pavyzdys su tinkamu kintamojo pavadinimu:
mano_kintamasis = 10
print(mano_kintamasis)  # išspausdina 10
```

Šiame pavyzdyje parodyta, kad kintamieji turi prasidėti raidėmis arba pabrėžimu (_), o ne skaičiais. Tai yra priežastis, kodėl pirmas pavyzdys su netinkamu kintamojo pavadinimu sukels klaidą.

### Kintamųjų jautrumas didžiajai ir mažajai raidei:

```Python
x = 5
X = 10
print(x)  # išspausdina 5
print(X)  # išspausdina 10
```

Šiame pavyzdyje parodyta, kad kintamųjų pavadinimai yra jautrūs didžiajai ir mažajai raidei. Tai reiškia, kad "x" ir "X" yra skirtingi kintamųjų pavadinimai.

### Kintamųjų tipai:

```Python
x = 5
y = "Hello, world!"
z = 3.14
print(type(x))  # išspausdina <class 'int'>
print(type(y))  # išspausdina <class 'str'>
print(type(z))  # išspausdina <class 'float'>
```

Šiame pavyzdyje parodyta, kad Python kalboje kintamieji nėra apibrėžiami tipu, o jų tipas yra nustatomas pagal priskirtą reikšmę. Tai reiškia, kad kintamasis gali turėti skirtingus tipus skirtingais programos etapais.

### Kintamųjų reikšmių keitimas:

```Python
x = 5
print(x)  # išspausdina 5
x = "Hello, world!"
print(x)  # išspausdina "Hello, world!"
```

Šiame pavyzdyje parodyta, kad kintamojo reikšmė gali būti keičiama bet kuriuo metu, ir kintamasis gali turėti skirtingus tipus skirtingais programos etapais.

### Kintamųjų priskyrimas kitam kintamajam:

Šiame pavyzdyje parodyta, kad kai kintamasis yra priskiriamas kitam kintamajam, pavyzdžiui, "y = x", tai reiškia, kad kintamasis "y" gaus tą pačią reikšmę kaip ir kintamasis "x". Tačiau, kai keičiama kintamojo "x" reikšmė, kintamasis "y" nesikeičia, nes jie rodo į skirtingas atminties vietas. Tai yra susiję su kintamųjų saugojimu atmintyje ir gali lemti neefektyvų programos veikimą, jei yra naudojami dideli kintamieji arba yra daugiau operacijų su kintamaisiais.

```Python
x = 5
y = x
print(y)  # išspausdina 5
x = 10
print(x)  # išspausdina 10
print(y)  # išspausdina 5
```

Šiuo kodu kintamajam "y" yra priskirta reikšmė "5", kai jis priskiriamas kintamajam "x". Tačiau, kai kintamojo "x" reikšmė yra pakeičiama į 10, tai neturi įtakos kintamojo "y" reikšmei, kuri vis dar lygi 5.

## Užduotys

- Sukurkite kintamąjį a ir priskirkite jam bet kokį sveikąjį skaičių.
- Sukurkite kitą kintamąjį b ir priskirkite jam bet kokį slankiojo kablelio skaičių.
- Tada sukurkite trečią kintamąjį c ir priskirkite jam bet kokį kompleksinį skaičių. 
- Atspausdinkite visus tris kintamuosius ir patikrinkite jų tipus.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<hr>
<p>Kintamasis a yra sveikasis skaičius. Kintamasis b yra slankiojo kablelio skaičius. Kintamasis c yra kompleksinis skaičius.</p>
  
```Python
a = 5
b = 3.14
c = 2 + 3j

print(a, type(a))
print(b, type(b))
print(c, type(c))
```

Rezultatas:

```Text
5 <class 'int'>
3.14 <class 'float'>
(2+3j) <class 'complex'>
```

</details>