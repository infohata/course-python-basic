# Lokalūs ir globalūs kintamieji

Python programavimo kalba turi skirtingus kintamųjų tipus, įskaitant skaičius, eilutes, sąrašus, žodynus ir t.t. Kintamieji gali būti apibrėžti globaliai arba lokaliai, priklausomai nuo to, kur jie yra apibrėžti ir prieinami.

Globalūs kintamieji yra apibrėžti programos pradžioje, ir jie yra pasiekiami visoje programoje. Lokalus kintamasis yra apibrėžtas funkcijos viduje ir yra pasiekiamas tik funkcijos viduje.

Štai pavyzdys:

```Python
x = "globali reikšmė"

def funkcija():
    x = "lokalus kintamasis"
    print("Funkcijos viduje x reikšmė:", x)

funkcija()

print("Globalaus x reikšmė:", x)
```

Šis pavyzdys apibrėžia globalų kintamąjį "x" ir funkciją "funkcija()", kuri apibrėžia lokalią kintamojo "x" reikšmę. Po to iškviečiama funkcija, kuri išveda lokalaus kintamojo "x" reikšmę.

Galutinis išvesties rezultatas yra "Globalaus x reikšmė: globali reikšmė", nes funkcijos viduje yra apibrėžtas naujas lokalus kintamasis "x", kuris nekeičia globalaus kintamojo "x" reikšmės.

Štai dar vienas pavyzdys, kuris naudoja globalų ir lokalų kintamąjį, bet šį kartą globalus kintamasis pakeičiamas funkcijos viduje, naudojant "global" raktinį žodį:

```Python
x = 10

def funkcija():
    global x
    x = 20
    print("Funkcijos viduje x reikšmė:", x)

funkcija()

print("Globalaus x reikšmė:", x)
```

Ši programa apibrėžia globalų kintamąjį "x" ir funkciją "funkcija()", kuri pakeičia globalaus kintamojo "x" reikšmę į 20, naudojant "global" raktinį žodį.

Galutinis išvesties rezultatas yra "Globalaus x reikšmė: 20", nes funkcija pakeitė globalaus kintamojo "x" reikšmę.