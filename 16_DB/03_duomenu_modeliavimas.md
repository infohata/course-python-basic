# Duomenų modeliavimas

Duomenų modeliavimas yra procesas, kurio metu analizuojamos sistemos reikalavimai ir sukuriamas duomenų struktūros modelis, kad būtų galima laikyti ir manipuliuoti duomenimis.

## Raktai (keys)

- Pirminis raktas (Primary key): Kiekvienoje lentelėje turėtų būti unikalus identifikatorius, vadinamas pirminiu raktu. Jis naudojamas nustatyti konkretų įrašą ir užtikrinti, kad nėra dubliuojamų duomenų. Paprastai pirminis raktas yra AUTO_INCREMENT(stulpelio reikšmė automatiškai didinama (inkrementuojama) kiekvieną kartą, kai į lentelę įrašomas naujas įrašas.) tipo stulpelis arba UUID(naudojamas, kai reikia sukurti unikalų identifikatorių, kuris būtų unikalus tarp visų sistemos komponentų arba tarp daugelio sistemų).
- Svetimasis raktas (Foreign key): Tai raktas, naudojamas siejant dvi skirtingas lenteles pagal jų pirminius raktus. Svetimas raktas leidžia sukurti ryšį tarp lentelių, kad būtų galima atlikti užklausas tarp jų.

Turime šį pavyzdį:

```sql
-- Sukuriame "studentai" lentelę
CREATE TABLE studentai (
  id INT PRIMARY KEY,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  gimimo_metai DATE,
  fk_klase_id INT,
  FOREIGN KEY (fk_klase_id) REFERENCES klases (id)
);

-- Sukuriame "mokytojai" lentelę
CREATE TABLE mokytojai (
  id INT PRIMARY KEY,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  dirba_nuo DATE,
  fk_dalykas_id INT,
  FOREIGN KEY (fk_dalykas_id) REFERENCES dalykai (id)
);

-- Sukuriame "klases" lentelę
CREATE TABLE klases (
  id INT PRIMARY KEY,
  pavadinimas VARCHAR(255) NOT NULL,
  fk_mokytojas_id INT,
  FOREIGN KEY (fk_mokytojas_id) REFERENCES mokytojai (id)
);

-- Sukuriame "pazymiai" lentelę
CREATE TABLE pazymiai (
  id INT PRIMARY KEY,
  pazymys INT NOT NULL,
  data DATE NOT NULL,
  fk_studentas_id INT,
  fk_dalykas_id INT,
  FOREIGN KEY (fk_studentas_id) REFERENCES studentai (id),
  FOREIGN KEY (fk_dalykas_id) REFERENCES dalykai (id)
);

-- Sukuriame "dalykai" lentelę
CREATE TABLE dalykai (
  id INT PRIMARY KEY,
  pavadinimas VARCHAR(255) NOT NULL
);
```

```sql
-- Įterpiame duomenis į "dalykai" lentelę
INSERT INTO dalykai (id, pavadinimas)
VALUES (1, 'Matematika'), (2, 'Fizika'), (3, 'Biologija'), (4, 'Anglų kalba'), (5, 'Lietuvių kalba'), (6, 'Istorija');

-- Įterpiame duomenis į "mokytojai" lentelę
INSERT INTO mokytojai (id, vardas, pavarde, dirba_nuo, fk_dalykas_id)
VALUES (1, 'Petras', 'Petraitis', '2012-09-01', 1),
       (2, 'Ona', 'Onaite', '2010-09-01', 2),
       (3, 'Marius', 'Marijus', '2014-09-01', 3),
       (4, 'Rasa', 'Rasaite', '2010-09-01', 4),
       (5, 'Aurimas', 'Aurimaitis', '2015-09-01', 5),
       (6, 'Gintare', 'Gintarėlė', '2017-09-01', 6);

-- Įterpiame duomenis į "klases" lentelę
INSERT INTO klases (id, pavadinimas, fk_mokytojas_id)
VALUES (1, '1a', 1), (2, '1b', 2), (3, '2a', 3), (4, '2b', 4), (5, '3a', 5), (6, '3b', 6);

-- Įterpiame duomenis į "studentai" lentelę
INSERT INTO studentai (id, vardas, pavarde, gimimo_metai, fk_klase_id)
VALUES (1, 'Jonas', 'Jonaitis', '2010-01-01', 1),
       (2, 'Miglė', 'Miglaitė', '2009-06-23', 1),
       (3, 'Eglė', 'Eglaitė', '2009-11-12', 2),
       (4, 'Simas', 'Simaitis', '2010-04-15', 3),
       (5, 'Rokas', 'Rokaitis', '2009-12-05', 4),
       (6, 'Greta', 'Gretaitė', '2010-02-11', 5),
       (7, 'Tadas', 'Tadaitis', '2009-08-30', 6),
       (8, 'Lina', 'Linkevičiūtė', '2005-03-15', 2),
       (9, 'Domantas', 'Domaševičius', '2006-08-22', 2),
       (10, 'Gabija', 'Gabiūtė', '2005-11-30', 3),
       (11, 'Tomas', 'Tomauskas', '2006-05-18', 3),
       (12, 'Diana', 'Dijūtė', '2005-07-06', 4),
       (13, 'Mindaugas', 'Mindaugiūnas', '2006-02-12', 4),
       (14, 'Kotryna', 'Kotriūtė', '2005-09-25', 5),
       (15, 'Lukas', 'Lukauškas', '2006-10-05', 5),
       (16, 'Vaida', 'Vaidatė', '2005-12-14', 6),
       (17, 'Paulius', 'Paukštaitis', '2006-03-28', 6);

-- Įterpiame duomenis į "pazymiai" lentelę
INSERT INTO pazymiai (id, pazymys, data, fk_studentas_id, fk_dalykas_id)
VALUES (1, 9, '2023-04-01', 1, 1),
       (2, 8, '2023-04-05', 1, 2),
       (3, 10, '2023-04-08', 2, 1),
       (4, 7, '2023-04-10', 2, 3),
       (5, 6, '2023-04-12', 3, 1),
       (6, 8, '2023-04-15', 3, 4),
       (7, 9, '2023-04-20', 4, 5),
       (8, 10, '2023-04-22', 4, 6),
       (9, 8, '2023-04-25', 5, 1),
       (10, 7, '2023-04-30', 5, 2),
       (11, 6, '2023-05-02', 6, 3),
       (12, 9, '2023-05-05', 6, 4),
       (13, 10, '2023-05-08', 7, 5),
       (14, 8, '2023-05-10', 7, 6),
       (15, 8, '2023-04-08', 8, 1),
       (16, 9, '2023-04-10', 8, 2),
       (17, 10, '2023-04-12', 8, 3),
       (18, 6, '2023-04-15', 8, 4),
       (19, 7, '2023-04-20', 8, 5),
       (20, 8, '2023-04-22', 8, 6),
       (21, 10, '2023-04-25', 9, 1),
       (22, 9, '2023-04-30', 9, 2),
       (23, 8, '2023-05-02', 9, 3),
       (24, 7, '2023-05-05', 9, 4),
       (25, 6, '2023-05-08', 9, 5),
       (26, 5, '2023-05-10', 9, 6),
       (27, 9, '2023-04-08', 10, 1),
       (28, 8, '2023-04-10', 10, 2),
       (29, 7, '2023-04-12', 10, 3),
       (30, 6, '2023-04-15', 10, 4);
```

## studentai lentelė

- Pirminis raktas (PRIMARY KEY): `id` stulpelis, kuriame saugomi unikalūs studentų identifikatoriai.
- Svetimasis raktas (FOREIGN KEY): `fk_klase_id` stulpelis, kuris nurodo, kuriai klasei priklauso studentas. Šis raktas yra susijęs su "klases" lentelės `id` stulpeliu.

## mokytojai lentelė

- Pirminis raktas: `id` stulpelis, kuriame saugomi unikalūs mokytojų identifikatoriai.
- Svetimasis raktas: `fk_dalykas_id` stulpelis, kuris nurodo, kokį dalyką moko mokytojas. Šis raktas yra susijęs su "dalykai" lentelės `id` stulpeliu.

## klases lentelė

- Pirminis raktas: `id` stulpelis, kuriame saugomi unikalūs klasės identifikatoriai.
- Svetimasis raktas: `fk_mokytojas_id` stulpelis, kuris nurodo, kuris mokytojas yra klasės vadovas. Šis raktas yra susijęs su "mokytojai" lentelės `id` stulpeliu.

## pazymiai lentelė

- Pirminis raktas: `id` stulpelis, kuriame saugomi unikalūs pažymių identifikatoriai.
- Svetimieji raktai:
`fk_studentas_id` stulpelis, kuris nurodo, kuriam studentui priklauso pažymys. Šis raktas yra susijęs su "studentai" lentelės `id` stulpeliu.
`fk_dalykas_id` stulpelis, kuris nurodo, iš kurio dalyko yra pažymys. Šis raktas yra susijęs su "dalykai" lentelės `id` stulpeliu.

## dalykai lentelė

Pirminis raktas: `id` stulpelis, kuriame saugomi unikalūs dalykų identifikatoriai.
Šioje lentelėje nėra svetimųjų raktų, tačiau ji turi ryšius su kitomis lentelėmis per savo `id` stulpelį, kuris yra naudojamas kaip svetimasis raktas kitose lentelėse.

`REFERENCES` komanda naudojama, norint nurodyti, su kuriuo kitu lentelės stulpeliu norime susieti svetimąjį raktą.

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
  id INT PRIMARY KEY,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  fk_adresas_id INT,
  FOREIGN KEY (fk_adresas_id) REFERENCES adresai (id)
);

-- Sukuriame "adresai" lentelę
CREATE TABLE adresai (
  id INT PRIMARY KEY,
  gatve VARCHAR(255) NOT NULL,
  miestas VARCHAR(255) NOT NULL,
  pasto_kodas VARCHAR(10) NOT NULL
);
```

Šiuo atveju, "darbuotojai" lentelėje yra foreign key laukas `fk_adresas_id`, kuris rodo į "adresai" lentelės `id`. Tai yra "vienas su vieną" ryšys, nes kiekvienas darbuotojas turi tik vieną adresą, ir kiekvienas adresas yra priskirtas tik vienam darbuotojui.

## One-to-Many

Vienas su daug ryšys reiškia, kad vienas įrašas iš vienos lentelės gali būti susietas su daug įrašų iš kitos lentelės. Tokiu atveju, lentelėje su daug įrašų sukuriame foreign key lauką, kuris rodo į kitos lentelės primary key.

Išanalizuokime prieš tai turėtą pavyzdį, kurio visos lentelės turi One-to-Many ryšį:

### studentai ir klasės

Viena klasė gali turėti daug studentų, o kiekvienas studentas priklauso tik vienai klasei. "studentai" lentelėje yra foreign key laukas "fk_klase_id", kuris rodo į "klases" lentelės "id".

### mokytojai ir dalykai

Kiekvienas mokytojas moko vieno dalyko, bet kiekvienas dalykas gali būti mokomas kelių mokytojų. "mokytojai" lentelėje yra foreign key laukas "fk_dalykas_id", kuris rodo į "dalykai" lentelės "id".

### klases ir mokytojai

Kiekvienai klasei yra priskirtas vienas mokytojas kaip klasės vadovas, bet kiekvienas mokytojas gali būti vadovu kelioms klasėms. "klases" lentelėje yra foreign key laukas "fk_mokytojas_id", kuris rodo į "mokytojai" lentelės "id".

### pazymiai ir studentai

Kiekvienas studentas gali turėti daug įvertinimų (pazymiai), bet kiekvienas įvertinimas yra priskirtas tik vienam studentui. "pazymiai" lentelėje yra foreign key laukas "fk_studentas_id", kuris rodo į "studentai" lentelės "id".

### pazymiai ir dalykai

Kiekvienas dalykas gali turėti daug įvertinimų (pazymiai), bet kiekvienas įvertinimas yra priskirtas tik vienam dalykui. "pazymiai" lentelėje yra foreign key laukas "fk_dalykas_id", kuris rodo į "dalykai" lentelės "id".

## Many-to-Many

Daug su daug ryšys reiškia, kad daug įrašų iš vienos lentelės gali būti susieti su daug įrašų iš kitos lentelės. Šiuo atveju reikia sukurti trečiąją lentelę, kuri saugo ryšius tarp kitų dviejų lentelių. Šioje lentelėje sukuriame du foreign key laukus, kurie rodo į abiejų lentelių primary key.

Pavyzdys:

Tarkime, turime duomenų bazę, kuri saugo informaciją apie knygas ir autorių duomenis. Kiekviena knyga gali turėti daug autorių, ir kiekvienas autorius gali būti parašęs daug knygų. Tokiu atveju turime tris lentelės:

```sql
-- Sukuriame "knygos" lentelę
CREATE TABLE knygos (
  id INT PRIMARY KEY,
  pavadinimas VARCHAR(255) NOT NULL
);

-- Sukuriame "autoriai" lentelę
CREATE TABLE autoriai (
  id INT PRIMARY KEY,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL
);

-- Sukuriame "knygos_autoriai" lentelę
CREATE TABLE knygos_autoriai (
  id INT PRIMARY KEY,
  fk_knyga_id INT,
  fk_autorius_id INT,
  FOREIGN KEY (fk_knyga_id) REFERENCES knygos (id),
  FOREIGN KEY (fk_autorius_id) REFERENCES autoriai (id)
);
```

Šiuo atveju, "knygos_autoriai" lentelė yra trečioji lentelė, kuri saugo ryšius tarp "knygos" ir "autoriai" lentelių. Lentelėje yra du foreign key laukai: `fk_knyga_id`, kuris rodo į "knygos" lentelės `id`, ir `fk_autorius_id`, kuris rodo į "autoriai" lentelės `id`. Tai yra "daug su daug" ryšys, nes kiekviena knyga gali turėti daug autorių, ir kiekvienas autorius gali būti parašęs daug knygų.
