# Python operacijos su skaičiais

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
6. Keliamoji laipsnio operacija (**) - naudojama pakelti skaičių į tam tikru laipsniu. Pavyzdžiui:

```Python
d = 2 ** 3
print(d)  # 8
```

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
  <p>Rezultatas: </p>

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

rezultatas1 = x + y
rezultatas2 = y - z
rezultatas3 = x * y * z
rezultatas4 = x / y
rezultatas5 = x ** z

print(rezultatas1)
print(rezultatas2)
print(rezultatas3)
print(rezultatas4)
print(rezultatas5)
```
<p>Rezultatas: </p>

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

rezultatas1 = a // b
rezultatas2 = a % b

print(rezultatas1)
print(rezultatas2)
```
<p>Rezultatas: </p>

```Python
2.0
0.5
```
</details>
</details>