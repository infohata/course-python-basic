# JSON biblioteka

JSON (JavaScript Object Notation) yra duomenų formatas, naudojamas duomenų keitimui tarp serverio ir kliento ar tarp dviejų skirtingų sistemų. JSON lengvai konvertuojamas į daugelio programavimo kalbų objektus, įskaitant Python.

JSON formatas naudoja raktus ir reikšmes, kur raktai yra eilutės, o reikšmės gali būti eilutės, skaičiai, loginės reikšmės (tiesa arba netiesa), masyvai arba kitos JSON objektų struktūros.

Pavyzdys JSON objekto:

```JSON
{
  "vardas": "Jonas",
  "amžius": 30,
  "ar_studentas": false,
  "pomėgiai": ["knygos", "filmai", "kelionės"],
  "adresas": {
    "gatvė": "Vytauto g. 10",
    "miestas": "Vilnius",
    "šalis": "Lietuva"
  }
}
```

Python kalboje galime dirbti su JSON duomenimis naudodami `json` modulį. Šis modulis leidžia konvertuoti Python objektus, tokius kaip žodynus, sąrašus, eilutes, skaičius ir loginės reikšmės, į JSON formatą ir atgal.

Pagrindinės `json` modulio funkcijos yra:

- `json.dump()` ir `json.dumps()` - konvertuoja Python objektą į JSON formatą.
- `json.load()` ir `json.loads()` - konvertuoja JSON duomenis į Python objektą.

## `json.dump()`

Ši funkcija konvertuoja Python objektą į JSON formatą ir rašo jį į failą. Ji priima du pagrindinius argumentus: Python objektą, kurį norite konvertuoti, ir failo objektą, į kurį norite įrašyti JSON duomenis. Paprastai naudojama kartu su `open()` funkcija, kad atidarytumėte failą rašymui.

```Python
import json

data = {"vardas": "Jonas", "amžius": 30}

with open("duomenys.json", "w", encoding="utf-8") as f:
    json.dump(data, f)
```

## `json.dumps()`

Ši funkcija konvertuoja Python objektą į JSON formatą ir grąžina JSON eilutę. Ji priima vieną argumentą: Python objektą, kurį norite konvertuoti.

```Python
import json

data = {"vardas": "Jonas", "amžius": 30}

json_eilute = json.dumps(data)
print(json_eilute)  # {"vardas": "Jonas", "amžius": 30}
```

## `json.load()`

Ši funkcija konvertuoja JSON duomenis iš failo į Python objektą. Ji priima vieną argumentą: failo objektą, iš kurio norite skaityti JSON duomenis. Paprastai naudojama kartu su `open()` funkcija, kad atidarytumėte failą skaitymui.

```Python
import json

with open("duomenys.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)  # {"vardas": "Jonas", "amžius": 30}
```

## `json.loads()`

Ši funkcija konvertuoja JSON eilutę į Python objektą. Ji priima vieną argumentą: JSON eilutę, kurią norite konvertuoti į Python objektą.

```Python
import json

json_eilute = '{"vardas": "Jonas", "amžius": 30}'

data = json.loads(json_eilute)
print(data)  # {"vardas": "Jonas", "amžius": 30}
```
