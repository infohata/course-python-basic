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
def skaiciuoti_kaina(prekes_pavadinimas, kaina, nuolaida=0):
    kaina_su_nuolaida = kaina * (1 - nuolaida / 100)
    print(f"{prekes_pavadinimas} - kaina su nuolaida: {kaina_su_nuolaida:.2f}€")

# Kvietimas su visais argumentais
skaiciuoti_kaina("Obuolys", 1.00, 10) 
# Išvestis: Obuolys - kaina su nuolaida: 0.90€

# Kvietimas tik su privalomaisiais argumentais
skaiciuoti_kaina("Avokadas", 1.20) 
# Išvestis: Avokadas - kaina su nuolaida: 1.20€
```

Ši funkcija turi privalomus argumentus prekes_pavadinimas ir kaina, taip pat neprivalomą argumentą nuolaida, kurio numatytoji reikšmė yra 0. Jei kviesite funkciją su nuolaida argumentu, bus naudojama jūsų pateikta reikšmė, jei kviesite funkciją be nuolaida argumento, bus naudojama numatytoji reikšmė 0.

## Konkretaus argumento perdavimas

<!-- TODO: perrašyti šitą dalį, nes neatspindi esmės. Mintis būtų, pvz.
def skaiciuoti_kaina(prekes_pavadinimas, kaina, nuolaida=0, pvm=21):
ir panaudoti:
skaiciuoti_kaina("pienas", 2, pvm=10)
-->

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

Sukurkite funkciją kelvinai_i_celsijus, kuri priima 1 argumentą - temperatūrą kelvinais. Funkcija turi grąžinti temperatūrą Celsijais. Atkreipkite dėmesį, kad 0 kelvino yra -273,15 Celsijaus laipsnių.

### Trečia užduotis

Sukurkite funkciją dauginti_skaicius, kuri priima 2 privalomus argumentus ir 1 neprivalomą argumentą multiplier, kurio numatytos reikšmės yra 1. Funkcija turi grąžinti dviejų privalomų argumentų sandaugą, padaugintą iš multiplier. Jei funkcijai perduodamas multiplier argumentas, jo reikšmė turėtų būti naudojama kaip daugiklis. Jei funkcija kviečiama be multiplier argumento, tada bus naudojama numatytoji reikšmė.

### Ketvirta užduotis

Sukurkite funkciją sandauga, kuri priima 3 argumentus: a, b ir c. Funkcija turi grąžinti trijų skaičių sandaugą. Kviesdami funkciją, nurodykite konkretų b argumento pavadinimą ir priskirkite reikšmę, lygią 5.

### Penkta užduotis

Sukurkite funkciją maisto_kalorijos, kuri priima 4 argumentus: baltymai, riebalai, angliavandeniai ir saldiklis. Funkcija turi grąžinti bendrą kalorijų kiekį maisto produktui. Kalorijos skaičiuojamos pagal šią formulę: (baltymai * 4) + (riebalai * 9) + (angliavandeniai * 4) + (saldiklis * 0). Kviesdami funkciją, nurodykite konkretų saldiklis argumento pavadinimą ir priskirkite reikšmę, lygią 2.

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
def kelvinai_i_celsijus(temp_kelvin):
    temp_celsijus = temp_kelvin - 273.15
    return temp_celsijus
```

</details>
<details>
  <summary>Trečia užduotis</summary>
  <hr>

```Python
def dauginti_skaicius(a, b, multiplier=1):
    sandauga = a * b * multiplier
    return sandauga
```

</details>
<details>
  <summary>Ketvirta užduotis</summary>
  <hr>

```Python
def sandauga(a, b=5, c=1):
    return a * b * c

print(sandauga(2, b=5)) # Išvestis: 50
```

</details>
<details>
  <summary>Penkta užduotis</summary>
  <hr>

```Python
def maisto_kalorijos(baltymai, riebalai, angliavandeniai, saldiklis=0):
    return (baltymai * 4) + (riebalai * 9) + (angliavandeniai * 4) + (saldiklis * 0)

print(maisto_kalorijos(20, 15, 30, saldiklis=2)) # Išvestis: 200
```

</details>
</details>