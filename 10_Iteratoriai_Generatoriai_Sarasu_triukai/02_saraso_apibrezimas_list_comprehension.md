# Sąrašo apibrėžimas (List comprehension)

List comprehension yra trumpas būdas kurti sąrašus naudojant `for` ciklą ir galimą sąlygą.

## Sąrašo kėlimas laipsniu

```Python
skaiciai = [1, 2, 3, 4, 5]
laipsniai = 3
pakelta_skaiciai = [x ** laipsniai for x in skaiciai]
print(pakelta_skaiciai)  # Rezultatas: [1, 8, 27, 64, 125]
```

## Sąrašo filtravimas pagal loginę sąlygą

```Python
skaiciai = [1, 2, 3, 4, 5]
salyga = lambda x: x % 2 == 0
filtruoti_skaiciai = [x for x in skaiciai if salyga(x)]
print(filtruoti_skaiciai)  # Rezultatas: [2, 4]
```

## Sąrašo apibrėžimas pritaikant lambda funkciją

```Python
skaiciai = [1, 2, 3, 4, 5]
dvigubas_skaiciai = [(lambda x: x * 2)(x) for x in skaiciai]
print(dvigubas_skaiciai)  # Rezultatas: [2, 4, 6, 8, 10]
```

## Sąrašo apibrėžimo pakeitimas generatoriaus apibrėžimu

```Python
skaiciai = [1, 2, 3, 4, 5]
laipsniai = 3
pakelta_skaiciai_gen = (x ** laipsniai for x in skaiciai)

for pakeltas in pakelta_skaiciai_gen:
    print(pakeltas)

# Rezultatas:
# 1
# 8
# 27
# 64
# 125
```
