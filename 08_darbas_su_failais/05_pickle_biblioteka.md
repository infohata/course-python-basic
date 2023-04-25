# Pickle biblioteka

`pickle` yra Python standartinė biblioteka, skirta objektų serializavimui ir deserializavimui. Serializavimas yra procesas, kai objektai konvertuojami į baitų seką, kad būtų galima juos saugoti diske arba perduoti per tinklą. Deserializavimas yra atvirkštinis procesas, kai baitų seka konvertuojama atgal į objektą.

## Kintamųjų saugojimas ir skaitymas su pickle

```Python
import pickle

# Kintamojo saugojimas (serializavimas)
kintamasis = 42

with open('variable.pickle', 'wb') as file:
    pickle.dump(kintamasis, file)

# Kintamojo skaitymas (deserializavimas)
with open('variable.pickle', 'rb') as file:
    ikeltas_kintamasis = pickle.load(file)

print(ikeltas_kintamasis)  # Išveda: 42
```

Naudojame `pickle.dump()` funkciją, kad išsaugotume (serializuotume) kintamąjį "kintamasis" į atidarytą failą. Serializavimas konvertuoja objektą į baitų seką, kad galėtumėte jį saugoti diske.

Tada naudojame `pickle.load()` funkciją, kad nuskaitytume (deserializuotume) kintamąjį iš atidaryto failo. Deserializavimas konvertuoja baitų seką atgal į objektą.

## Sąrašų ir žodynų saugojimas ir skaitymas

```Python
import pickle

# Sąrašo saugojimas (serializavimas)
sarasas = [1, 2, 3, 4, 5]

with open('sarasas.pickle', 'wb') as failas:
    pickle.dump(sarasas, failas)

# Sąrašo skaitymas (deserializavimas)
with open('sarasas.pickle', 'rb') as failas:
    ikeltas_sarasas = pickle.load(failas)

print(ikeltas_sarasas)  # Išveda: [1, 2, 3, 4, 5]

# Žodyno saugojimas (serializavimas)
zodynas = {'a': 1, 'b': 2, 'c': 3}

with open('zodynas.pickle', 'wb') as failas:
    pickle.dump(zodynas, failas)

# Žodyno skaitymas (deserializavimas)
with open('zodynas.pickle', 'rb') as failas:
    ikeltas_zodynas = pickle.load(failas)

print(ikeltas_zodynas)  # Išveda: {'a': 1, 'b': 2, 'c': 3}
```

## Objektų saugojimas ir skaitymas

```Python
import pickle

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __str__(self):
        return f"{self.vardas}, {self.amzius} metų"

# Objekto saugojimas (serializavimas)
zmogus = Zmogus("Jonas", 30)

with open('zmogus.pickle', 'wb') as failas:
    pickle.dump(zmogus, failas)

# Objekto skaitymas (deserializavimas)
with open('zmogus.pickle', 'rb') as failas:
    ikeltas_zmogus = pickle.load(failas)

print(ikeltas_zmogus)  # Išveda: Jonas, 30 metų
```

## Užduotis

Patobulinkite biudžeto programą, kad pajamų/išlaidų žurnalą atidarant programai nuskaitytų iš pickle failo, o uždarant - perrašytų žurnalo pickle failą atnaujinta informacija. Atkreipkite dėmesį, kad žurnalo įrašai yra objektai - jų sąrašo tiesiogiai json faile išsaugoti neitų.
