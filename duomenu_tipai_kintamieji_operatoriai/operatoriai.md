# Operatoriai

## Matematiniai operatoriai

1. Sumavimo operatorius (+) - naudojamas skaičių sumai gauti:

```Python
a = 5
b = 10
c = a + b
print(c) # spausdina 15
```
2. Atimties operatorius (-) - naudojamas skaičių skirtumui gauti:

```Python
a = 10
b = 5
c = a - b
print(c) # spausdina 5
```

3. Dauginimo operatorius (*) - naudojamas skaičių sandaugai gauti.:

```Python
a = 2
b = 3
c = a * b
print(c) # spausdina 6
```

4. Dalybos operatorius (/) - naudojamas skaičių dalijimui:

```Python
a = 10
b = 2
c = a / b
print(c) # spausdina 5.0 (dėl skaičių tipų konversijos)
```

5. Liekanos operatorius (%) - naudojamas gauti liekaną, kai vienas skaičius dalinamas iš kito:

```Python
a = 10
b = 3
c = a % b
print(c) # spausdina 1 (nepamirškite, kad liekana yra skaičius, gaunamas dalinant pirmąjį skaičių iš antrojo)
```
6. Kelimo laipsniu operatorius (**) - naudojamas skaičių kėlimui laipsniu:

```Python
a = 2
b = 3
c = a ** b
print(c) # spausdina 8
```

## if ir else sąlyginis sakinys

`if` ir `else` yra Python programavimo kalbos sąlyginio sakinio komponentai, kurie leidžia programai priimti sprendimus pagal tam tikras sąlygas:

```Python
if <sąlyga>:
    <vykdomos komandos, jei sąlyga tenkinama>
else:
    <vykdomos komandos, jei sąlyga netenkinama>
```

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

## Loginiai operatoriai

1. "Ir" operatorius (and) - naudojamas patikrinti, ar abu teiginiai yra tiesa:

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

2. "Arba" operatorius (or) - naudojamas patikrinti, ar bent vienas teiginys yra tiesa:

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

3. "Ne" operatorius (not) - naudojamas pakeisti teiginio reikšmę iš tiesa į netiesa arba atvirkščiai:

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
# Paprašome vartotojo įvesti savo vardą
vardas = input("Įveskite savo vardą: ")

# Spausdiname pasisveikinimo žinutę su vartotojo įvestu vardu
print("Sveiki, " + vardas + "!")

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

- Parašykite programą, kuri nustatytų, ar vartotojo įvestas skaičius yra teigiamas, naudodama daugiau operatorių. Jei skaičius yra teigiamas, turi būti spausdinamas pranešimas "Skaičius yra teigiamas", o jei ne - "Skaičius yra neigiamas".

### Antra užduotis

- Parašykite programą, kuri patikrintų, ar vartotojo įvestas skaičius yra tarp 5 ir 10, naudodama mažiau arba lygu operatorių. Jei skaičius yra tarp 5 ir 10, turi būti spausdinamas pranešimas "Skaičius yra tarp 5 ir 10", o jei ne - "Skaičius nėra tarp 5 ir 10".

### Trečia užduotis

- Parašykite programą, kuri nustatytų, ar vartotojo įvestas skaičius yra lyginis, naudodama nelygybės operatorių. Jei skaičius yra lyginis, turi būti spausdinamas pranešimas "Skaičius yra lyginis", o jei ne - "Skaičius yra nelyginis".

### Ketvirta užduotis

- Parašykite programą, kuri patikrintų, ar du skaičiai yra didesni nei 0, naudodama "ir" operatorių. Jei abu skaičiai yra didesni nei 0, turi būti spausdinamas pranešimas "Abu skaičiai yra didesni nei 0", o jei ne - "Bent vienas skaičius yra neigiamas arba lygus 0".

### Penkta užduotis

- Parašykite programą, kuri nustatytų, ar bent vienas duotų skaičių yra lyginis, naudodama "arba" operatorių. Jei bent vienas skaičius yra lyginis, turi būti spausdinamas pranešimas "Bent vienas skaičius yra lyginis", o jei ne - "Abu skaičiai yra nelyginiai".


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
# Paprašome vartotojo įvesti skaičių
a = int(input("Įveskite skaičių: "))

# Patikriname, ar skaičius yra lyginis
if a % 2 == 0:
    print("Skaičius yra lyginis")
else:
    print("Skaičius yra nelyginis")
```
</details>
<details>
  <summary>Ketvirta užduotis</summary>
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
  <summary>Penkta užduotis</summary>
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