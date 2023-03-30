# Simbolių eilutės

## Simbolių eilutės kūrimas

```Python
string1 = 'Labas, pasauli!'
string2 = "Kaip sekasi?"
```

## Simbolių ištraukimas

Galite gauti tam tikrus simbolius iš simbolių eilutės naudodami kvadratinius skliaustus ir nurodydami, kuriose pozicijose norite gauti simbolius. Skliausteliuose nurodoma pozicija pradedant nuo 0. Taigi, jei norite gauti pirmąjį simbolį, nurodykite 0, antrasis simbolis būtų 1, ir t.t.

```Python
string = 'Labas, pasauli!'
print(string[0]) # Išveda 'L'
print(string[1]) # Išveda 'a'
print(string[-1]) # Išveda '!'
```

❗Pastaba: Naudokite neigiamus skaičius, kad gautumėte simbolius nuo galo. Pavyzdžiui, -1 reiškia paskutinį simbolį, -2 reiškia antrą nuo paskutinio, ir t.t.

## Simbolių keitimas

Simbolių eilutę galite keisti, naudodami = operatorių. Tai gali būti naudinga, jei norite pakeisti tam tikrus simbolius arba visą simbolių eilutę.

```Python
string = 'Labas, pasauli!'
string = string[:5] + ' rytas' + string[5:]
print(string) # Išveda 'Labas rytas, pasauli!'
```

❗Pastaba: Šiuo atveju string[:5] reiškia simbolių eilutę nuo pradžios iki 5 pozicijos, o string[5:] reiškia simbolių eilutę nuo 5 pozicijos iki pabaigos.

❗Pastaba: atkreipkite dėmesį, kad po žodžio labas prieš kablelį nėra tarpo, todėl norint įterpti žodį "rytas", prieš jį reikia įterpri ir tarpą " ".

## Simbolių skaidymas (slicing)

Galite gauti tam tikrą dalį simbolių eilutės, naudodami slicing (skaidymo) operatorių :. Šis operatorius leidžia nurodyti, kuriuos simbolius reikia ištraukti. Pvz., string[start:stop] gautų simbolius nuo pozicijos start iki pozicijos stop - 1.

```Python
string = 'Labas, pasauli!'
print(string[0:5]) # Išveda 'Labas'
print(string[7:]) # Išveda 'pasauli!'
print(string[:5]) # Išveda 'Labas'
```

❗Pastaba: Jei nenurodoma start reikšmė, slicing prasideda nuo pradžios. Jei nenurodoma stop reikšmė, slicing baigiasi iki pabaigos.

## Simbolių eilutės ilgis

Jei norite sužinoti, kiek simbolių yra simbolių eilutėje, galite naudoti funkciją len().

```Python
string = 'Labas, pasauli!'
print(len(string)) # Išveda 15
```

## Nauja eilutė, tabuliacija ir Unicode simboliai

Naujos eilutės pavyzdys:

```Python
print("Labas\nPasauli")
```

Rezultatas:

```Text
Labas
Pasauli
```

Šiame pavyzdyje "\n" yra naujos eilutės simbolis. Jis pasako programai, kad teksto eilutę reikia padalinti ir pradėti naują eilutę.

Tabuliacijos pavyzdys:

```Python
print("Vardas\tAmžius\tMiestas")
print("Tomas\t25\tVilnius")
print("Monika\t28\tKaunas")
```

Rezultatas:

```Text
Vardas  Amžius  Miestas
Tomas   25      Vilnius
Monika  28      Kaunas
```

Šiame pavyzdyje "\t" yra tab simbolis. Jis naudojamas padaryti tam tikrą atstumą tarp skirtingų teksto eilučių.

Unicode simbolių pavyzdys:

```Python
print("\u00A9 2023 OpenAI")
```

Rezultatas:

```Python
© 2023 OpenAI
```

Šiame pavyzdyje "\u00A9" yra Unicode simbolis, kuris atitinka copyright simbolį.

Jei norite pamatyti visus Unicode simbolius, galite naudoti Unicode kodo lentelę, kuri pateikia sąrašą visų galimų simbolių kartu su jų skaitiniais kodais: http://unicode-table.com.

💡 Gerai žinoti: galima tekste naudoti ir emoji, pvz. šią lemputę, jeigu jūsų naudojamas šriftas juos palaiko.

## Simbolių eilučių metodai

```Python
# Sukuriamas tekstas
sakinys = "Labas, pasauli!"

# Upper metodas: pakeičia visas raides didžiosiomis raidėmis
didziosios_raides = sakinys.upper()

# Lower metodas: pakeičia visas raides mažosiomis raidėmis
mazosios_raides = sakinys.lower()

# Join metodas: sujungia eilučių sąrašą į vieną eilutę
zodziu_sarasas = ["Labas", "pasauli", "!"]
eilute = " ".join(zodziu_sarasas)

# Split metodas: skaido eilutę pagal nurodytą skyriklį ir grąžina sąrašą
zodziu_sarasas = sakinys.split(", ")

# Find metodas: ieško nurodytos frazės ir grąžina jos poziciją
pozicija = sakinys.find("pasauli")

# Replace metodas: pakeičia nurodytą frazę kitu tekstu
pakeistas_tekstas = sakinys.replace("Labas", "Sveiki")

# Spausdiname pradinę eilutę ir jos pakeistus variantus
print("Pradinis tekstas: ", sakinys)
print("Upper metodas: ", didziosios_raides)
print("Lower metodas: ", mazosios_raides)
print("Join metodas: ", eilute)
print("Split metodas: ", zodziu_sarasas)
print("Find metodas: ", pozicija)
print("Replace metodas: ", pakeistas_tekstas)
```

Ši programa išvestų šiuos rezultatus:

```Text
Pradinis tekstas: Labas, pasauli!
Upper metodas: LABAS, PASAULI!
Lower metodas: labas, pasauli!
Join metodas: Labas pasauli!
Split metodas: ['Labas', 'pasauli!']
Find metodas: 7
Replace metodas: Sveiki, pasauli!
```

❗Pastaba: atsargiai naudokite `.find()` rezultatus loginėse išraiškose. Pvz.

```Python
tekstas = "Labas pasauli"
if tekstas.find("pasauli"):
    print("radau pasauli")
else:
    print("neradau pasauli")
if tekstas.find("Labas"):
    print("radau Labas")
else:
    print("neradau Labas")
```

Rezultatas:

```Text
radau pasauli
neradau Labas
```

Taip gaunasi todėl, kad paieškos rezultatas yra nulis, o konvertuojant tarp kintamųjų tipų `int` ir `bool`, nulis yra False.

```Python
print(tekstas.find("Labas"))
print(0 == True)
print(0 == False)
```

```Text
0
False
True
```

Teisingas naudojimas `.find()` metodo sąlygoje būtų tikrinti, ar randama reikšmė yra neneigiama

```Python
if tekstas.find("Labas") >= 0:
    print("radau Labas")
else:
    print("neradau Labas")
# radau Labas
```

## Formatavimas

Formatavimas yra svarbi programavimo koncepcija, leidžianti kurti teksto eilutes su kintamaisiais arba reikšmėmis, kurios gali būti pateikiamos įvairiais būdais.

### Konkatenacija (`+`)

Konkatenacija yra paprasčiausias būdas sujungti tekstą su kintamaisiais. Norint pridėti kintamąjį prie teksto, tiesiog naudojamas pliuso simbolis. Pavyzdžiui:

```Python
vardas = "Jonas"
amzius = 25

tekstas = "Sveiki, mano vardas yra " + vardas + " ir man yra " + str(amzius) + " metai."
print(tekstas)
```

Rezultatas:

```Python
Sveiki, mano vardas yra Jonas ir man yra 25 metai.
```

Šiame pavyzdyje teksto eilutė sukurta sujungiant atskirus tekstus ir kintamuosius. Reikia atkreipti dėmesį, kad skaičius amzius buvo konvertuotas į eilutę naudojant str() funkciją.

### `f'` eilučių formatas

`f'` eilučių formatas yra formatavimo metodas, leidžiantis sukurti tekstą su kintamaisiais tiesiogiai eilutėje. Norint pridėti kintamąjį, tiesiog reikia naudoti `f'` simbolį ir įdėti kintamojo pavadinimą į skliaustus. Pavyzdžiui:

```Python
vardas = "Jonas"
amzius = 25

tekstas = f"Sveiki, mano vardas yra {vardas} ir man yra {amzius} metai."
print(tekstas)
```

Rezultatas:

```Text
Sveiki, mano vardas yra Jonas ir man yra 25 metai.
```

Šiame pavyzdyje naudojamas f' formatas, kad tiesiogiai eilutėje būtų pridėti kintamieji. Nereikia konvertuoti skaičiaus į eilutę, nes f' formatas tai padarys už jus.

### `%` simbolio formatas

`%` simbolio formatas yra senesnis formatavimo būdas, kuris naudojamas Python 2 ir ankstyvose Python 3 versijose. Norint suformatuoti tekstą su kintamaisiais, reikia naudoti `%` simbolį ir specifikuoti kintamųjų tipus ir reikšmes. Pavyzdžiui:

```Python
vardas = "Jonas"
amzius = 25

tekstas = "Sveiki, mano vardas yra %s ir man yra %d metai." % (vardas, amzius)
print(tekstas)
```

Rezultatas:

```Text
Sveiki, mano vardas yra Jonas ir man yra 25 metai.
```

Šiame pavyzdyje `%` simbolio formatas naudojamas norint pridėti kintamuosius prie tekstinių eilučių. `%s` simbolis yra naudojamas teksto reikšmėms formatuoti, o `%d` simbolis - sveikojo skaičiaus reikšmėms formatuoti. Kintamieji yra perduodami kaip argumentai, t.y., jie yra sudedami į skliaustus, atskirtus kableliais.

### `.format()` metodas

`.format()` metodas yra dar vienas formatavimo būdas, kuris yra naudojamas Python 2 ir Python 3 versijose. Norint pridėti kintamąjį prie teksto, tiesiog naudojamas {} skliaustas ir `.format()` metodas. Pavyzdžiui:

```Python
vardas = "Jonas"
amzius = 25

tekstas = "Sveiki, mano vardas yra {} ir man yra {} metai.".format(vardas, amzius)
print(tekstas)
```

Rezultatas:

```Text
Sveiki, mano vardas yra Jonas ir man yra 25 metai.
```

Šiame pavyzdyje naudojamas `.format()` metodas, kad būtų pridėti kintamieji prie teksto. Toliau šie kintamieji yra perduodami kaip parametrai, perduodami {} skliaustams.

Rekomenduojame naudoti naujesnius formatavimo būdus, tokius kaip `f'` formatas ar `.format()` metodas, nes jie yra lengvesni ir geresni nei senesni būdai, tokių kaip konkatenacija ar `%` simbolio formatas. Tačiau visi šie formatavimo metodai yra naudingi ir vertingi, todėl verta išmokti juos visus.

## Skaičių formatavimas įvairiais būdais naudojant `f'` formatą

### Realieji skaičiai (su kableliais)

Pavyzdžiui, norint formatuoti skaičių su kableliais, galite naudoti tūkstančių skirtukus `,.` Šis formatavimo raktas veikia su skaičiais ir `float` tipo skaičiais.

```Python
skaicius = 1234567.89
print(f"suformatuotas skaicius: {skaicius:,.2f}")
```

Rezultatas:

```Text
suformatuotas skaicius: 1,234,567.89
```

Šiuo pavyzdžiu skaičius skaicius formatuojamas kaip `float` tipo skaičius su 2 skaičiais po kablelio. Formatuojant skaičių taip pat naudojamas tūkstančių skirtukas `,.`

### Skaičius be nulių po kableliu

Jeigu norite, kad `float` tipo skaičius būtų pateiktas be nulių po kablelio, galite naudoti `g` formatą.

```Python
skaicius = 1234.0
print(f"suformatuotas skaicius: {skaicius:g}")
```

Rezultatas:

```Text
suformatuotas skaicius: 1234
```

### Skaitmenų plotis

Jeigu norite nurodyti skaitmenų plotį, galite naudoti `:` formatavimo raktą su `d` arba `f` formatu. Pavyzdžiui, jei norite, kad skaičius būtų pateiktas su 5 skaitmenimis, įskaitant nulius, galite naudoti formatą `{:05d}`:

```Python
skaicius = 123
print(f"suformatuotas skaicius: {skaicius:05d}")
```

Rezultatas:

```Text
suformatuotas skaicius: 00123
```

Šiuo pavyzdžiu skaičius skaicius formatuojamas kaip sveikasis skaičius su 5 skaitmenimis, o skaitmenys, kurių trūksta, užpildomi nuliais.

Taip pat galite nurodyti skaitmenų plotį ir kablelio skaitmenų plotį `float` tipo skaičiams. Pavyzdžiui, jei norite, kad skaičius būtų pateiktas 10 simbolių plote, iš kurių 2 yra po kablelio, galite naudoti formatą `{:10.2f}`:

```Python
skaicius1 = 1234.5678
skaicius2 = 12345.678
print(f"suformatuotas skaicius: {skaicius1:010.2f}")
print(f"suformatuotas skaicius: {skaicius2:010.2f}")
```

Rezultatas:

```Text
suformatuotas skaicius:   1234.57
suformatuotas skaicius:  12345.68
```

Šiuo pavyzdžiu skaičius skaicius formatuojamas kaip `float` tipo skaičius su 10 skaitmenų pločiu, kuris apima 2 skaitmenis po kablelio. Skaitmenų, kurių trūksta, užpildomi tarpais, o skaičiai po kablelio apvalinami. Taip galima pasiekti gražų įvairių ilgių skaičių lygiavimą ties kableliu

## Kito tipo kintamųjų konvertavimas į `str`

Kintamųjų konvertavimas į `str` tipo kintamąjį yra naudinga funkcija, kai reikia sukurti tekstines eilutes, kuriose reikia įtraukti skaičius ar kitus tipo kintamuosius.

### Skaičių konvertavimas į `str`

Norint konvertuoti skaičių į `str` tipo kintamąjį, galite tiesiog panaudoti str() funkciją. Pavyzdžiui:

```Python
skaicius = 123
skaicius_str = str(skaicius)
print("Skaičius kaip str: " + skaicius_str)
```

Rezultatas:

```Text
Skaičius kaip str: 123
```

Šiuo pavyzdžiu skaičius skaicius konvertuojamas į str tipo kintamąjį skaicius_str naudojant str() funkciją.

### Konvertavimas su formatavimu

Kartais gali prireikti konvertuoti skaičius į str tipo kintamuosius su tam tikru formatavimu. Pavyzdžiui, norint pridėti nulius prie skaičiaus, kad jis atitiktų tam tikrą skaitmenų plotį.

```Python
skaicius = 123
skaicius_str = "{:0>5}".format(skaicius)
print("Skaičius su formatavimu: " + skaicius_str)
```

Rezultatas:

```Text
Skaičius su formatavimu: 00123
```

Šiuo pavyzdžiu skaičius skaicius konvertuojamas į str tipo kintamąjį skaicius_str ir formatuojamas naudojant formatavimo raktą {:0>5}, kuris nustato, kad skaičius turėtų būti pateiktas su 5 skaitmenimis, o skaitmenys, kurių trūksta, turėtų būti užpildyti nuliais.

Galima naudoti ir kitus formatavimo raktus, kad sukurtumėte reikiamą tekstinių eilučių formatą.

## Įvedimas ir išvedimas

### Įvedimas ('input')

`input` funkcija leidžia jums gauti informaciją iš vartotojo ir naudoti ją savo programoje. Pavyzdžiui, jei norite sužinoti vartotojo vardą, galite naudoti `input` funkciją.

Kodas, kuris paprašo vartotojo įvesti savo vardą ir išveda pranešimą su pasisveikinimu:

```Python
name = input("Įveskite savo vardą: ")
print("Sveiki, " + name + "!")
```

Jeigu programoje norite naudoti skaičius, "input" funkcija taip pat gali būti naudojama skaičių įvedimui. Tačiau svarbu prisiminti, kad "input" funkcija visada grąžina tekstą, todėl turite konvertuoti įvestus duomenis į skaičių formatą, jei norite atlikti skaičiavimus.

Kodas, kuris paprašo vartotojo įvesti du skaičius ir atspausdina jų sumą:

```Python
num1 = input("Įveskite pirmąjį skaičių: ")
num2 = input("Įveskite antrąjį skaičių: ")
suma = int(num1) + int(num2)
print("Suma yra: " + str(suma))
```

2. Išvedimas (`print`)

`print` funkcija leidžia jums išvesti informaciją į konsolę arba į failą. Pavyzdžiui, jei norite išvesti pranešimą su tekstiniu turiniu, galite naudoti "print" funkciją.

Kodas, kuris išveda pranešimą su tekstiniu turiniu:

```Python
print("Tai yra pranešimas.")
```

Jeigu norite išvesti kintamąjį arba rezultatą, "print" funkciją galite naudoti kartu su formatavimo simboliais. Pavyzdžiui:

```Python
x = 5
y = 10
sum = x + y
print("Pirma reikšmė: {}, antra reikšmė: {}, suma: {}".format(x, y, sum))
```

Šis kodas išvestų pranešimą, kuriame būtų pateikta pirmoji reikšmė, antra reikšmė ir jų suma.

Todėl, "input" ir "print" funkcijos yra svarbios Python programavimo kalbos funkcijos, leidžiančios programuotojams įvesti duomenis ir išvesti informaciją savo programose.

## Sudėtingesni pavyzdžiai

### Interaktyvus skaičiuotuvas

Šis pavyzdys demonstruoja, kaip galima sukurti interaktyvų skaičiuotuvą, kuris paprašys vartotojo įvesti du skaičius ir atliks nurodytą operaciją su šiais skaičiais.

```Python
print("Sveiki atvykę į interaktyvų skaičiuotuvą!")
print("Pasirinkite veiksmą, kuriuo norite atlikti su dviem skaičiais:")
print("1 - Sudėtis")
print("2 - Atimtis")
print("3 - Daugyba")
print("4 - Dalyba")

choice = input("Įveskite savo pasirinkimą (1-4): ")
num1 = float(input("Įveskite pirmąjį skaičių: "))
num2 = float(input("Įveskite antrąjį skaičių: "))

if choice == '1':
    result = num1 + num2
    print("Rezultatas: ", result)
elif choice == '2':
    result = num1 - num2
    print("Rezultatas: ", result)
elif choice == '3':
    result = num1 * num2
    print("Rezultatas: ", result)
elif choice == '4':
    result = num1 / num2
    print("Rezultatas: ", result)
else:
    print("Netinkamas pasirinkimas")
```

Ši programa paprašys vartotojo pasirinkti norimą veiksmą (sudėtis, atimtis, daugyba arba dalyba), tada paprašys įvesti du skaičius ir atliks atitinkamą veiksmą su šiais skaičiais.

### Konvertuoti laipsnius Celsijaus į Farenheitus

Šis pavyzdys demonstruoja, kaip galima sukurti programą, kuri paprašys vartotojo įvesti temperatūrą laipsniais Celsijaus, tada konvertuos šią temperatūrą į laipsnius Farenheitų ir išves šį rezultatą.

```Python
celsius = float(input("Įveskite temperatūrą laipsniais Celsijaus: "))
fahrenheit = (celsius * 1.8) + 32
print("{:.1f} laipsnių Celsijaus yra {:.1f} laipsnių Farenheitų.".format(celsius, fahrenheit))
```

Ši programa paprašys vartotojo įvesti temperatūrą laipsniais Celsijaus. Tada konvertuos šią temperatūrą į laipsnius Farenheitų, naudodama formulę: F = (C * 1.8) + 32. Galiausiai išves konvertuotą temperatūrą į konsolę, naudojant formatavimo simbolius.
