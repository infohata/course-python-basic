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

### Pirma užduotis

- Sukurkite klasę "Gyvunas" ir klases "Kate" ir "Suo", kurios paveldi tėvin4s klasės atributus ir metodus.
- Kiekviena paveldinti klasė turi turėti savo unikalų "balsas" ir "judeti" metodą.
- Sukurkite kelis skirtingoms klasėms priklausančius objektus, priskirkite jiems vardus ir iškvieskite jų metodus.

### Antra užduotis

- Patikrinkite pirmoje užduotyje sukurtų objektų priklausomybę esančioms klasėms.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
class Gyvunas:
    def __init__(self, vardas):
        self.vardas = vardas

    def balsas(self):
        pass

    def judeti(self):
        print('Ramiai guliu...')

class Kate(Gyvunas):
    def balsas(self):
        print('Miau')

    def judeti(self):
        print('Einu lėtai')

class Suo(Gyvunas):
    def balsas(self):
        print('Au au!')

    def judeti(self):
        print('Bėgu greitai')


seskas = Gyvunas('Pilkis')
kate = Kate('Rainė')
suo = Suo('Margis')

print(seskas.vardas)
seskas.balsas()
seskas.judeti()

print(kate.vardas)
kate.balsas()
kate.judeti()

print(suo.vardas)
suo.balsas()
suo.judeti()
```

Rezultatas:

```Text
Pilkis
Ramiai guliu...
Rainė
Miau
Einu lėtai
Margis
Au au!
Bėgu greitai
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>


```Python
print(isinstance(seskas, Gyvunas))
print(isinstance(seskas, Kate))
print(isinstance(seskas, Suo))
print(isinstance(kate, Gyvunas))
print(isinstance(kate, Kate))
print(isinstance(kate, Suo))
print(isinstance(suo, Gyvunas))
print(isinstance(suo, Kate))
print(isinstance(suo, Suo))
```

Rezultatas:

```Text
True
False
False
True
True
False
True
False
True
```

</details>
</details>
