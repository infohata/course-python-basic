## Python programavimo principai

Python yra programavimo kalba, kuri remiasi tam tikrais principais ir taisyklėmis.

## Kodo struktūra

Python kodo struktūra yra labai svarbi, nes ji nusako, kaip kodo eilutės turi būti struktūrizuotos ir kiek reikia naudoti įtraukas (indentation). Python nenaudoja skliaustų ar kabliatūros, kad atskirtų blokus. Vietoj to, Python naudoja įtraukas, kurios turi būti pastatytos tuo pačiu atstumu nuo kairės eilutės.

Pavyzdžiui, šis kodas yra teisingai struktūrizuotas:

```Python
if x > 0:
    print("x yra teigiamas")
else:
    print("x yra neigiamas arba lygus nuliui")
```

Tačiau šis kodas yra neteisingai struktūrizuotas:

```Python
if x > 0:
print("x yra teigiamas")
else:
    print("x yra neigiamas arba lygus nuliui")
```

## Sakinio struktūra

Python sakinių struktūra yra paprasta. Kiekvienas sakinių gali būti užbaigtas kabliataškiu (;), tačiau paprastai Python nereikalauja to daryti. Taigi, sakinių galite naudoti taip, kaip norite.

```Python
print("Sveiki, pasauli!")
```

## Blokų struktūra

Python programavimo kalba remiasi blokų struktūra. Tai reiškia, kad kodo blokai yra apibrėžti įtraukomis. Jei įtraukos nesutampa, gali būti gauta sintaksės klaida.

Pavyzdžiui, šis kodas yra teisingas:

```Python
if x > 0:
    print("x yra teigiamas")
else:
    print("x yra neigiamas arba lygus nuliui")
```

Tačiau šis kodas yra neteisingas:

```Python
if x > 0:
print("x yra teigiamas")
else:
print("x yra neigiamas arba lygus nuliui")
```

## PEP8 taisyklės

PEP8 yra Python kodo rašymo taisyklių rinkinys, kuris padeda standartizuoti Python kodo formatavimą. Šios taisyklės yra naudingos, nes jie padeda kitiems programuotojams lengviau suprasti jūsų kodą. Kai kurios iš PEP8 taisyklių:

    ❗Nenaudokite tabuliavimo simbolių kaip įtraukos. Vietoj to naudokite tarpus.

    ❗Kiekvienas eilutėje neturėtų viršyti 79 simbolių ilgio.

    ❗Naudojant kelis argumentus, atskirkite juos kableliais ir po kiekvieno argumento padėkite po vieną tarpą.

    ❗Naudokite paaiškinamuosius kintamųjų pavadinimus.

    ❗Funkcijos ir klasės pavadinimai turėtų būti parašyti naudojant CapWords notaciją (pavyzdžiui, ManoKlasė).

    ❗Trumpuosiuose funkcijų pavadinimuose naudokite mažąsias raides ir atskirkite žodžius apatiniais brūkšniais (pavyzdžiui, mano_funkcija).

    ❗Nesupaprastinkite trumpųjų pavadinimų (pvz., nenaudokite l vietoj el).

    ❗Naudojant palyginimo operatorius, naudokite išsamias formas (pavyzdžiui, != vietoj <>).

    ❗Naudokite vienodą kabliataškių vietą. Pavyzdžiui, jei pradinis kabliataškis pradedamas naujoje eilutėje, tai ir visi kiti kabliataškiai turėtų būti pradedami naujoje eilutėje.

💡 Šios taisyklės nėra būtinos, tačiau jų laikymasis padės padidinti jūsų kodo skaitomumą ir suprantamumą, ypač jei jūs dirbate su keliais programuotojais arba dalyvaujate atviro kodo projektuose.

## Komentarai

Kodas yra skirtas ne tik kompiuteriams, bet ir žmonėms. Komentarai yra svarbūs, kad kiti programuotojai galėtų lengviau suprasti, ką reiškia tam tikri kodo blokai ką norite pasiekti su savo kodu. Komentarai taip pat gali padėti jums patiems, jei vėliau turėsite peržiūrėti savo kodą ir suprasti, ką jūs bandėte padaryti.

Komentarai yra rašomi tarp simbolio `#`, o kai yra paleidžiamas kodas, viskas, kas yra tarp `#` ir eilutės pabaigos, yra ignoruojama. Komentarai taip pat gali būti naudojami kaip laikinas kodas, kurio nenorite paleisti, bet kurį norite laikyti savo faile.

```Python
# Ši eilutė nuskaito vartotojo įvestus skaičius
x = int(input("Įveskite pirmą skaičių: "))
y = int(input("Įveskite antrą skaičių: "))

# Ši eilutė sudeda du skaičius
suma = x + y

# Ši eilutė išveda sumą į ekraną
print("Suma yra:", suma)
```
```Python
# Čia mes apibrėžiame kintamuosius, kuriuos naudosime toliau
skaicius1 = 5
skaicius2 = 10

# Ši eilutė sudeda du skaičius
suma = skaicius1 + skaicius2

# Ši eilutė išveda sumą į ekraną
print("Suma yra:", suma)
```
```Python
# Ši funkcija patikrina, ar skaičius yra lyginis
def ar_lyginis(skaicius):
    if skaicius % 2 == 0:
        return True
    else:
        return False

# Čia mes patikriname, ar 4 yra lyginis skaičius
if ar_lyginis(4):
    print("4 yra lyginis skaičius")
else:
    print("4 nėra lyginis skaičius")
```

## Klaviatūros sutrumpinimai VS Code aplinkoje

Klaviatūros sutrumpinimai (angl. keyboard shortcuts) yra efektyvus būdas darbui su programavimo redaktoriais, nes jie leidžia programuotojams greičiau ir efektyviau rašyti kodą. VS Code yra labai galinga kūrimo aplinka, kuri turi daugybę klaviatūros sutrumpinimų, kurie palengvina programavimo procesą. Šie klaviatūros sutrumpinimai gali būti naudojami tiek Linux, tiek Windows, tiek macOS sistemose.

    👉 `Ctrl + Shift + P` (`Cmd + Shift + P` macOS sistemoje) - Atidaryti komandų paleidimo langą

    👉 `Ctrl + P` (`Cmd + P` macOS sistemoje) - Atidaryti greitąjį meniu

    👉 `Ctrl + Shift + E` (`Cmd + Shift + E` macOS sistemoje) - Atidaryti naršyklę

    👉 `Ctrl + Shift + F` (`Cmd + Shift + F` macOS sistemoje) - Atidaryti paieškos langą

    👉 `Ctrl + Shift + K` (`Cmd + Shift + K` macOS sistemoje) - Ištrinti eilutę

    👉 `Ctrl + /` (`Cmd + /` macOS sistemoje) - Sukurti išjungti komentarą

💡 Šie pavyzdžiai yra tik keli iš daugybės klaviatūros sutrumpinimų, kuriuos galite naudoti su VS Code.

Galite rasti visus oficialius VS Code klaviatūros sutrumpinimus dokumentacijoje, kuri yra prieinama per Visual Studio Code programą arba per jų svetainę. Štai keli būdai, kaip pasiekti šią dokumentaciją:

### Per VS Code programą:

1. Atidarykite VS Code programą
2. Pasirinkite meniu Help (Pagalba) -> Keyboard Shortcuts Reference (Klaviatūros sutrumpinimų sąrašas) arba naudokite klavišų kombinaciją `Ctrl + K`, `Ctrl + R` (`Cmd + K`, `Cmd + R` macOS sistemoje)

### Per VS Code svetainę:

1. Atidarykite VS Code svetainę (https://code.visualstudio.com/)
2. Pasirinkite meniu Docs (Dokumentacija) -> Keyboard Shortcuts (Klaviatūros sutrumpinimai)

Dokumentacija pateikia išsamią informaciją apie kiekvieną klaviatūros sutrumpinimą, taip pat jie yra suskirstyti pagal kategorijas, pvz., redagavimas, navigavimas, paieška ir kt. Be to, dokumentacija gali būti filtruojama pagal operacinę sistemą.