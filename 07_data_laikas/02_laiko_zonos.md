# Laiko zonos

## Aware ir Naive datos/laiko objektai

Python datetime modulyje yra du pagrindiniai datos ir laiko objektų tipai - "aware" ir "naive". "Naive" datos ir laiko objektai neturi informacijos apie laiko zonas ar vasaros laiko taikymą, todėl jie gali būti nepatogūs esant laiko zonų pokyčiams. "Aware" objektai turi informaciją apie laiko zonas ir vasaros laiko taikymą.

## `datetime.utcnow()`

Norėdami gauti dabartinį laiką pagal Coordinated Universal Time (UTC) laiko zoną, galite naudoti `datetime.utcnow()` funkciją:

```Python
from datetime import datetime

utc_now = datetime.utcnow()
print(utc_now)
```

## Laiko zonų sąrašas, `zoneinfo` modulis

Python 3.9+ versijose yra zoneinfo modulis, leidžiantis dirbti su laiko zonomis:

```Python
from zoneinfo import ZoneInfo
from datetime import datetime

# Sukurti "aware" datetime objektą su nurodyta laiko zona
laikas = datetime(2023, 4, 12, 18, 30, tzinfo=ZoneInfo("Europe/Vilnius"))
print(laikas)
```

Galite naudoti šį modulį, kad išvestumėte sąrašą laiko zonų, kurias jis palaiko:

```Python
from zoneinfo import available_timezones

for time_zone in available_timezones():
    print(time_zone)
```

## `datetime.tzinfo`

`datetime.tzinfo` yra abstrakti klasė, skirta laiko zonos informacijai saugoti. Galite naudoti `zoneinfo` modulio funkcijas, kad užpildytumėte tzinfo atributą, kai kuriate naują "aware" datetime objektą:

```Python
from datetime import datetime
from zoneinfo import ZoneInfo

laikas = datetime(2023, 4, 12, 18, 30, tzinfo=ZoneInfo("Europe/Vilnius"))
print(laikas.tzinfo)
```

## Laiko zonos nurodymas `datetime.datetime` objekte

Norėdami nurodyti laiko zoną `datetime.datetime` objekte, galite naudoti `replace()` funkciją arba `astimezone()` funkciją.

Pavyzdys su `replace()`:

```Python
from datetime import datetime
from zoneinfo import ZoneInfo

utc_now = datetime.utcnow()
vilnius_time = utc_now.replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo("Europe/Vilnius"))
print(vilnius_time)
```

Pavyzdys su `astimezone()`:

```Python
from datetime import datetime
from zoneinfo import ZoneInfo

utc_now = datetime.utcnow().replace(tzinfo=ZoneInfo("UTC"))
vilnius_time = utc_now.astimezone(ZoneInfo("Europe/Vilnius"))
print(vilnius_time)
```

Abu šie pavyzdžiai pirmiausia sukuria `datetime.datetime` objektą, atspindintį dabartinį laiką pagal Coordinated Universal Time (UTC) laiko zoną. Tada jie naudoja `replace()` arba `astimezone()` funkciją, kad pakeistų laiko zoną į "Europe/Vilnius" ir išvestų rezultatą ekrane.

## Užduotys

### Pirma užduotis

Parašykite programą, kuri išvestų sąrašą visų laiko zonų, kurių pavadinime yra "America".

### Antra užduotis

Parašykite programą, kuri iš vartotojo paprašytų laiko HH:MM(:SS) formatu, kur sekundės nėra būtinos. Tada paprašykite įvesti laiko zoną. Išspausdinkite įvestą laiką šiomis laiko zonomis: Sydney'aus, Dubai'aus, Vilniaus, London'o, New York'o ir Los Angeles.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
from zoneinfo import available_timezones

america_time_zones = []

for tz in available_timezones():
    if "America" in tz:
        america_time_zones.append(tz)

for time_zone in america_time_zones:
    print(time_zone)
```

</details>
</details>
