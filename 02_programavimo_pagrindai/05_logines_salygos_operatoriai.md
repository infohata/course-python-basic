# Operatoriai

## if ir else sąlyginis sakinys

`if`, `elif`, `else` yra Python programavimo kalbos sąlyginio sakinio komponentai, kurie leidžia programai priimti sprendimus pagal tam tikras sąlygas:

```Python
if <sąlyga1>:
    <komandos, jei sąlyga1 tenkinama>
elif <sąlyga2>:
    <komandos, jei sąlyga2 tenkinama>
elif <sąlyga3>:
    <komandos, jei sąlyga3 tenkinama>
else:
    <komandos, jei nei viena sąlyga netenkinama>
```
Kai `if` sąlyga yra netenkinama, Python patikrina kiekvieną `elif` sąlygą iš eilės, kol randama pirmoji tenkinama sąlyga. Jei nėra tenkinamos sąlygos, vykdomos komandos nurodytos else sakinio dalimi.

## Palyginimo operatoriai

1. Lygybės operatorius (==) - naudojamas patikrinti, ar du objektai yra lygūs:

```Python
a = 10
b = 5
if a == b:
    print("a ir b yra lygūs")
else:
    print("a ir b nėra lygūs")
```

2. Nelygybės operatorius (!=) - naudojamas patikrinti, ar du objektai nelygūs:

```Python
a = 10
b = 5
if a != b:
    print("a ir b yra nelygūs")
else:
    print("a ir b yra lygūs")
```

3. Daugiau operatorius (>) - naudojamas patikrinti, ar vienas skaičius didesnis už kitą:

```Python
a = 10
b = 5
if a > b:
    print("a yra didesnis nei b")
else:
    print("a yra mažesnis arba lygus b")
```

4. Mažiau operatorius (<) - naudojamas patikrinti, ar vienas skaičius mažesnis už kitą: 

```Python
a = 10
b = 5
if b < a:
    print("b yra mažesnis nei a")
else:
    print("b yra didesnis arba lygus a")
```

5. Daugiau arba lygu operatorius (>=) - naudojamas patikrinti, ar vienas skaičius didesnis arba lygus kitam:

```Python
a = 10
b = 5
if a >= b:
    print("a yra didesnis arba lygus b")
else:
    print("a yra mažesnis nei b")
```

6. Mažiau arba lygu operatorius (<=) - naudojamas patikrinti, ar vienas skaičius mažesnis arba lygus kitam:

```Python
a = 10
b = 5
if b <= a:
    print("b yra mažesnis arba lygus a")
else:
    print("b yra didesnis nei a")
```

## Boolean tipo kintamasis

Tai kintamasis, kuris gali turėti tik dvi reikšmes: `True` arba `False`. Tai reikš, kad boolean tipo kintamasis gali būti naudojamas kaip tikslinė reikšmė, kuri atitinka tikrąją arba netikrąją reikšmę.

Pavyzdys:

```Python
x = True
y = False

print(x) # išvestų "True"
print(y) # išvestų "False"
```
Pavyzdys:

```Python
a = 10
b = 5

if a > b:
    print("a yra didesnis už b")
else:
    print("a yra mažesnis arba lygus b")
```
Šiame pavyzdyje if sąlyginis saknis naudoja boolean tipo kintamąjį, kad nustatytų, ar kintamasis a yra didesnis už kintamąjį b. Jei sąlyga yra tenkinama, išvedamas pranešimas "a yra didesnis už b". Jei sąlyga netenkinama, išvedamas pranešimas "a yra mažesnis arba lygus b".

Boolean tipo kintamieji taip pat gali būti sujungti su loginiais operatoriais `and`, `or` ir `not`, kad būtų sudarytos sudėtingesnės sąlygos.

Pavyzdys: 

```Python
x = True
y = False

print(x and y) # išvestų "False"
print(x or y) # išvestų "True"
print(not x) # išvestų "False"
```
Šiame pavyzdyje and operatorius tikrina, ar abu boolean tipo kintamieji yra `True`, ir grąžina `True`, jei abu yra `True`. or operatorius tikrina, ar bent vienas boolean tipo kintamasis yra `True`, ir grąžina `True`, jei bent vienas yra `True`. not operatorius grąžina priešingą boolean tipo kintamojo reikšmę.


## Loginiai operatoriai

1. "Ir" operatorius (`and`) - naudojamas patikrinti, ar abu teiginiai yra tiesa:

```Python
a = True
b = False
c = a and b
print(c) # spausdina False
```
```Python
a = 10
b = 5
if a > 5 and b < 10:
    print("Abu teiginiai yra tiesa")
else:
    print("Vienas ar abu teiginiai yra netiesa")
```

2. "Arba" operatorius (`or`) - naudojamas patikrinti, ar bent vienas teiginys yra tiesa:

```Python
a = True
b = False
c = a or b
print(c) # spausdina True
```
```Python
a = 10
b = 5
if a > 10 or b < 10:
    print("Bent vienas teiginys yra tiesa")
else:
    print("Abu teiginiai yra netiesa")
```

3. "Ne" operatorius (`not`) - naudojamas pakeisti teiginio reikšmę iš tiesa į netiesa arba atvirkščiai:

```Python
a = True
b = not a
print(b) # spausdina False
```
```Python
a = 10
if not a > 5:
    print("Teiginys yra netiesa")
else:
    print("Teiginys yra tiesa")
```

4. Kombinuoti operatoriai - galima naudoti kelis operatorius kartu, kad sudarytumėte sudėtingesnes sąlygas:

```Python
a = 10
b = 5
c = 20
d = a > b and b < c or c == 20
print(d) # spausdina True
```

## Įvadas į užduotis

```Python
# Paprašome vartotojo įvesti savo amžių ir konvertuojame į sveikąjį skaičių
amzius = int(input("Įveskite savo amžių: "))

# Patikriname, ar vartotojo amžius yra didesnis nei 18
if amzius >= 18:
    print("Jūs esate pilnametis(-ė).")
else:
    print("Jūs dar nepilnametis(-ė).")

# Paprašome vartotojo įvesti skaičių ir konvertuojame į skaičių su kableliu
skaicius = float(input("Įveskite skaičių su kableliu: "))

# Spausdiname vartotojo įvestą skaičių su kableliu
print("Jūsų įvestas skaičius yra:", skaicius)
```

# Užduotys

### Pirma užduotis

- Parašykite programą, kuri nustatytų, ar vartotojo įvestas skaičius yra teigiamas, naudodami daugiau operatorių. Jei skaičius yra teigiamas, turi būti spausdinamas pranešimas "Skaičius yra teigiamas", o jei ne - "Skaičius yra neigiamas".

### Antra užduotis

- Parašykite programą, kuri patikrintų, ar vartotojo įvestas skaičius yra tarp 5 ir 10, naudodama mažiau arba lygu operatorių. Jei skaičius yra tarp 5 ir 10, turi būti spausdinamas pranešimas "Skaičius yra tarp 5 ir 10", o jei ne - "Skaičius nėra tarp 5 ir 10".

### Trečia užduotis

- Parašykite programą, kuri patikrintų, ar du skaičiai yra didesni nei 0, naudodami "ir" operatorių. Jei abu skaičiai yra didesni nei 0, turi būti spausdinamas pranešimas "Abu skaičiai yra didesni nei 0", o jei ne - "Bent vienas skaičius yra neigiamas arba lygus 0".

### Ketvirta užduotis

- Parašykite programą, kuri nustatytų, ar bent vienas duotų skaičių yra lyginis, naudodami "arba" operatorių. Jei bent vienas skaičius yra lyginis, turi būti spausdinamas pranešimas "Bent vienas skaičius yra lyginis", o jei ne - "Abu skaičiai yra nelyginiai".


# Atsakymai į užduotis
<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
  <summary>Pirma užduotis</summary>
  <hr>
  
```Python
# Paprašome vartotojo įvesti skaičių
a = int(input("Įveskite skaičių: "))

# Patikriname, ar skaičius yra teigiamas
if a > 0:
    print("Skaičius yra teigiamas")
else:
    print("Skaičius yra neigiamas")
```
</details>
<details>
  <summary>Antra užduotis</summary>
  <hr>

```Python
# Paprašome vartotojo įvesti skaičių
a = int(input("Įveskite skaičių: "))

# Patikriname, ar skaičius yra tarp 5 ir 10
if a >= 5 and a <= 10:
    print("Skaičius yra tarp 5 ir 10")
else:
    print("Skaičius nėra tarp 5 ir 10")
```
</details>
<details>
  <summary>Trečia užduotis</summary>
  <hr>

```Python
# Paprašome vartotojo įvesti du skaičius
a = int(input("Įveskite pirmą skaičių: "))
b = int(input("Įveskite antrą skaičių: "))

# Patikriname, ar abu skaičiai yra didesni nei 0
if a > 0 and b > 0:
    print("Abu skaičiai yra didesni nei 0")
else:
    print("Bent vienas skaičius yra neigiamas arba lygus 0")
```
</details>
<details>
  <summary>Ketvirta užduotis</summary>
  <hr>

```Python
# Paprašome vartotojo įvesti du skaičius
a = int(input("Įveskite pirmą skaičių: "))
b = int(input("Įveskite antrą skaičių: "))

# Patikriname, ar bent vienas skaičius yra lyginis
if a % 2 == 0 or b % 2 == 0:
    print("Bent vienas skaičius yra lyginis")
else:
    print("Abu skaičiai yra nelyginiai")
```
</details>
</details>