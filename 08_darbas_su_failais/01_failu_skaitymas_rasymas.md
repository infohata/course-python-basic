# Failų skaitymas, rašymas

## `open()`, žymės `"r"` ir `"w"`, `failas.close()`

Failų atidarymas ir uždarymas yra svarbūs programavimo procesai, kurie leidžia programai atlikti tam tikrus veiksmus su failais, tokius kaip skaityti, rašyti, papildyti arba redaguoti failus.

Failų atidarymas vyksta naudojant open() funkciją, kurioje yra nurodomas failo pavadinimas ir režimas, kuriuo norima atidaryti failą. Režimas gali būti nurodomas kaip "r" (skaitymo režimas) arba "w" (rašymo režimas).

Pavyzdys, kaip atidaryti failą skaitymo režimu:

```Python
failas = open("tekstas.txt", "r")
```

Šiuo kodu atidaromas "tekstas.txt" failas skaitymo režimu, kurio pavadinimas yra nurodomas pirmajame parametre.

Jei norite atidaryti failą rašymo režimu, reikia nurodyti režimą "w":

```Python
failas = open("tekstas.txt", "w")
```

Šis kodas atidaro "tekstas.txt" failą rašymo režimu, leidžiant jums rašyti į failą.

Kai baigsite darbą su failu, reikia jį uždaryti naudojant close() funkciją:

```Python
failas.close()
```

## `with`, `open()`

`with`  yra naujesnis ir rekomenduojamas būdas atlikti failų operacijas. Jis yra paprastesnis ir saugesnis nei `open()` ir `close()`funkcijos. `with` užtikrina, kad failas automatiškai bus uždarytas, kai bus baigtas jo naudojimas. Tai leidžia išvengti potencialių nuostolių ir sumažinti programos apkrovą.
Štai kaip galite naudoti `with` kartu su `open()` funkcija:

```Python
with open("tekstas.txt", "r") as failas:
    # atliekamos operacijos su failu
```

## Eilučių skaitymas iš failo

Naudojant `for`ciklą galima skaityti teksto failą eilutėmis ir gauti prieigą prie kiekvienos eilutės atskirai:

```Python
with open('failo_vardas.txt', 'r') as failas:
    for eilute in failas:
        print(eilute)
```

## Skaitymas eilutėmis su `readline()``

```Python
with open('failo_pavadinimas.txt', 'r') as failas:
    eilute = failas.readline()
    while eilute != '':
        print(eilute)
        eilute = failas.readline()
```

Šiame pavyzdyje mes naudojame funkciją `readline()` skaityti kiekvieną eilutę atskirai ir ją spausdinti. Pirmiausia priskiriame kintamajam "eilute" pirmąją eilutę ir naudojame "while" ciklą, kad patikrintume, ar kintamasis nėra tuščias. Po kiekvienos eilutės spausdinimo, perskaitome kitą eilutę ir taip tęsiame, kol baigiasi failas.

## Skaitymas eilučių masyvo su `readlines()``

```Python
with open('failo_pavadinimas.txt', 'r') as failas:
    eilutes = failas.readlines()
    for eilute in eilutes:
        print(eilute)
```

Šiame pavyzdyje mes naudojame funkciją `readlines()` skaityti visas eilutes ir grąžinti jas kaip masyvą. Šiuo atveju mes priskiriame masyvą kintamajam "eilutes" ir naudojame "for" ciklą, kad spausdintume kiekvieną eilutę atskirai.

❗ Paminėtina, jog `readlines()` funkcija skaito visas eilutes į atmintį, todėl ji gali užimti daug vietos, ypač jei turite didelį failą. Jei jūsų failas yra didelis, geriau naudoti pirmąjį pavyzdį su `readline()`, nes jis skaito failą eilutėmis, o ne visą failą iš karto.

## Skaitymas viso failo su `read()`

Pavyzdys:

```Python
with open('failo_pavadinimas.txt', 'r') as failas:
    viskas = failas.read()
    print(viskas)
```

Šiame pavyzdyje mes naudojame funkciją `read()` nuskaitant visą failą ir priskiriant jį kintamajam "viskas". Tada tiesiog spausdiname kintamąjį, kad pamatytume visą failą.

## Skaitymas dalimis su "buferiavimu"

Skaitymas dalimis su "buferiavimu" yra būdas perskaityti failą arba duomenų srautą dalimis, o ne viską iš karto. Tai naudinga, kai yra didelių failų, kurie gali užimti daug atminties, ir reikia juos skaityti dalimis, arba kai yra tiesiog reikalingas efektyvesnis duomenų nuskaitymas iš disko.

Pavyzdys:

```Python
with open('failas.txt', 'r') as f:
    while True:
        dalis = f.read(54)
        if not dalis:
            break
        print(dalis)
```

## `tell()`

Ši funkcija yra Python programavimo kalbos funkcija, kuri leidžia gauti dabartinę failo poziciją.

Pavyzdys:

```Python
with open("duomenys.txt", "r") as f:
    pozicija = f.tell()  # Gauti dabartinę poziciją faile
    print(pozicija)
```

## `seek()`

Ši funkcija naudojama pakeisti dabartinę failo žymeklio padėtį. Ji priima vieną ar du argumentus: pirmasis nurodo nuo kurio simbolio pradėti, antrasis nurodo nuorodą (0 - nuo failo pradžios, 1 - nuo dabartinės padėties, 2 - nuo failo galo). Numatytoji nuoroda yra 0 (failo pradžia).

Pavyzdys:

```Python
with open("tekstas.txt", "r") as failas:
    # Nustatykite žymeklį ant 5 simbolio failo pradžioje
    failas.seek(5)

    # Perskaitykite failą nuo 5 simbolio
    turinys = failas.read()
    print(turinys)
```

## `write()`

Ši funkcija naudojama, kai norite rašyti į failą.

Pavyzdys:

```Python
with open("rezultatai.txt", "w") as failas:
    failas.write("Labas, pasauli!")
```

## `writelines()`

Ši funkcija naudojama rašyti daug eilučių į failą. Ji priima sąrašą eilučių arba kitą iteruojamą tekstą. Svarbu, kad eilučių galuose būtų įtrauktas naujos eilutės simbolis ("\n").

Pavyzdys:

```Python
eilutes = ["Labas, pasauli!\n", "Tai mano pirmasis failas Python kalboje.\n"]

with open("rezultatai.txt", "w") as failas:
    failas.writelines(eilutes)
```

## Append/Papildymas "a" 

Žymė "a" naudojamaa, kai norite pridėti turinį prie esamo failo. Jei failas neegzistuoja, jis bus sukurtas.

Pavyzdys:

```Python
with open("papildymas.txt", "a") as failas:
    failas.write("Papildoma eilutė.\n")
```

## Read and Write - Skaitymas ir rašymas "r+"

Žymė "r+" naudojama, kai norite atidaryti failą tiek skaitymui, tiek rašymui. Jei failas neegzistuoja, jis nebus sukurtas.

Pavyzdys:

```Python
with open("skaitymas_rasymas.txt", "r+") as failas:
    # Skaitymas
    turinys = failas.read()
    print("Pradinis turinys:", turinys)

    # Rašymas
    failas.seek(0)  # grįžkite į failo pradžią
    failas.write("Pakeista eilutė.\n")
```

## Write and Read - Rašymas ir skaitymas "w+"

Žymė "w+" naudojama, kai norite atidaryti failą tiek rašymui, tiek skaitymui. Jei failas neegzistuoja, jis bus sukurtas. Jei failas egzistuoja, jo turinys bus ištrintas.

Pavyzdys:

```Python
with open("rasymas_skaitymas.txt", "w+") as failas:
    # Rašymas
    failas.write("Nauja eilutė.\n")

    # Skaitymas
    failas.seek(0)  # grįžkite į failo pradžią
    turinys = failas.read()
    print("Naujas turinys:", turinys)
```

Visi šie atidarymo rėžimai leidžia manipuliuoti failuose esančiu turiniu. Priklausomai nuo jūsų poreikių, galite pasirinkti tinkamiausią rėžimą.

## Užduotys

### Pirma užduotis

Atidarykite tekstiniame faile esančią eilutę ir atspausdinkite ją, pakeičiant visus didžiąsias raides mažosiomis ir atvirkščiai. Failo pavadinimas: "pakeitimai.txt".💡 Galite naudoti `swapcase()` funkciją.

### Antra užduotis

Sukurkite naują failą "skaiciai.txt" ir įrašykite į jį skaičius nuo 1 iki 100, kiekvieną naujoje eilutėje.

### Trečia užduotis

Atidarykite "tekstas.txt" failą, pakeiskite failo žymeklį į vidurį failo ir atspausdinkite likusį failo turinį.

### Ketvirta užduotis

- Sukurkite failą "eilutes.txt" ir įrašykite į jį šias eilutes:

```text
Saulėlydis žėri žemę švelniai.
Vakare vėjas šnypščia medžius.
Vėjas nerimsta, šnypščia ir švilpia.
```

- Papildykite failą "eilutes.txt" nauja eilute, kuri yra jūsų vardas ir pavardė.

- Atidarykite "eilutes.txt" failą, perskaitykite jo turinį ir atspausdinkite visas eilutes, kuriose yra žodis "vėjas".


## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
with open("pakeitimai.txt", "r") as failas:
    eilute = failas.readline()
    nauja_eilute = eilute.swapcase()
    print(nauja_eilute)
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
with open("skaiciai.txt", "w") as failas:
    for skaicius in range(1, 101):
        failas.write(f"{skaicius}\n")
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
with open("tekstas.txt", "r") as failas:
    failas.seek(0, 2)  # Pereikite į failo pabaigą
    failo_ilgis = failas.tell()  # Gauti failo ilgį
    vidurys = failo_ilgis // 2  # Rasti failo vidurį

    failas.seek(vidurys)  # Nustatykite žymeklį ant vidurio
    likusi_dalis = failas.read()  # Perskaitykite likusią dalį
    print(likusi_dalis)
```

</details>
<details>
<summary>Ketvirta užduotis</summary>
<hr>

```Python
with open("eilutes.txt", "w", encoding="utf-8") as failas:
    failas.write("Saulėlydis žėri žemę švelniai.\n")
    failas.write("Vakare vėjas šnypščia medžius.\n")
    failas.write("Vėjas nerimsta, šnypščia ir švilpia.\n")
```

```Python
with open("eilutes.txt", "a", encoding="utf-8") as failas:
    failas.write("Jūsų vardas ir pavardė\n")  # Čia įrašykite savo vardą ir pavardę
```

```Python
with open("eilutes.txt", "r", encoding="utf-8") as failas:
    for eilute in failas:
        if "vėjas" in eilute:
            print(eilute)

```

</details>
</details>