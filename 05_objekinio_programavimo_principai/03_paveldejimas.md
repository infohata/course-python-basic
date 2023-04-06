# Paveldėjimas

Viena iš objektinio programavimo savybių yra paveldėjimas. Tai reiškia, kad klasė gali paveldėti kitos klasės savybes ir metodus. Paveldėjimas padeda sumažinti kodą, nes leidžia sukurti naujas klases, kurios naudoja savybes ir metodus iš jau egzistuojančių klasių.

```Python
class SportinisAutomobilis(Automobilis):
    def greitis(self):
        print('Šis automobilis gali važiuoti iki 300 km/h')

ferrari = SportinisAutomobilis('Ferrari', '458 Italia', metai=2021, spalva='raudona')
```

Šiame pavyzdyje sukūrėme objektą, kuris paveldi savybes ir metodus iš klasės "Automobilis", tačiau turi savo unikalų metodą "greitis".

```Python
print(ferrari.marke) # Ferrari
print(ferrari.modelis) # 458 Italia
print(ferrari.gauti_metus()) # 2021
print(ferrari.gauti_spalva()) # raudona

ferrari.keisti_spalva("geltona")
print(ferrari.gauti_spalva()) # geltona

ferrari.greitis() # Šis automobilis gali važiuoti iki 300 km/h
```

## Objekto priklausymo klasei patikrinimas

`isinstance` yra funkcija, kuri leidžia patikrinti, ar objektas priklauso tam tikrai klasei. Ši funkcija grąžina `True`, jei objektas yra tos klasės objektas arba objekto klasė paveldi nurodytą klasę, ir `False` kitu atveju. Pvz.:

```Python
ferrari = SportinisAutomobilis('Ferrari', '458 Italia')
audi = Automobilis("Audi", "A4")

print(isinstance(audi, Automobilis)) # True
print(isinstance(ferrari, Automobilis)) # True
print(isinstance(audi, SportinisAutomobilis)) # False
print(isinstance(ferrari, SportinisAutomobilis)) # True
```

## Užduotys
