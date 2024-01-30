# Kas yra SQL?

SQL (Structured Query Language) yra programavimo kalba, skirta valdyti duomenų bazes. Su SQL pagalba galima kurti, modifikuoti ir valdyti duomenų bazes, atlikti užklausas ir gauti reikiamą informaciją.

Pradžiai, pasiruošime aplinką darbui su SQL "Visual Studio Code" platformoje.

1. Įdiekite "SQLite" plėtinį

Atidarykite VSCode ir pasirinkite "Extensions" iš esančių meniu juostų. Įrašykite "SQLite" paieškos laukelyje ir pasirinkite "SQLite" plėtinį. Spustelėkite "Install", kad įdiegtumėte plėtinį.
![Plėtinys](/images/db/pletinys.png)

2. Sukurkite naują SQLite duomenų bazę

Norėdami sukurti naują SQLite duomenų bazę, pasirinkite "Explorer" iš esančių meniu juostų, spustelėkite dešinįjį pelės klavišą ir pasirinkite "New File". Pavadinkite failą "test.db" arba kaip norite ir įrašykite ".db" formatą.

3. Atidarykite duomenų bazę

Spustelėkite dešinį pelės klavišą ant duomenų bazės failo ir pasirinkite "Open Database".
![Atidaryti DB](/images/db/opendb1.png)

Dar vienas būdas: "Shift + Command + P" (arba "Shift + Ctrl + P" Windows sistemoje) paieškos laukelyje galite įvesti "SQLite: Open Database" ir pasirinkti duomenų bazę iš pasirinkimų sąrašo.
![Atidaryti DB](/images/db/opendb2.png)
![Atidaryti DB](/images/db/opendb3.png)

Atidarę duomenų bazę galėsite ją matyti lango apačioje, kairėje pusėje
![Atidaryti DB](/images/db/opendb4.png)

Duomenų bazių kūrimui ir valdymui SQL kalba naudojamos užklausos, kurios siunčiamos į duomenų bazę.

Norėdami valdyti savo duomenų bazę, turite paspausti dešinį pelės klavišą ant savo susikurto failo ".db" ir pasirinkti "New Query". Jums atsidarys naujas SQLite langas, kuriame galėsite kurti bei valdyti savo duomenų bazę. Taip pat galite susikurti ir naują failą, kurio formatas privalo būtų ".sql"
![New Query](/images/db/naujaquery.png)

## Duomenų tipai

SQL duomenų tipai gali šiek tiek skirtis tarp skirtingų duomenų bazių sistemų, tačiau štai pagrindiniai duomenų tipai, kuriuos galima rasti daugelyje sistemų

### Tekstas

- CHAR(n): Fiksuoto dydžio tekstas, kur n yra simbolių skaičius.
- VARCHAR(n): Kintamo dydžio tekstas, kur n yra maksimalus simbolių skaičius.
- TEXT: Kintamo dydžio tekstas, kurio ilgis gali būti labai didelis.

### Sveikieji skaičiai

- TINYINT: Mažas sveikasis skaičius.
- SMALLINT: Vidutinio dydžio sveikasis skaičius.
- INTEGER: Didelis sveikasis skaičius. (INT irgi yra bet nenaudotinas)
- BIGINT: Labai didelis sveikasis skaičius.

### Skaičiai su kableliu

- FLOAT(n, d): Aproksimacija realaus skaičiaus su n skaitmenimis ir d dešimtainiais skaitmenimis.
- REAL: Realus skaičius su 7 skaitmenimis tikslumu.
- DOUBLE: Realus skaičius su 15 skaitmenimis tikslumu.
- DECIMAL(n, d): Tikslus realus skaičius su n skaitmenimis ir d dešimtainiais skaitmenimis.
- NUMERIC(n, d): Panašus į DECIMAL, bet skiriasi kai kuriuose aspektuose.

### Datos ir laiko

- DATE: Data (metai, mėnesiai, dienos).
- TIME: Laikas (valandos, minutės, sekundės).
- TIMESTAMP: Data ir laikas.
- DATETIME: Data ir laikas (skirtumas tarp TIMESTAMP ir DATETIME gali būti sistemose).
- INTERVAL: Laiko tarpas tarp dviejų datų ar laikų.

### Loginiai

- BOOLEAN: Loginis tipas, kuris gali turėti reikšmes TRUE, FALSE arba NULL.

### Binariniai

- BINARY(n): Fiksuoto dydžio dvejetainiai duomenys, kur n yra baitų skaičius.
VARBINARY(n): Kintamo dydžio dvejetainiai duomenys, kur n yra maksimalus baitų skaičius.
- BLOB: Didelis dvejetainių duomenų objektas, skirtas saugoti didelius dvejetainius duomenis.

### ENUM ir SET

- ENUM: Leidžia nurodyti konkretų iš anksto apibrėžtų reikšmių sąrašą.
- SET: Leidžia nurodyti konkretų iš anksto apibrėžtų reikšmių sąrašą, bet skirtingai nei ENUM, galima saugoti kelias reikšmes viename įraše.

## CREATE TABLE

Ši užklausa naudojama sukurti naują lentelę duomenų bazeje. Kuriant ar valdant duomenis pirmą kartą ir norint, kad duomenų bazė veiktų, gali reikti ją išsaugoti savo kompiuteryje.

Duomenų bazės lentelėse saugomi įrašai, kurie atspindi tam tikrus objektus ar dalykus. Kiekviena lentelė turi stulpelius (laukus) ir eilutes (įrašus). Stulpeliai aprašo kiekvieno įrašo savybes, o eilutėse saugomi faktiniai duomenys.

Pavyzdys

```sql
CREATE TABLE klientai (
id INTEGER PRIMARY KEY AUTOINCREMENT,
vardas VARCHAR(50),
pavardė VARCHAR(50),
adresas VARCHAR(100),
el_paštas VARCHAR(50)
);
```

Ši SQL užklausa kuriama, kad būtų sukurta nauja lentelė "klientai" su keliais stulpeliais: "id", "vardas", "pavardė", "adresas" ir "el_paštas". Kiekvienas stulpelis turi savo tipą ir reikšmių apribojimus.

"id" - tai yra unikalus identifikatorius, kuris naudojamas kliento atpažinimui lentelėje. Tai yra įprasta lentelės praktika turėti stulpelį su unikaliu identifikatoriumi, kuris automatiškai generuojamas kiekvienam naujam įrašui, įterpiant į lentelę. "INT" yra tipas, apibrėžiantis sveikus skaičius. "PRIMARY KEY" apibrėžia šio stulpelio rolę kaip pagrindinio identifikatoriaus. Tai reiškia, kad kiekvienas įrašas lentelėje turi unikalų "id" numerį.

"vardas", "pavardė" ir "el_paštas" yra "VARCHAR" tipai, apibrėžiantys tekstinius stulpelius, kurių ilgis negali viršyti nurodytos reikšmės simbolių skaičiaus.

"adresas" taip pat yra "VARCHAR" tipas, bet jo ilgis gali būti iki 100 simbolių, nes adresas gali būti ilgesnis nei vardas ar pavardė.

Taigi, sukurdami lentelę SQL užklausoje, turite apibrėžti kiekvieno stulpelio pavadinimą, tipą ir reikšmių apribojimus, kuriuos jūs norite nustatyti stulpeliui. Tai padeda užtikrinti, kad duomenys, įvesti į lentelę, atitiktų jūsų reikalavimus ir būtų saugomi tinkamai.

Norėdami paleisti kodą galite naudoti "Shift + Command + P" (arba "Shift + Ctrl + P" Windows sistemoje) ir pasirinkti "Run Query"
![Paleisti kodą](/images/db/paleistikoda1.png)

Arba pažymėkite kodą, kurį norite paleisti, spauskite dešinį pelės klavišą ir pasirinkite "Run Query"
![Paleisti kodą](/images/db/paleistikoda2.png)

## ALTER TABLE

Ši užklausa naudojama modifikuoti esamą lentelę, pvz., pridėti naują stulpelį ar pakeisti esamo stulpelio tipą.

Pavyzdys

```sql
ALTER TABLE klientai
ADD telefonas VARCHAR(20);
```

```sql
ALTER TABLE klientai
ALTER COLUMN adresas TEXT;
```

## DROP TABLE

Ši užklausa naudojama pašalinti lentelę iš duomenų bazės.

Pavyzdys

```sql
DROP TABLE klientai;
```

## Užduotys

### Pirma užduotis

- Sukurkite lentelę pavadinimu "studentai", kuri turės šiuos stulpelius:

```text
id: sveikas skaičius, PRIMARY KEY
vardas: tekstas, maksimalus ilgis - 50 simbolių
pavarde: tekstas, maksimalus ilgis - 50 simbolių
studijų_programa: tekstas, maksimalus ilgis - 100 simbolių
el_pastas: tekstas, maksimalus ilgis - 50 simbolių
```

- Modifikuokite lentelę "studentai" - prie "studentai" lentelės pridėkite naują stulpelį "gimimo_data" su datos tipu.
- Pašalinkite lentelę "studentai"

Pašalinkite "studentai" lentelę iš duomenų bazės.

### Antra užduotis

- Sukurkite lentelę "dėstytojai", kuri turės šiuos stulpelius:

```text
id: sveikas skaičius, PRIMARY KEY
vardas: tekstas, maksimalus ilgis - 50 simbolių
pavarde: tekstas, maksimalus ilgis - 50 simbolių
skyrius: tekstas, maksimalus ilgis - 100 simbolių
el_paštas: tekstas, maksimalus ilgis - 50 simbolių
```

- Prie "dėstytojai" lentelės pridėkite naują stulpelį "kabineto_nr" su sveiko skaičiaus tipu.

- Pašalinkite "dėstytojai" lentelę iš duomenų bazės.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```sql
CREATE TABLE studentai (
  studento_id INTEGER PRIMARY KEY,
  vardas VARCHAR(50),
  pavarde VARCHAR(50),
  studijų_programa VARCHAR(100),
  el_pastas VARCHAR(50)
);

ALTER TABLE studentai
ADD gimimo_data DATE;

DROP TABLE studentai;
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```sql
CREATE TABLE destytojai (
  id INTEGER PRIMARY KEY,
  vardas VARCHAR(50),
  pavarde VARCHAR(50),
  skyrius VARCHAR(100),
  el_pastas VARCHAR(50)
);

ALTER TABLE destytojai
ADD kabineto_nr INT;

DROP TABLE destytojai;
```

</details>
</details>
