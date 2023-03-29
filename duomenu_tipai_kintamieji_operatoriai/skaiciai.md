# Skaičiai ir kintamieji

Skaičiai yra svarbūs kiekvienam programavimo kalbos programuotojui. Python programavimo kalba palaiko kelis skaičių tipus, kuriuos galite naudoti savo projektuose. Šiame mokomajame faile bus aptariami trys pagrindiniai skaičių tipai: sveikieji skaičiai (`int`), slankiojo kablelio skaičiai (`float`) ir kompleksiniai skaičiai (`complex`).

<br>

## Sveikieji skaičiai (`int`)

Sveikieji skaičiai yra skaičių tipas, naudojamas saugoti sveikus skaičius. Šis tipas gali būti teigiamas, neigiamas arba nulis. Sveiki skaičiai Python programavimo kalboje yra apibrėžiami be skaičių po kablelio.

Štai keletas pavyzdžių, kaip naudoti sveikuosius skaičius Python programavimo kalboje:

```Python
a = 5 
b = -10 
c = 0
```

Kaip matote iš aukščiau pateiktų pavyzdžių, kintamieji gali būti
priskiriami sveikiesiems skaičiams.

<br>

## Slankiojo kablelio skaičiai (`float`)

Slankiojo kablelio skaičiai yra skaičių tipas, naudojamas saugoti
skaičius su kableliu. Šis tipas yra naudojamas matematinėse ir mokslo
programose, kurių reikia didesnės tikslumo paklaidos, negu sveikųjų
skaičių atveju.

Štai keletas pavyzdžių, kaip naudoti slankiojo kablelio skaičius Python
programavimo kalboje:

```Python
a = 3.14 
b = -2.5 
c = 0.0
```

Kaip matote iš aukščiau pateiktų pavyzdžių, kintamieji gali būti
priskiriami slankiojo kablelio skaičiams.

<br>

## Kompleksiniai skaičiai (complex)

Kompleksiniai skaičiai (`complex`) - tai skaičiai, kurie susideda iš realiosios ir įsivaizduojamosios dalies. Jie aprašomi naudojant 'j' raidę kaip įsivaizduojamosios dalies simbolį. Pavyzdžiui: 

```Python
a = 2 + 3j
b =  -4j
c = 1 - 2j
```

Python taip pat turi kai kuriuos papildomus skaičių tipus, tokius kaip `decimal.Decimal`, kuris leidžia atlikti tiksliai apskaičiavimus su slankiojo kablelio skaičiais, ir `fractions.Fraction`, kuris leidžia atlikti operacijas su iracionaliais skaičiais. Daugiau informacijos apie decimal rasite [čia](https://docs.python.org/3/library/decimal.html),  apie fractions - [čia](https://docs.python.org/3/library/fractions.html).

<br>

Norint sukurti kintamąjį su tam tikru skaičių tipu, galite tiesiog priskirti reikšmę su tinkamu tipu, pvz.:

```Python
x = 5        # sveikasis skaičius
y = 3.14     # slankiojo kablelio skaičius
z = 2 + 3j   # kompleksinis skaičius
```

Norint sužinoti kintamojo skaičiaus tipą, galite naudoti type() funkciją, pvz.:

```Python
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>
```
<br>

## Python operacijos su skaičiais

Pagrindinės operacijos yra:

1. Sudėties operacija (+) - naudojama sumuoti du ar daugiau skaičių. Pavyzdžiui:

```Python
x = 5 + 3
print(x)  # 8
```
2. Atimties operacija (-) - naudojama atimti du ar daugiau skaičių. Pavyzdžiui:

```Python
y = 10 - 4
print(y)  # 6
```
3. Daugybos operacija (*) - naudojama padauginti du ar daugiau skaičių. Pavyzdžiui:

```Python
z = 2 * 3
print(z)  # 6
```
4. Dalybos operacija (/) - naudojama padalinti vieną skaičių iš kito. Pavyzdžiui:

```Python
a = 10 / 2
print(a)  # 5.0
```
❗Pastebėkite, kad dalybos operacija grąžina slankiojo kablelio skaičių, net jei pirmasis skaičius yra dalijamas be liekanos. Jei norite gauti sveikąjį skaičių kaip rezultatą, galite naudoti šalutinę dalybos operaciją (//), kuri grąžina sveikąją dalį. Pavyzdžiui:

```Python
b = 10 // 3
print(b)  # 3
```
❗Pastebėkite, kad šalutinė dalybos operacija grąžina sveikąjį skaičių, taigi jei vienas iš skaičių yra slankiojo kablelio skaičius, grąžinamas rezultatas bus apvalintas į mažesnę sveikąją dalį.

5. Liekana (%) - naudojama gauti likučius po dalijimo. Pavyzdžiui:

```Python
c = 10 % 3
print(c)  # 1
```
6. Keliamoji laipsnio operacija (**) - naudojama pakelti skaičių į tam tikrą laipsnį. Pavyzdžiui:

```Python
d = 2 ** 3
print(d)  # 8
```
<br>

# Užduotys

### Pirma užduotis

- Sukurkite kintamąjį a ir priskirkite jam bet kokį sveikąjį skaičių.
- Sukurkite kitą kintamąjį b ir priskirkite jam bet kokį slankiojo kablelio skaičių.
- Tada sukurkite trečią kintamąjį c ir priskirkite jam bet kokį kompleksinį skaičių. 
- Atspausdinkite visus tris kintamuosius ir patikrinkite jų tipus.

### Antra užduotis

- Sukurkite kintamuosius x, y ir z ir priskirkite jiems atitinkamai sveikąjį skaičių, slankiojo kablelio skaičių ir kompleksinį skaičių. 
- Atlikite sudėties operaciją su kintamaisiais x ir y ir išsaugokite rezultatą kintamajame result1.
- Atlikite atimties operaciją su kintamaisiais y ir z ir išsaugokite rezultatą kintamajame result2.
- Atlikite daugybos operaciją su kintamaisiais x, y ir z ir išsaugokite rezultatą kintamajame result3. 
- Atlikite dalybos operaciją su kintamaisiais x ir y ir išsaugokite rezultatą kintamajame result4.
- Atlikite keliamosios laipsnio operaciją su kintamaisiais x ir z ir išsaugokite rezultatą kintamajame result5. 
- Atspausdinkite visus penkis rezultatus.

### Trečia užduotis

- Sukurkite kintamąjį a ir priskirkite jam bet kokį sveikąjį skaičių. 
- Sukurkite kintamąjį b ir priskirkite jam bet kokį slankiojo kablelio skaičių.
- Atlikite šalutinę dalybos operaciją su kintamaisiais a ir b ir išsaugokite rezultatą kintamajame result1. 
- Atlikite liekanos operaciją su kintamaisiais a ir b ir išsaugokite rezultatą kintamajame result2. Atspausdinkite abu rezultatus.

# Atsakymai į užduotis
<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
  <summary>Pirma užduotis</summary>
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
  <p>Output: </p>

```Python
5 <class 'int'>
3.14 <class 'float'>
(2+3j) <class 'complex'>
```
</details>
<details>
  <summary>Antra užduotis</summary>
  <hr>

```Python
x = 10
y = 2.5
z = 4 + 2j

result1 = x + y
result2 = y - z
result3 = x * y * z
result4 = x / y
result5 = x ** z

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
```
<p>Output: </p>

```Python
12.5
(-1.5-2j)
(100+50j)
4.0
(-95.06424688018397+34.92320580341538j)
```
</details>
<details>
  <summary>Trečia užduotis</summary>
  <hr>

```Python
a = 10
b = 3.5

result1 = a // b
result2 = a % b

print(result1)
print(result2)
```
<p>Output: </p>

```Python
2.0
0.5
```
</details>
</details>