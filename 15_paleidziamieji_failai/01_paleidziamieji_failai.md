# Paleidžiamieji failai

PyInstaller yra įrankis, kuris leidžia sukurti paleidžiamąjį failą iš Python programos. Tai labai naudinga, kai norite platinti savo programą vartotojams, kurie neturi Python aplinkos ar modulių.

## Įsidiekite PyInstaller

PyInstaller gali būti įdiegtas naudojant `pip`. Atidarykite terminalą ir įveskite šią komandą:

```text
pip install pyinstaller
```

## Sukurkite paprastą Python programą

Prieš pradedant kurti paleidžiamąjį failą, turime turėti Python programą. Tarkime, turime programą, kuri vadinasi mano_programa.py:

```Python
# mano_programa.py

def main():
    print("Labas, Pasauli!")

if __name__ == "__main__":
    main()
```

## Sukurkite paleidžiamąjį failą su PyInstaller

Dabar, kai turite Python programą, galite naudoti PyInstaller, kad sukurtumėte paleidžiamąjį failą. Atidarykite terminalą, nueikite į katalogą, kuriame yra mano_programa.py, ir įveskite šią komandą:

```text
pyinstaller --onefile mano_programa.py
```

Po šios komandos vykdymo PyInstaller sukurs paleidžiamąjį failą. Jūs galite rasti sukurtą failą dist kataloge.

## Paleiskite sukurtą paleidžiamąjį failą

Dabar galite paleisti sukurtą paleidžiamąjį failą tiesiogiai per terminalą arba naršyklą.

Jei naudojate Windows, paleiskite failą per Windows naršyklą arba įveskite komandą:

```text
dist\mano_programa.exe
```

Jei naudojate Linux ar macOS, paleiskite failą per terminalą:

```text
./dist/mano_programa
```

## Piktogramos (icon) pakeitimas

1. Turite turėti ikonos failą, kurį norite naudoti savo programai. Dažniausiai naudojamas ikonos formatas yra .ico (Windows) arba .icns (macOS, *pritaikoma tik prie .app failo*). Jei naudojate Linux, galite naudoti .png failą.

2. Nurodykite ikoną naudojant PyInstaller:

Windows:

```text
pyinstaller --onefile --icon=mano_icon.ico my_program.py
```

Linux:

```text
pyinstaller --onefile --icon=mano_icon.png my_program.py
```

Čia mano_icon.ico, mano_icon.icns arba mano_icon.png yra jūsų pasirinktos ikonos failas.

Po komandos įvykdymo, paleidžiamasis failas, esantis dist kataloge, turėtų turėti nurodytą ikoną.
