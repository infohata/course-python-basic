# Data ir laikas, formatavimas

`datetime` yra standartinis Python modulis apimantis daugybę funkcijų ir klasių, kurios leidžia kurti, pakeisti, formatuoti ir manipuliuoti datomis ir laiku.

## `datetime` klasė

```Python
from datetime import datetime

# Sukurkite datetime objektą su nurodytomis metų, mėnesio, dienos, valandų, minučių ir sekundžių reikšmėmis
dt = datetime(2023, 4, 7, 16, 30, 45)

print(dt)  # Išves: 2023-04-07 16:30:45
```

## `datetime.now()` funkcija

```Python
from datetime import datetime

# Gaukite dabartinį laiką kaip datetime objektą
dabar = datetime.now()

print(dabar)  # Išves: dabartinį laiką
```

## `date` klasė

```Python
from datetime import date

# Sukurkite date objektą su nurodytomis metų, mėnesio ir dienos reikšmėmis
d = date(2023, 4, 7)

print(d)  # Išves: 2023-04-07
```

## `date.today()` funkcija

```Python
from datetime import date

# Gaukite šiandienos datą kaip date objektą
siandiena = date.today()

print(siandiena)  # Išves: šiandienos datą
```

## `datetime.timedelta` klasė ir matematiniai veiksmai su data/laiku

```Python
from datetime import datetime, timedelta

dabar = datetime.now()
print("Dabar:", dabar)

# Pridėti 5 dienas prie dabartinės datos
po_5_dienu = dabar + timedelta(days=5)
print("Po 5 dienų:", po_5_dienu)

# Atimti 2 valandas nuo dabartinio laiko
pries_2_valandas = dabar - timedelta(hours=2)
print("Prieš 2 valandas:", pries_2_valandas)

# Skirtumas tarp dviejų datų
date1 = datetime(2023, 4, 7)
date2 = datetime(2023, 5, 7)
skirtumas = date2 - date1
print("Skirtumas tarp datų:", skirtumas)  # Išves: 30 days, 0:00:00
```

## Datos ir laiko išvedimo formatavimas su `strftime`

Funkcija strftime taip pat priklauso datetime moduliui ir leidžia formatuoti datetime objektą į stringą.

```Python
from datetime import datetime

date_object = datetime(2023, 4, 12, 18, 30, 0)
format_string = "%Y-%m-%d %H:%M:%S"

date_string = date_object.strftime(format_string)
print(date_string)
```

Čia %Y, %m, %d, %H, %M ir %S yra formatavimo kodo simboliai, atitinkantys metus, mėnesius, dienas, valandas, minutes ir sekundes.

Daugiau formatavimo galimybių: <https://strftime.org/>

## Datos ir laiko formavimas iš stringo su `strptime`

Python kalboje funkcija strptime priklauso datetime moduliui, kuris leidžia formatuoti stringą į datetime objektą. Štai kaip galite naudoti šią funkciją:

```Python
from datetime import datetime

date_string = "2023-04-12 18:30:00"
format_string = "%Y-%m-%d %H:%M:%S"

date_object = datetime.strptime(date_string, format_string)
print(date_object)
```

## Datos ir laiko išraiška skaičiumi per timestamp

Timestamp yra skaičius, atspindintis sekundžių kiekį nuo 1970 m. sausio 1 d. 00:00:00 (UTC). Python leidžia konvertuoti datetime objektus į timestamp'us ir atgal. Štai kaip tai galite padaryti:

```Python
from datetime import datetime
import time

date_object = datetime(2023, 4, 12, 18, 30, 0)

timestamp = time.mktime(date_object.timetuple())
print(timestamp)
```

Konvertuoti timestamp'ą į datetime objektą:

```Python
from datetime import datetime
import time

timestamp = 1671395400

date_object = datetime.fromtimestamp(timestamp)
print(date_object)
```

## Užduotys

### Pirma užduotis

Parašykite programą, kuri pateiktų dabartinį laiką, bet tik minutes ir sekundes.

### Antra užduotis

Sukurkite funkciją, kuri priimtų gimimo datą kaip stringą (formatu "%Y-%m-%d") ir grąžintų, kiek dienų liko iki jūsų gimtadienio

### Trečia užduotis

Parašykite programą, kuri priimtų datą ir laiką stringo formatu (pavyzdžiui, "2023-05-21 15:30"), pridėtų prie to 48 valandas ir grąžintų naują datą ir laiką stringo formatu.

### Ketvirta užduotis

Parašykite programą, kuri priimtų du laikotarpius kaip timestamp'us ir grąžintų laikotarpių skirtumą dienomis.

### 💡 Penkta užduotis

Sukurkite funkciją, kuri priimtų datą kaip stringą (pavyzdžiui, "2023-06-01") ir grąžintų, kokia savaitės diena yra ta data (pavyzdžiui, "Pirmadienis", "Antradienis" ir tt.).

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
from datetime import datetime

dabar = datetime.now()
format_string = "%M:%S"

laikas = dabar.strftime(format_string)
print(laikas)
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
from datetime import datetime, date

def dienos_iki_gimtadienio(gimimo_data):
    gimimo_data_format = datetime.strptime(gimimo_data, "%Y-%m-%d")
    siandiena = date.today()
    siandiena = datetime(siandiena.year, siandiena.month, siandiena.day)
    gimtadienio_data = gimimo_data_format.replace(year=siandiena.year)

    if gimtadienio_data < siandiena:
        gimtadienio_data = gimtadienio_data.replace(year=siandiena.year + 1)

    skirtumas = gimtadienio_data - siandiena
    return skirtumas.days

gimimo_data = "2000-01-17"
print(f"Liko {dienos_iki_gimtadienio(gimimo_data)} dienos (-ų) iki gimtadienio.")
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
from datetime import datetime, timedelta

def prideti_48_valandas(data_laikas):
    format_string = "%Y-%m-%d %H:%M"
    date_object = datetime.strptime(data_laikas, format_string)
    naujas_date_object = date_object + timedelta(hours=48)
    naujas_data_laikas = naujas_date_object.strftime(format_string)
    return naujas_data_laikas

data_laikas = "2023-05-21 15:30"
print(f"Pridėjus 48 valandas: {prideti_48_valandas(data_laikas)}")
```

</details>
<details>
<summary>Ketvirta užduotis</summary>
<hr>

```Python
from datetime import datetime

def skirtumas_dienomis(timestamp1, timestamp2):
    date_object1 = datetime.fromtimestamp(timestamp1)
    date_object2 = datetime.fromtimestamp(timestamp2)
    skirtumas = abs(date_object2 - date_object1)
    return skirtumas.days

timestamp1 = 1671395400
timestamp2 = 1674000000
print(f"Laikotarpių skirtumas dienomis: {skirtumas_dienomis(timestamp1, timestamp2)}")
```

</details>
<details>
<summary>Penkta užduotis</summary>
<hr>

```Python
from datetime import datetime

def savaites_diena(data):
    format_string = "%Y-%m-%d"
    date_object = datetime.strptime(data, format_string)
    dienos = ["Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis", "Šeštadienis", "Sekmadienis"]
    return dienos[date_object.weekday()]

data = "2023-06-01"
print(f"Ši data yra {savaites_diena(data)}")
```

</details>
</details>