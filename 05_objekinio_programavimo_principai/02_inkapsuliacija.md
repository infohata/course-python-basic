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

    def gauti_metai(self):
        return self.__metai

    def gauti_spalva(self):
        return self.__spalva
```

```Python
trecias_automobilis = Automobilis('Mercedes', 'C-Class')

print(trecias_automobilis.marke) # Mercedes
print(trecias_automobilis.modelis) # C-Class
print(trecias_automobilis.gauti_metai()) # 2023
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

    def gauti_metai(self):
        return self.__metai

    def gauti_spalva(self):
        return self.__spalva

    def __keisti_spalva(self, nauja_spalva):
        self.__spalva = nauja_spalva

    def keisti_spalva(self, nauja_spalva):
        self.__keisti_spalva(nauja_spalva)
```

```Python
trecias_automobilis.keisti_spalva('raudona')
print(trecias_automobilis.gauti_spalva()) # raudona
```

## Užduotys
