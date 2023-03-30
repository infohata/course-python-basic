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

Sukurkite kintamuosius x, y ir z ir priskirkite jiems atitinkamai sveikąjį skaičių, slankiojo kablelio skaičių ir kompleksinį skaičių. Tada su jais atlikite:

- sudėties operaciją su kintamaisiais x ir y ir išsaugokite rezultatą kintamajame atsakymas1.
- atimties operaciją su kintamaisiais x ir y ir išsaugokite rezultatą kintamajame atsakymas2.
- daugybos operaciją su kintamaisiais x, y ir y ir išsaugokite rezultatą kintamajame atsakymas3.
- dalybos operaciją su kintamaisiais x ir y ir išsaugokite rezultatą kintamajame atsakymas4.
- keliamosios laipsnio operaciją su kintamaisiais x ir y ir išsaugokite rezultatą kintamajame atsakymas5.

Atspausdinkite visus penkis rezultatus.

### Antra užduotis

Iššūkis 💡: Perdarykite pirmąją užduotį, tik vietoj kintamojo y panaudokite z kintamąjį.

### Trečia užduotis

- Sukurkite kintamąjį a ir priskirkite jam bet kokį sveikąjį skaičių.
- Sukurkite kintamąjį b ir priskirkite jam bet kokį slankiojo kablelio skaičių.
- Atlikite šalutinę dalybos operaciją su kintamaisiais a ir b ir išsaugokite rezultatą kintamajame atsakymas1.
- Atlikite liekanos operaciją su kintamaisiais a ir b ir išsaugokite rezultatą kintamajame atsakymas2. Atspausdinkite abu rezultatus.

# Atsakymai į užduotis
<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
x = 10
y = 2.5
z = 4 + 2j

atsakymas1 = x + y
atsakymas2 = x - y
atsakymas3 = x * y * y
atsakymas4 = x / y
atsakymas5 = x ** y

print(atsakymas1)
print(atsakymas2)
print(atsakymas3)
print(atsakymas4)
print(atsakymas5)
```
<p>Rezultatas: </p>

```
12.5
7.5
62.5
4.0
316.22776601683796
```
</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
x = 10
y = 2.5
z = 4 + 2j

atsakymas1 = x + z
atsakymas2 = x - z
atsakymas3 = x * z * z
atsakymas4 = x / z
atsakymas5 = x ** z

print(atsakymas1)
print(atsakymas2)
print(atsakymas3)
print(atsakymas4)
print(atsakymas5)
```
<p>Rezultatas: </p>

```
(14+2j)
(6-2j)
(120+160j)
(2-1j)
(-1070.1348355876978-9942.575694137897j)
```
</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
a = 10
b = 3.5

atsakymas1 = a // b
atsakymas2 = a % b

print(atsakymas1)
print(atsakymas2)
```
<p>Rezultatas: </p>

```
2.0
0.5
```
</details>
</details>