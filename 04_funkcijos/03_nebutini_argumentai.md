# Nebūtini argumentai su numatytomis reikšmėmis ir konkretaus argumento perdavimas

## Nebūtini argumentai su numatytomis reikšmėmis

Nebūtini argumentai su numatytomis reikšmėmis leidžia nurodyti numatytas reikšmes funkcijos argumentams, kurie gali būti praleisti kviečiant funkciją. Tai leidžia pasiekti lankstumą funkcijų kūrimo metu.

Pavyzdys:

```Python
def pasveikinti(vardas, pasisveikinimas="Sveiki"):
    print(pasisveikinimas + ", " + vardas)

# Kvietimas su abiem argumentais
pasveikinti("Jonas", "Labas") # Išvestis: Labas, Jonas

# Kvietimas tik su privalomuoju argumentu
pasveikinti("Ona") # Išvestis: Sveiki, Ona
```

Ši funkcija turi privalomą argumentą vardas ir neprivalomą argumentą pasisveikinimas, kurio numatytoji reikšmė yra "Sveiki". Jei kviesite funkciją su pasisveikinimas argumentu, bus naudojama jūsų pateikta reikšmė. Jei kviesite funkciją be pasisveikinimas argumento, bus naudojama numatytoji reikšmė "Sveiki".

Dar vienas pavyzdys:

```Python
def skaiciuoti_kaina(prekes_pavadinimas, kaina, nuolaida=0, pvm=21):
    kaina_su_nuolaida = kaina * (1 - nuolaida / 100)
    kaina_su_pvm = kaina_su_nuolaida * (1 + pvm / 100)
    print(f"{prekes_pavadinimas} - kaina su nuolaida ir PVM: {kaina_su_pvm:.2f}€")

# Kvietimas su visais argumentais
skaiciuoti_kaina("Obuolys", 1.00, 10, 5) 
# Išvestis: Obuolys - kaina su nuolaida ir PVM: 0.95€

# Kvietimas su privalomaisiais argumentais ir PVM nustatytu iš anksto
skaiciuoti_kaina("Avokadas", 1.20, pvm=10) 
# Išvestis: Avokadas - kaina su nuolaida ir PVM: 1.32€

# Kvietimas su privalomaisiais argumentais ir be nuolaidos ar PVM
skaiciuoti_kaina("Pienas", 2) 
# Išvestis: pienas - kaina su nuolaida ir PVM: 2.42€
```

Funkcija apskaičiuoja kainą su nuolaida ir PVM, naudodama kaina, nuolaida ir pvm argumentus.
Kadangi nuolaida ir pvm yra pasirinktiniai argumentai, tai jei jie nėra nurodyti kviečiant funkciją, jų reikšmės bus lygios numatytosioms: 0 ir 21 atitinkamai.

## Konkretaus argumento perdavimas

Konkretaus argumento perdavimas yra būdas nurodyti, kuriam argumentui skiriama kuri reikšmė.

Pavyzdys:

```Python
def skaiciuoti(veiksmas, a, b):
    if veiksmas == "sudeti":
        return a + b
    elif veiksmas == "atimti":
        return a - b
    elif veiksmas == "dauginti":
        return a * b
    elif veiksmas == "dalinti":
        return a / b

# Kviečiant funkciją skaiciuoti, konkrečiai nurodomi argumentai
rezultatas = skaiciuoti(veiksmas="sudeti", a=2, b=3)
print(rezultatas) # Išvestis: 5
```

Ši funkcija turi tris privalomus argumentus: `veiksmas`, `a` ir `b`. Kviesdami funkciją, galite nurodyti konkretų argumento pavadinimą, prieš tai parašę `==` ir priskirdami reikšmę, kurią norite perduoti funkcijai. Tai padeda užtikrinti, kad kiekvienas argumentas būtų perduotas tinkamai ir nekiltų klaidų.

## Užduotys

### Pirma užduotis

Sukurkite funkciją apskritimo_plotas, kuri priima 2 argumentus: apskritimo spindulys ir pi reikšmę. Jei funkcija kviečiama be pi argumento, jis turėtų būti nustatytas į numatytąją reikšmę 3.14. Funkcija turi grąžinti apskritimo plotą.

### Antra užduotis

Parašykite funkciją keliones_informacija, kuri turi šiuos argumentus:

- keliones_trukme: privalomas argumentas, nurodantis kelionės trukmę valandomis.
- greitis: privalomas argumentas, nurodantis vidutinį greitį km/h.
- vartojimas: neprivalomas argumentas, nurodantis vidutinį kuro sąnaudų kiekį su numatyta reikšme 7 (l/100 km.)
- kuro_kaina: neprivalomas argumentas su numatyta reikšme 1.2 (kuro kaina eurais už litrą).

Funkcija turėtų grąžinti šią informaciją:

- Nuvažiuotas atstumas (atstumas = keliones_trukme * greitis).
- Bendros kelionės kuro sąnaudos (sąnaudos = atstumas * vartojimas / 100).
- Bendros kelionės išlaidos kuras (išlaidos = sąnaudos * kuro_kaina).

Funkcija turi grąžinti šią informaciją kaip žodyną.

### Trečia užduotis

Sukurkite funkciją, kuri mažina skaičių nurodyta nebūtino argumento reikšme, ir jeigu skaičius yra vis dar didesnis negu nebūtino ribos argumento reikšmė, kviesti save dar kartą. Tarpinis rezultatas yra spausdinamas, galutinis rezultatas grąžinamas.

# Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
  <summary>Pirma užduotis</summary>
  <hr>
  
```Python
def apskritimo_plotas(spindulys, pi=3.14):
    plotas = pi * (spindulys ** 2)
    return plotas
```

</details>
<details>
  <summary>Antra užduotis</summary>
  <hr>

```Python
def keliones_informacija(keliones_trukme, greitis, vartojimas=7, kuro_kaina=1.2):
    atstumas = keliones_trukme * greitis
    sąnaudos = atstumas * vartojimas / 100
    išlaidos = sąnaudos * kuro_kaina
    
    return {
        'atstumas': atstumas,
        'sąnaudos': sąnaudos,
        'išlaidos': išlaidos
    }
```

</details>
<details>
  <summary>Trečia užduotis</summary>
  <hr>

```Python
def mazinti_iki(skaicius, po=10, iki=0):
    skaicius -= po
    if skaicius >= iki:
        print(skaicius)
        return mazinti_iki(skaicius, po, iki)
    else:
        return skaicius

print(mazinti_iki(101))
print(mazinti_iki(33, 3, 23))
```
</details>
</details>