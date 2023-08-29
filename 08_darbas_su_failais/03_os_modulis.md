# `os` modulis

`os` modulis yra standartinis Python bibliotekos modulis, kuris suteikia funkcijas ir galimybes sąveikauti su operacinės sistemos funkcijomis. Jis leidžia dirbti su failų sistema, katalogų struktūra, procesais, aplinkos kintamaisiais ir pan.

## Navigacija po katalogų medį

- `os.getcwd()`: Grąžina dabartinio darbo katalogo kelią.
- `os.chdir(path)`: Pakeičia dabartinį darbo katalogą į nurodytą kelią.

Pavyzdys:

```Python
import os

# Gauti dabartinio darbo katalogo kelią
print("Dabartinis darbo katalogas:", os.getcwd())

# Pakeisti darbo katalogą į kitą katalogą
os.chdir('/naujas_katalogas')
print("Dabartinis darbo katalogas:", os.getcwd())
```

## Failų egzistavimo tikrinimas

`os.path` modulis suteikia funkcijas, skirtas tikrinti failų ir katalogų egzistavimą:

`os.path.exists(path)`: Grąžina True, jei nurodytas kelias egzistuoja, ir False priešingu atveju.

Pavyzdys:

```Python
import os

failo_kelias = 'pavyzdys.txt'
if os.path.exists(failo_kelias):
    print(f"Failas '{failo_kelias}' egzistuoja.")
else:
    print(f"Failas '{failo_kelias}' neegzistuoja.")
```

## Katalogų kūrimas

`os.makedirs(path)`: Sukuria visą katalogų medį, jei jis neegzistuoja.

Pavyzdys:

```Python
import os

katalogo_kelias = 'naujas_katalogas/papildomas_katalogas'
if not os.path.exists(katalogo_kelias):
    os.makedirs(katalogo_kelias)
    print(f"Katalogas '{katalogo_kelias}' sukurtas.")
else:
    print(f"Katalogas '{katalogo_kelias}' jau egzistuoja.")
```

## Failų trynimas

`os.remove(path)` funkcija leidžia trinti nurodytą failą. Ji priima vieną argumentą - failo kelią.

Pavyzdys:

```Python
import os

failo_kelias = 'pavyzdys.txt'

if os.path.exists(failo_kelias):
    os.remove(failo_kelias)
    print(f"Failas '{failo_kelias}' ištrintas.")
else:
    print(f"Failas '{failo_kelias}' neegzistuoja.")
```

## Katalogų trynimas

`os.rmdir(path)` funkcija leidžia trinti nurodytą katalogą. Katalogas turi būti tuščias, kitaip ši funkcija išmes klaidą. Ji priima vieną argumentą - katalogo kelią.

Pavyzdys:

```Python
import os

katalogo_kelias = 'naujas_katalogas'

if os.path.exists(katalogo_kelias):
    if not os.listdir(katalogo_kelias):
        os.rmdir(katalogo_kelias)
        print(f"Katalogas '{katalogo_kelias}' ištrintas.")
    else:
        print(f"Katalogas '{katalogo_kelias}' nėra tuščias.")
else:
    print(f"Katalogas '{katalogo_kelias}' neegzistuoja.")
```

## Viso katalogų medžio trynimas

`os.removedirs(path)` funkcija leidžia trinti visą katalogų medį, jei kiekvienas katalogas yra tuščias. Ji priima vieną argumentą - katalogų medžio kelią.

Pavyzdys:

```Python
import os

katalogu_medzio_kelias = 'naujas_katalogas/papildomas_katalogas'

if os.path.exists(katalogu_medzio_kelias):
    os.removedirs(katalogu_medzio_kelias)
    print(f"Katalogų medis '{katalogu_medzio_kelias}' ištrintas.")
else:
    print(f"Katalogų medis '{katalogu_medzio_kelias}' neegzistuoja.")
```

## `os.listdir`

Tai yra funkcija iš `os` modulio, kuri naudojama norint gauti katalogo turinį kaip sąrašą. Ji grąžina visų katalogo elementų sąrašą.

Pavyzdys:

```Python
import os

katalogo_kelias = '.'  # Jūsų dabartinis katalogas
turinys = os.listdir(katalogo_kelias)

print("Katalogo turinys:")
for elementas in turinys:
    print(elementas)
```

## `os.stat`

Tai yra kita funkcija iš `os` modulio, kuri naudojama failo ar katalogo būsenai (pvz., dydis, paskutinė modifikavimo data ir kt.) gauti. Ji grąžina `os.stat_result` objektą, kuris turi daug naudingų savybių, tokių kaip:

- `st_mode`: Tai yra failo apsaugos bitai, kurie nurodo failo tipą ir jo teises. Jis naudojamas, norint nustatyti failo tipą (pvz., paprastas failas, katalogas, simbolinė nuoroda) ir teises (skaitymo, rašymo, vykdymo).
- `st_ino`: Inode numeris yra unikalus failo identifikatorius failų sistemoje, naudojamas tik Unix tipo sistemose. Windows šios savybės nepalaiko, bet `os.stat` grąžina šią savybę su reikšme 0.
- `st_dev`: Įrenginio identifikatorius, kuriame yra failas.
- `st_nlink`: Tai yra failo ar katalogo nuorodų skaičius. Paprastai failo atveju šis skaičius yra 1, o katalogo atveju jis gali būti didesnis.
- `st_uid`: Vartotojo ID yra naudojamas Unix tipo sistemose nurodyti failo ar katalogo savininką. Windows šios savybės nepalaiko, bet `os.stat` grąžina šią savybę su reikšme 0.
- `st_gid`: Grupės ID yra naudojamas Unix tipo sistemose nurodyti failo ar katalogo savininko grupę. Windows šios savybės nepalaiko, bet `os.stat` grąžina šią savybę su reikšme 0.
- `st_size`: Failo dydis baitais. Šis dydis nėra taikomas katalogams.
- `st_atime`: Paskutinio failo ar katalogo prieigos laikas, t. y., kada failas ar katalogas buvo paskutinį kartą perskaitytas. Laikas pateikiamas sekundėmis nuo epochos (1970-01-01 00:00:00 UTC).
- `st_mtime`: Paskutinio failo ar katalogo modifikavimo laikas, t. y., kada failas ar katalogas buvo paskutinį kartą pakeistas. Laikas pateikiamas sekundėmis nuo epochos (1970-01-01 00:00:00 UTC).
- `st_ctime`: Failo ar katalogo būsenos pakeitimo laikas, t. y., kada failo ar katalogo teisės, nuorodos ar dydis buvo paskutinį kartą pakeisti. Laikas pateikiamas sekundėmis nuo epochos (1970-01-01 00:00:00 UTC).
- `st_blksize`: Bloko dydis bitais yra naudojamas tik Linux sistemoje failo ar katalogo saugojimui efektyviau valdyti. macOS ir Windows šių savybių nepalaiko.
- `st_blocks`: Užimamų blokų skaičius yra naudojamas tik Linux sistemoje failo ar katalogo saugojimui efektyviau valdyti. macOS ir Windows šių savybių nepalaiko.

Pavyzdys:

```Python
import os

failo_kelias = 'kazkoks_failas'

failo_statistika = os.stat(failo_kelias)

print(failo_statistika)
```

Štai bendras pavyzdys, kaip galite naudoti `os.listdir` ir `os.stat` kartu:

```Python
import os

katalogo_kelias = '.'

# Gaukime katalogo turinį
turinys = os.listdir(katalogo_kelias)

for elementas in turinys:
    elemento_kelias = os.path.join(katalogo_kelias, elementas)  # Sudedame katalogo ir elemento pavadinimą
    
    # Tikriname, ar tai failas
    if os.path.isfile(elemento_kelias):
        failo_statistika = os.stat(elemento_kelias)
        print(f"Failas: {elementas}")
        print(f"  Dydis: {failo_statistika.st_size} baitai")
        print(f"  Paskutinė modifikavimo data: {failo_statistika.st_mtime}")
    elif os.path.isdir(elemento_kelias):
        print(f"Katalogas: {elementas}")
```

## Užduotys

### Pirma užduotis

Sukurkite naują katalogą pavadinimu "Mano_Katalogas" dabartinėje darbo vietoje. Patikrinkite, ar katalogas buvo sėkmingai sukurtas, ir atspausdinkite rezultatą.

### Antra užduotis

Parašykite programą, kuri peržiūrėtų dabartinį darbo katalogą ir atspausdintų visus rastus failus bei katalogus.

### Trečia užduotis

Sukurkite naują failą pavadinimu "testas.txt" dabartinėje darbo vietoje. Tada parašykite programą, kuri patikrintų, ar failas "testas.txt" egzistuoja, ir trintų jį, jei egzistuoja. Atspausdinkite rezultatą, kad failas buvo sėkmingai ištrintas.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
import os

katalogo_kelias = "Mano_Katalogas"

if not os.path.exists(katalogo_kelias):
    os.makedirs(katalogo_kelias)
    print(f"Katalogas '{katalogo_kelias}' sukurtas.")
else:
    print(f"Katalogas '{katalogo_kelias}' jau egzistuoja.")
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
import os

dabartinis_katalogas = os.getcwd()
print(f"Dabartinis katalogas: {dabartinis_katalogas}")

print("Failai ir katalogai:")
for elementas in os.listdir(dabartinis_katalogas):
    print(elementas)
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
import os

failo_kelias = "testas.txt"

# Sukurkite failą
with open(failo_kelias, "w") as f:
    f.write("Tai yra testinis failas.")

# Patikrinkite, ar failas egzistuoja, ir trinkite jį
if os.path.exists(failo_kelias):
    os.remove(failo_kelias)
    print(f"Failas '{failo_kelias}' ištrintas.")
else:
    print(f"Failas '{failo_kelias}' neegzistuoja.")
```

</details>
</details>
