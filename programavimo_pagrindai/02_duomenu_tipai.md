# Skaičiai

Skaičiai yra svarbūs kiekvienam programavimo kalbos programuotojui. Python programavimo kalba palaiko kelis skaičių tipus, kuriuos galite naudoti savo projektuose. Šiame mokomajame faile bus aptariami trys pagrindiniai skaičių tipai: sveikieji skaičiai (`int`), slankiojo kablelio skaičiai (`float`) ir kompleksiniai skaičiai (`complex`).

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

## Kompleksiniai skaičiai (complex)

Kompleksiniai skaičiai (`complex`) - tai skaičiai, kurie susideda iš realiosios ir įsivaizduojamosios dalies. Jie aprašomi naudojant 'j' raidę kaip įsivaizduojamosios dalies simbolį. Pavyzdžiui: 

```Python
a = 2 + 3j
b =  -4j
c = 1 - 2j
```

Python taip pat turi kai kuriuos papildomus skaičių tipus, tokius kaip `decimal.Decimal`, kuris leidžia atlikti tiksliai apskaičiavimus su slankiojo kablelio skaičiais, ir `fractions.Fraction`, kuris leidžia atlikti operacijas su iracionaliais skaičiais. Daugiau informacijos apie decimal rasite [čia](https://docs.python.org/3/library/decimal.html),  apie fractions - [čia](https://docs.python.org/3/library/fractions.html).

Norint sukurti kintamąjį su tam tikru skaičių tipu, galite tiesiog priskirti reikšmę su tinkamu tipu, pvz.:

```Python
x = 5        # sveikasis skaičius
y = 3.14     # slankiojo kablelio skaičius
z = 2 + 3j   # kompleksinis skaičius
```