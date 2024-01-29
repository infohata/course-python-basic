# Raktai, ryšiai

## Raktai (keys)

- Pirminis raktas (Primary key): Kiekvienoje lentelėje turėtų būti unikalus identifikatorius, vadinamas pirminiu raktu. Jis naudojamas nustatyti konkretų įrašą ir užtikrinti, kad nėra dubliuojamų duomenų. Paprastai pirminis raktas yra AUTO_INCREMENT - stulpelio reikšmė automatiškai didinama (inkrementuojama) kiekvieną kartą, kai į lentelę įrašomas naujas įrašas. Pirminio rakto stulpelis dar gali būti UUID tipo, kuris yra naudojamas, kai reikia sukurti unikalų identifikatorių tarp visų sistemos komponentų arba tarp daugelio sistemų.
- Svetimasis raktas (Foreign key): Tai raktas, naudojamas siejant dvi skirtingas lenteles pagal jų pirminius raktus. Svetimas raktas leidžia sukurti ryšį tarp lentelių, kad būtų galima atlikti užklausas tarp jų.

Pavyzdys:

Turime duomenų bazę, kuriame saugome informaciją apie klientus ir jų užsakymus. Tam galime sukurti dvi lentelės: "Klientai" ir "Užsakymai"

```sql
-- Sukuriame "Klientai" lentelę
CREATE TABLE Klientai (
  id INTEGER PRIMARY KEY,
  vardas VARCHAR(50),
  pavarde VARCHAR(50),
  el_pastas VARCHAR(100),
  telefonas VARCHAR(15)
);

-- Sukuriame "Užsakymai" lentelę
CREATE TABLE Uzsakymai (
  id INTEGER PRIMARY KEY,
  data TEXT,
  kiekis INTEGER,
  suma DECIMAL(10,2),
  kliento_id INTEGER REFERENCES Klientai(id) -- svetimasis raktas, siejantis šią lentelę su "Klientai" lentelės pirminiu raktu "id".
);
```

❗ `REFERENCES` komanda naudojama, norint nurodyti, su kuriuo kitu lentelės stulpeliu norime susieti svetimąjį raktą.

Kiekvienas įrašas "Užsakymai" lentelėje turi nurodytą kliento ID, kuris atitinka konkretų klientą "Klientai" lentelėje. Šis ryšys leidžia mums atlikti užklausas, kurios apjungia abiejų lentelių duomenis

## Ryšiai tarp lentelių

Duomenų bazėse lentelių tarpusavio ryšiai sudaro pagrindą struktūruoti duomenis. Yra trys pagrindiniai ryšių tipai:

- Vienas su vienu (One-to-One)
- Vienas su daug (One-to-Many)
- Daug su daug (Many-to-Many)

## One-to-One

Šis ryšys nurodo, kad vienas įrašas iš vienos lentelės gali būti susietas su vienu įrašu iš kitos lentelės. Tokiu atveju, vienoje iš lentelių būtina sukurti foreign key lauką, kuris rodo į kitos lentelės primary key.

Pavyzdys:

Tarkime, turime duomenų bazę, kurioje saugomi darbuotojų duomenys ir jų darbo vietos adreso duomenys. Kiekvienam darbuotojui yra priskirtas unikalus darbo vietos adresas. Tokiu atveju turėtume dvi lentelės:

```sql
-- Sukuriame "darbuotojai" lentelę
CREATE TABLE darbuotojai (
  id INTEGER PRIMARY KEY,
  vardas TEXT NOT NULL,
  pavarde TEXT NOT NULL,
  fk_adresas_id INTEGER UNIQUE REFERENCES adresai(id) -- foreign key laukas, kuris rodo į "adresai" lentelės `id`.
);

-- Sukuriame "adresai" lentelę
CREATE TABLE adresai (
  id INTEGER PRIMARY KEY,
  gatve TEXT NOT NULL,
  miestas TEXT NOT NULL,
  pasto_kodas TEXT NOT NULL
);

```

![One-to-One](/images/db/onetoone.png)

Šiuo atveju, "darbuotojai" lentelėje yra foreign key laukas `fk_adresas_id`, kuris rodo į "adresai" lentelės `id`. Tai yra "vienas su vienu" ryšys, nes kiekvienas darbuotojas turi tik vieną adresą, ir kiekvienas adresas yra priskirtas tik vienam darbuotojui.

## One-to-Many

Vienas su daug ryšys reiškia, kad vienas įrašas iš vienos lentelės gali būti susietas su daug įrašų iš kitos lentelės. Tokiu atveju, lentelėje su daug įrašų sukuriame foreign key lauką, kuris rodo į kitos lentelės primary key.

```sql
-- Sukuriame "Klientai" lentelę
CREATE TABLE Klientai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas TEXT,
  pavarde TEXT,
  el_pastas TEXT,
  telefonas TEXT
);

-- Sukuriame "Užsakymai" lentelę
CREATE TABLE Uzsakymai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  uzsakymo_data DATE,
  kiekis INTEGER,
  suma FLOAT,
  kliento_id INTEGER REFERENCES Klientai(id)
);
```

![One-to-Many](/images/db/onetomany.png)

Šis kodas sukurs duomenų bazę su dviem lentelėmis: "Klientai" ir "Užsakymai". Lentelės bus susietos "One-to-Many" ryšiu, kuriuo kiekvienas klientas gali turėti daugybę užsakymų, tačiau kiekvienas užsakymas yra susijęs tik su vienu klientu.

## Many-to-Many

Daug su daug ryšys reiškia, kad daug įrašų iš vienos lentelės gali būti susieti su daug įrašų iš kitos lentelės. Šiuo atveju reikia sukurti trečiąją lentelę, kuri saugo ryšius tarp kitų dviejų lentelių. Šioje lentelėje sukuriame du foreign key laukus, kurie rodo į abiejų lentelių primary key.

Pavyzdys:

Tarkime, turime duomenų bazę, kuri saugo informaciją apie knygas ir autorių duomenis. Kiekviena knyga gali turėti daug autorių, ir kiekvienas autorius gali būti parašęs daug knygų. Tokiu atveju turime tris lentelės:

```sql
-- Sukuriame "knygos" lentelę
CREATE TABLE knygos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas VARCHAR(255) NOT NULL
);

-- Sukuriame "autoriai" lentelę
CREATE TABLE autoriai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL
);

-- Sukuriame "knygos_autoriai" lentelę
CREATE TABLE knygos_autoriai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  knyga_id INTEGER REFERENCES knygos(id),
  autorius_id INTEGER REFERENCES autoriai(id)
);
```

![Many-to-Many](/images/db/manytomany.png)

Pastaba: nenaudokite `fk_` prefiksų. Paveiksliuke `fk_knyga_id` atitinka `knyga_id` kode.

Šiuo atveju, "knygos_autoriai" lentelė yra trečioji lentelė, kuri saugo ryšius tarp "knygos" ir "autoriai" lentelių. Lentelėje yra du foreign key laukai: `fk_knyga_id`, kuris rodo į "knygos" lentelės `id`, ir `fk_autorius_id`, kuris rodo į "autoriai" lentelės `id`. Tai yra "daug su daug" ryšys, nes kiekviena knyga gali turėti daug autorių, ir kiekvienas autorius gali būti parašęs daug knygų.

## Užduotys

### Pirma užduotis

Sukurkite duomenų bazę, kurioje saugosite informaciją apie studentų duomenis ir jų kursus. Kiekvienas studentas gali mokytis daugelyje kursų, ir kiekvienas kursas gali turėti daug studentų. Sukurkite atitinkamas lentelės ir susiekite jas Many-to-Many ryšiu.

### Antra užduotis

Sukurkite duomenų bazę, kurioje saugosite informaciją apie prekes ir jų kategorijas. Kiekviena prekė gali priklausyti tik vienai kategorijai, tačiau kiekviena kategorija gali turėti daug prekių. Sukurkite atitinkamas lentelės ir susiekite jas One-to-Many ryšiu.

### Trečia užduotis

Sukurkite duomenų bazę, kurioje saugosite informaciją apie darbuotojus ir jų vadovus. Kiekvienas darbuotojas turi tik vieną vadovą, tačiau kiekvienas vadovas gali turėti daug darbuotojų. Sukurkite atitinkamas lentelės ir susiekite jas One-to-Many ryšiu.

### Ketvirta užduotis

Sukurkite duomenų bazę, kurioje saugosite informaciją apie skelbimus ir jų kategorijas. Kiekvienas skelbimas gali priklausyti daugeliui kategorijų, ir kiekviena kategorija gali turėti daug skelbimų. Sukurkite atitinkamas lentelės ir susieti jas Many-to-Many ryšiu.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```sql
-- Sukuriame "Studentai" lentelę
CREATE TABLE Studentai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(50),
  pavarde VARCHAR(50),
  el_pastas VARCHAR(100),
  telefonas VARCHAR(20)
);

-- Sukuriame "Kursai" lentelę
CREATE TABLE Kursai (
  id INTEGER PRIMARY KEY,
  pavadinimas VARCHAR(50),
  aprasymas TEXT
);

-- Sukuriame "StudentuKursai" lentelę, kuri susieja "Studentai" ir "Kursai" lentelės Many-to-Many ryšiu
CREATE TABLE StudentuKursai (
  id INTEGER PRIMARY KEY,
  studento_id INTEGER REFERENCES Studentai(id),
  kurso_id INTEGER REFERENCES Kursai(id)
);
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```sql
-- Sukuriame "Kategorijos" lentelę
CREATE TABLE Kategorijos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas TEXT
);

-- Sukuriame "Prekes" lentelę
CREATE TABLE Prekes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas TEXT,
  aprasymas TEXT,
  kategorijos_id INTEGER REFERENCES Kategorijos(id)
);
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```sql
-- Sukuriam duomenų bazės schemą
CREATE TABLE vadovai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL
);

CREATE TABLE darbuotojai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  fk_vadovas_id INTEGER REFERENCES vadovai(id)
);

```

</details>
<details>
<summary>Ketvirta užduotis</summary>
<hr>

```sql
-- Sukuriam duomenų bazės schemą
CREATE TABLE skelbimai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas VARCHAR(255) NOT NULL,
  turinys TEXT NOT NULL
);

CREATE TABLE kategorijos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas VARCHAR(255) NOT NULL
);

CREATE TABLE skelbimu_kategorijos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fk_skelbimo_id INTEGER REFERENCES skelbimai(id),
  fk_kategorijos_id INTEGER REFERENCES kategorijos(id)
);
```

</details>
</details>
