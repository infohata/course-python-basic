# ciklai `while`

`while` ciklas leidžia kurti kartojamus procesus, kol nurodyta sąlyga yra teisinga.

Sąlyga yra logiškas reiškinys, kuris yra tikrinamas prieš kiekvieną ciklo vykdymą. Jei sąlyga yra teisinga, kodo blokas tarp `while` ir žymės `:` yra vykdomas. Jei sąlyga tampa neteisinga, vykdymas nutraukiamas ir programa tęsia vykdymą nuo žymės `:` po `while` ciklo. Pvz.:

```Python
skaicius = 1
while skaicius <= 5:
    print(skaicius)
    skaicius = skaicius + 1
```

Rezultatas:

```Text
1
2
3
4
5
```

Šioje programoje `while` ciklas kartojasi, kol kintamasis skaičius yra mažesnis arba lygus 5. Kiekvieną kartą, kai ciklas kartojasi, spausdiname skaičių ir padidiname jį vienetu.

## Begalinis ciklas (`infinite loop`)

Begalinis ciklas kartojasi be pabaigos, nes sąlyga, kurią tikrina ciklas, visada yra teisinga. Tai gali būti neigiamai paveikti programos veikimą, nes begalinis ciklas gali sukelti programos sustojimą ar net viso kompiuterio  užstrigimą.

Šioje programoje `while` ciklas niekada nesibaigs, nes sąlyga `True` yra visada teisinga:

```Python
while True:
    print('Ciklas tęsiasi')

# Ciklas tęsiasi
# Ciklas tęsiasi
# Ciklas tęsiasi
# Ciklas tęsiasi
# Ciklas tęsiasi
# Ciklas tęsiasi
# Ciklas tęsiasi
# ...
```

Tam, kad išvengtumėte begalinių ciklų, turite užtikrinti, kad ciklas turėtų galutinę sąlygą, kuri pasibaigs kai reikia. Pavyzdžiui, jei naudojate `while` ciklą, įsitikinkite, kad jis yra su tiksliomis pradinio ir galutinio kintamojo reikšmėmis arba kitomis galutinėmis sąlygomis.

## Ciklo nutraukimas su `break`

Ciklo nutraukimas leidžianti nutraukti ciklą iki jo paprastai numatytos pabaigos. Tai yra naudinga, jeigu norite nutraukti ciklą, kai įvykdoma tam tikra sąlyga arba kai jūsų programa negali tinkamai veikti, jei ciklas vykdomas per ilgai.

Naudojant `break` ciklas iškart sustoja, o programa tęsia vykdymą iš kito kodo bloko, kuris seka po ciklo. Pvz.:

```Python
skaicius = 0
while skaicius < 10:
    skaicius += 1
    if skaicius >= 5:
        break
    print(skaicius)
```

Rezultatas:

```Text
1
2
3
4
```

❗ Svarbu prisiminti, kad `break` yra naudojamas tik cikle, kuriame yra vykdomi tam tikri veiksmai, ir kad jis turi būti naudojamas atsargiai, kad nebūtų nutrauktas per daug anksti arba per dažnai.

## Žingsnio praleidimas su `continue`

Žingsio praleidimas leidžia praleisti dabartinę ciklo iteraciją ir tęsti kitą iteraciją. Tai yra naudinga, jeigu norite praleisti ciklo žingsnį ar jo dalį, kai įvykdoma tam tikra sąlyga, ir tęsti su kitu ciklo elementu. Pvz.:

```Python
skaicius = 0
while skaicius < 10:
    skaicius += 1
    if skaicius == 5:
        continue
    print(skaicius)
```

Rezultatas:

```Text
1
2
3
4
6
7
8
9
10
```

## `while` ciklas su `else` bloku

`while` ciklas gali būti naudojamas su `else` bloku, kuris bus vykdomas, kai ciklo sąlyga tampa netiesa ir ciklas baigiasi natūraliai. Tai gali būti naudinga, kai norite įvykdyti tam tikrus veiksmus tik tada, kai ciklas baigiasi. Pvz.:

```Python
skaicius = 0
while skaicius < 5:
    print(skaicius)
    skaicius += 1
else:
    print("Ciklas baigtas")
```

Rezultatas:

```Text
0
1
2
3
4
Ciklas baigtas
```

❗ Svarbu prisiminti, kad `else` blokas su `while` ciklu gali būti naudojamas tik tada, kai ciklas baigiasi natūraliai, o ne kai jis yra nutraukiamas su `break`.

## Užduotys

### Pirma užduotis

- Turite skaičių lygų 10. Atspausdinkite skaičiaus mažinimo ciklą, kol jis pasieks -1.

### Antra užduotis

- Turite skaičių lygų 5. Atspausdinkite skaičiaus mažinimo ciklą, kol jis pasieks -10, tačiau sustabdykite ciklą, kai skaičius bus lygus -5, bet pratęskite, jeigu skaičius bus lygus 0.

### Trečia užduotis

Parašyti programą, kuri:

- Leistų vartotojui įvesti skaičių.
- Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
- Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą

Patarimas: Naudoti ciklą while, sąlygą if, break

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
skaicius = 10
while skaicius >= -1:
    print(skaicius)
    skaicius -= 1
```

Rezultatas

```Text
10
9
8
7
6
5
4
3
2
1
0
-1
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
skaicius = 5
while skaicius >= -10:
    skaicius -= 1
    if skaicius == -5:
        print('Sustabdomas ciklas, nes pasiektas skaičius -5')
        break
    elif skaicius == 0:
        print('Pratęsiame ciklą, nes pasiektas skaičius 0')
        continue
    print(skaicius)
```

Rezultatas

```Text
4
3
2
1
Pratęsiame ciklą, nes pasiektas skaičius 0
-1
-2
-3
-4
Sustabdomas ciklas, nes pasiektas skaičius -5
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
suma = 0

while True:
    skaicius = int(input('Įveskite skaičių: '))
    if skaicius < 0:
        break
    suma += skaicius

print(suma)
```

</details>
</details>
