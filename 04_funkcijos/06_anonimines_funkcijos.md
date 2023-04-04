# Anoniminės funkcijos

Anoniminės funkcijos yra funkcijos, kurios neturi pavadinimo. Jų apibrėžimas yra sudarytas iš `lambda` raktinio žodžio ir argumentų sąrašo, kurioje gali būti aprašytas tam tikras kodas. Šios funkcijos yra labai naudingos, kai reikia sukurti paprastą funkciją vienoje vietoje, kuria naudosimės tik kartą.

Štai pavyzdys, kaip galima apibrėžti bevardę funkciją Python programavimo kalboje:

```Python
suma = lambda x, y: x + y

print(suma(2, 3)) # išveda 5
```

Šiame pavyzdyje apibrėžiama anoniminė funkcija "suma", kuri suskaičiuoja dviejų argumentų sumą. Ši funkcija yra apibrėžiama naudojant "lambda" raktinį žodį, ir reikšmė yra priskiriama kintamajam "suma". Po to funkcija yra iškviečiama su argumentais "2" ir "3", ir išvesties rezultatas yra "5".

Štai dar vienas pavyzdys:

```Python
skaiciu_kvadratai = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))
print(skaiciu_kvadratai) # išveda [1, 4, 9, 16, 25]
```

Ši anoniminė funkcija `lambda` yra naudojama kartu su `map` funkcija, kad suskaičiuotų kiekvieno sąrašo elemento kvadratą. Tai yra trumpesnis ir patogesnis būdas, nei apibrėžti atskirą funkciją tik skaičių kvadratų skaičiavimui.

Funkcija `map` yra Python vidinė funkcija, kuri naudojama norint sukurti naują sąrašą iš kito sąrašo, keičiant kiekvieną jo elementą pagal tam tikrą funkciją arba anoniminę funkciją.

Pavyzdžiui, kai naudojama anoniminė funkcija `lambda x: x**2`, funkcija `map` pakeičia kiekvieną sąrašo elementą jo kvadratu. Kiekvienam sąrašo elementui, funkcija "lambda" priskiria reikšmę ir paduoda ją į `map` funkciją, kuri tada sudaro naują sąrašą su pakeistais elementais, o `list` funkcija paverčia gautą `map` funkcijos rezultatą sąrašu.

Pabaigoje, sukurtas naujas sąrašas yra išvestas su `print` funkcija.

Galutinis išvesties rezultatas yra naujas sąrašas, kuriame kiekvienas skaičius iš pradinio sąrašo yra pakeltas kvadratu, t.y. [1, 4, 9, 16, 25].

Pavyzdys su `lambda` rikiuojant žodžius pagal jų ilgį:

```Python
zodziai = ['alus', 'baravykas', 'duona', 'cukrus', 'jogurtas']
zodziai_rikiuoti = sorted(zodziai, key=lambda x: len(x))
print(zodziai_rikiuoti) # išveda ['alus', 'duona', 'cukrus', 'jogurtas', 'baravykas']
```

Šioje anoniminėje funkcijoje "lambda" yra naudojama kaip raktinis argumentas funkcijai "sorted" rikiuoti žodžius pagal jų ilgį.

Pavyzdys su `lambda` filtruojant sąrašą pagal tam tikrą sąlygą:

```Python
skaiciai = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lyginiai_skaiciai = list(filter(lambda x: x % 2 == 0, skaiciai))
print(lyginiai_skaiciai) # išveda [2, 4, 6, 8, 10]
```

Ši anoniminė funkcija `lambda` yra naudojama kartu su `filter` funkcija, kad gautų visus sąrašo lyginius skaičius.

Anoniminės funkcijos yra dažnai naudojamos kartu su kitomis funkcijomis, kaip argumentai arba grąžinamos reikšmės. Jos yra lengvai skaitytos ir suprantamos, todėl yra labai naudingos Python programavimo kalboje.

## Užduotys

### Pirma užduotis

Sukurkite anoniminę funkciją, kuri iš sąrašo skaičių pasirenka tik tuos, kurie yra didesni nei 10.

### Antra užduotis

Sukurkite anoniminę funkciją, kuri grąžina sąrašo elementų vidurkį.

### Trečia užduotis
<!-- perkurti, viskskai nonsence. Pigiau tiesiog didziausias = max(x,y,z) -->

Parašykite anoniminę funkciją, kuri grąžina didžiausią skaičių iš duotų trijų skaičių.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
  <summary>Pirma užduotis</summary>
  <hr>
  
```Python
skaiciai = [1, 20, 3, 40, 5, 60, 7, 80, 9, 100]
didziau_nei_10 = list(filter(lambda x: x > 10, skaiciai))
print(didziau_nei_10) # išveda [20, 40, 60, 80, 100]
```

</details>
<details>
  <summary>Antra užduotis</summary>
  <hr>

```Python
skaiciai = [1, 2, 3, 4, 5]
vidurkis = lambda x: sum(x) / len(x)

print(vidurkis(skaiciai)) # išveda 3.0
```

</details>
<details>
  <summary>Trečia užduotis</summary>
  <hr>

```Python
didziausias_skaicius = lambda x, y, z: max(x, y, z)

print(didziausias_skaicius(10, 20, 5)) # išveda 20
```

</details>
</details>
