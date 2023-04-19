# Inkapsuliacija

Inkapsuliacija yra objektinio programavimo konceptas, kuris leidžia paslėpti objekto vidinius duomenis nuo išorinio pasaulio ir apsaugo nuo tiesioginio prieigos prie šių duomenų. Tai yra viena iš pagrindinių būdų, kaip padaryti klasę saugesnę ir tvirtesnę.

## Privatūs kintamieji

Privatūs kintamieji yra klasės kintamieji, kurie yra paslėpti nuo tiesioginės išorinės prieigos ir yra prieinami tik per klasės metodus. Jie gali būti sukurtas pridėjus du `_` prieš jo pavadinimą. Tai suteikia kintamajam ypatybę, kad jis tampa privatus ir negalima tiesiogiai pasiekti iš išorės kodo, tai yra, kodas iš kitos klasės negali tiesiogiai pasiekti šio kintamojo. Pvz.:

```Python
class Automobilis:
    def __init__(self, marke, modelis, metai=2023, spalva='pilka'):
        self.marke = marke
        self.modelis = modelis
        self.__metai = metai
        self.__spalva = spalva

    def gauti_metus(self):
        return self.__metai

    def gauti_spalva(self):
        return self.__spalva
```

```Python
trecias_automobilis = Automobilis('Mercedes', 'C-Class')

print(trecias_automobilis.marke) # Mercedes
print(trecias_automobilis.modelis) # C-Class
print(trecias_automobilis.gauti_metus()) # 2023
print(trecias_automobilis.gauti_spalva()) # pilka
```

## Privatūs metodai

Privatus metodas yra metodas, kuris yra paslėptas nuo tiesioginės išorinės prieigos ir yra prieinamas tik per klasės viduje esančius kitus metodus. Jis gali būti sukurtas pridėjus du `_` prieš jo pavadinimą. Tai suteikia metodui ypatybę, kad jis tampa privatus ir negalima tiesiogiai pasiekti iš išorinės kodo, tai yra, kodas iš kitos klasės negali tiesiogiai pasiekti šio metodo.

```Python
class Automobilis:
    def __init__(self, marke, modelis, metai=2023, spalva='pilka'):
        self.marke = marke
        self.modelis = modelis
        self.__metai = metai
        self.__spalva = spalva

    def gauti_metus(self):
        return self.__metai

    def gauti_spalva(self):
        return self.__spalva

    def __keisti_spalva(self, nauja_spalva):
        self.__spalva = nauja_spalva

    def perdazyti(self, nauja_spalva):
        self.__keisti_spalva(nauja_spalva)
```

```Python
trecias_automobilis.perdazyti('raudona')
print(trecias_automobilis.gauti_spalva()) # raudona
```

## Užduotys

### Pirma užduotis

- Sukurkite banko sąskaitos klasę, kuri turėtų kintamuosius: saskaitos numeris, savininkas, balansas ir pin kodas. Pastarieji du kintamieji turėtų būti privatūs.
- Sukurkite metodą, kuris leistų nuskaityti pinigus nuo sąskaitos, tačiau norint atlikti šį veiksmą reikalingas slaptažodis, kuris turėtų būti žinomas tik klasės viduje.
- Padarykite taip, kad būtų galima papildyti sąskaitą.

### Antra užduotis

- Sukurkite knygų klasę, kuri turėtų privačius kintamuosius: pavadinimas, autorius, buklė ir puslapių skaičius, ir metodus jiems gauti.
- Sukurkite metodą, kuris leistų pakeisti knygos būklę, kur galimos reikšmės yra tik 'patenkinama', 'prasta', 'atnaujinta', 'sugadinta'.
- Sukurkite metodą, kuris leistų sumažinti knygos puslapių skaičių, naudojant privatų metodą, perrašantį tą reikšmę. Turi neigi padidinti puslapių skaičiaus.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
class BankoSaskaita:
    def __init__(self, saskaitos_numeris, savininkas, balansas, pin_kodas):
        self.saskaitos_numeris = saskaitos_numeris
        self.savininkas = savininkas
        self.__balansas = balansas
        self.__pin_kodas = pin_kodas

    def nuskaityti(self, suma, pin_kodas):
        if pin_kodas == self.__pin_kodas:
            self.__balansas -= suma
            print(f'{suma} € sėkmingai nuskaityta. Dabartinis saskaitos likutis: {self.__balansas} €')
        else:
            print('Neteisingas slaptažodis. Nuskaitymas negalimas.')

    def papildyti(self, suma, pin_kodas):
        if pin_kodas == self.__pin_kodas:
            self.__balansas += suma
            print(f'{suma} € sėkmingai papildyta. Dabartinis saskaitos likutis: {self.__balansas} €')
        else:
            print('Neteisingas slaptažodis. Papildymas negalimas.')

saskaita = BankoSaskaita('LT123456789', 'Jonas Jonaitis', 1000, 1234)

saskaita.nuskaityti(100, 1122)
saskaita.nuskaityti(200, 1234)
saskaita.nuskaityti(100, 1234)
saskaita.papildyti(500, 1234)
```

Rezultatas:

```Text
Netinkamas slaptažodis. Nuskaitymas negalimas.
200 € sėkmingai nuskaityta. Dabartinis saskaitos likutis: 800 €
100 € sėkmingai nuskaityta. Dabartinis saskaitos likutis: 700 €
500 € sėkmingai papildyta. Dabartinis saskaitos likutis: 1200 €
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
class Knyga:
    def __init__(self, pavadinimas, autorius, bukle, puslapiai):
        self.__pavadinimas = pavadinimas
        self.__autorius = autorius
        self.__bukle = bukle
        self.__puslapiai = puslapiai

    def gauti_pavadinima(self):
        return self.__pavadinimas

    def gauti_autoriu(self):
        return self.__autorius

    def gauti_bukle(self):
        return self.__bukle

    def gauti_puslapius(self):
        return self.__puslapiai

    def pakeisti_bukle(self, bukle):
        if bukle in ('patenkinama', 'prasta', 'atnaujinta', 'sugadinta'):
            self.__bukle = bukle
        else:
            print(f'negalima pakeisti būklės į {bukle}.')

    def __naujas_puslapiu_skaicius(self, puslapiai):
        self.__puslapiai = puslapiai

    def isplesti_puslapius(self, puslapiai):
        if abs(puslapiai) <= self.__puslapiai:
            self.__naujas_puslapiu_skaicius(self.__puslapiai - abs(puslapiai))
        else:
            self.__puslapiai = 0

knyga = Knyga("Python programavimo kalba", "Guido van Rossum", 'nauja', 400)

knyga.isplesti_puslapius(50)
knyga.pakeisti_bukle('prasta')
print(knyga.gauti_pavadinima())
print(knyga.gauti_autoriu())
print(knyga.gauti_bukle())
print(knyga.gauti_puslapius())
```

Rezultatas:

```Text
Python programavimo kalba
Guido van Rossum
prasta
350
```

</details>
</details>
