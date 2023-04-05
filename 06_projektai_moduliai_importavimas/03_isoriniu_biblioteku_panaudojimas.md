# Išorinių bibliotekų panaudojimas

Python programavimo kalba turi daug išorinių bibliotekų, kurias galite naudoti savo projektuose, kad išvengtumėte kodo dubliavimo ir pasinaudotumėte kitų kūrėjų darbu. Šios bibliotekos dažnai yra platinamos per Python Package Index (PyPI) ir gali būti įdiegtos naudojant `pip` - Python paketų tvarkyklę.

## `pip install`, `pip list`

Pagrindinės `pip` komandos yra:

`pip install <paketo_pavadinimas>`: įdiegia paketą iš PyPI.

```bash
pip install requests
```

`pip list`: rodo visus įdiegtus paketus ir jų versijas.

```bash
pip list
```

## Kaip naudoti `requirements.txt` ir `pip freeze`

Sukurkite virtualią aplinką ir aktyvuokite ją (jei dar neaktyvavote):

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

Įdiekite reikiamas išorines bibliotekas naudojant

```bash
pip install <paketo_pavadinimas>:
```

Po to, kai visos reikiamos bibliotekos yra įdiegtos, naudokite komandą `pip freeze > requirements.txt`, kad sugeneruotumėte `requirements.txt` failą su visomis įdiegtomis bibliotekomis ir jų versijomis:

```bash
pip freeze > requirements.txt
```

`requirements.txt` failą įtraukite į savo projekto repozitoriją, kad kitų kūrėjų ar kompiuterių būtų lengviau įdiegti visas reikiamas priklausomybes.

## Kodėl reikalinga virtuali aplinka kiekvienam projektui?

Virtualios aplinkos yra izoliuotos Python aplinkos, kurios leidžia atskirai valdyti kiekvieno projekto priklausomybes. Virtualios aplinkos yra naudingos dėl šių priežasčių:

- Izoliacija: kiekvienas projektas gali turėti savo bibliotekų versijas, be jokių konfliktų su kitais projektais.
- Tvarka: virtualios aplinkos padeda išlaikyti sistemos tvarką, kadangi bibliotekos nėra įdiegiamos globaliai.
- Perkeliamumas: virtualių aplinkų naudojimas palengvina projekto perkėlimą tarp skirtingų kompiuterių, nes priklausomybės yra aiškiai aprašytos.
