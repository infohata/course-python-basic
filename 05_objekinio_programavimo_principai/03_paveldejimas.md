# Paveldėjimas

Viena iš objektinio programavimo savybių yra paveldėjimas. Tai reiškia, kad klasė gali paveldėti kitos klasės savybes ir metodus. Paveldėjimas padeda sumažinti kodą, nes leidžia sukurti naujas klases, kurios naudoja savybes ir metodus iš jau egzistuojančių klasių.

```Python
class Elektromobilis(Automobilis):
    kuro_tipas = 'elektra'

    def max_greitis(self):
        print('Šis automobilis gali važiuoti iki 350 km/h')
        return 350

tesla_sp = Elektromobilis('Tesla', 'Model S Plaid', metai=2022, spalva='raudona')
```

Šiame pavyzdyje sukūrėme objektą, kuris paveldi savybes ir metodus iš klasės "Automobilis", tačiau turi savo unikalų metodą "greitis".

```Python
print(tesla_sp.marke) # Tesla
print(tesla_sp.modelis) # Model S Plaid
print(tesla_sp.gauti_metus()) # 2022
print(tesla_sp.gauti_spalva()) # raudona

tesla_sp.keisti_spalva("geltona")
print(tesla_sp.gauti_spalva()) # geltona

print(tesla.kuro_tipas) # elektra
tesla_sp.max_greitis() # Šis automobilis gali važiuoti iki 350 km/h
```

## Objekto priklausymo klasei patikrinimas

`isinstance` yra funkcija, kuri leidžia patikrinti, ar objektas priklauso tam tikrai klasei. Ši funkcija grąžina `True`, jei objektas yra tos klasės objektas arba objekto klasė paveldi nurodytą klasę, ir `False` kitu atveju. Pvz.:

```Python
tesla_sp = Elektromobilis('Tesla', 'Model S Plaid')
audi = Automobilis("Audi", "A4")

print(isinstance(audi, Automobilis)) # True
print(isinstance(tesla_sp, Automobilis)) # True
print(isinstance(audi, Elektromobilis)) # False
print(isinstance(tesla_sp, Elektromobilis)) # True
```

## Užduotys
