# Duomenų modeliavimas

Duomenų modeliavimas - tai procesas, kurio metu sudaromas duomenų struktūros planas, leidžiantis efektyviai saugoti ir valdyti informaciją. Duomenų modelis susideda iš lentelių, kuriose saugomi susiję duomenys, pvz., studentai, mokytojai, klasės, pažymiai ir dalykai. Kiekvienoje lentelėje yra stulpeliai, atitinkantys duomenų tipus (pvz., vardas, pavardė, gimimo_metai). Lentelės yra sujungtos per pirminius (PRIMARY KEY) ir svetimuosius raktus (FOREIGN KEY), kurie leidžia atspindėti ryšius tarp duomenų objektų.

```sql
-- Sukuriame "studentai" lentelę
CREATE TABLE studentai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  gimimo_metai DATE,
  klase_id INTEGER REFERENCES klases (id)
);

-- Sukuriame "mokytojai" lentelę
CREATE TABLE mokytojai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  dirba_nuo DATE,
  dalykas_id INTEGER REFERENCES dalykai (id)
);

-- Sukuriame "klases" lentelę
CREATE TABLE klases (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas VARCHAR(255) NOT NULL,
  mokytojas_id INT REFERENCES mokytojai (id)
);

-- Sukuriame "pazymiai" lentelę
CREATE TABLE pazymiai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pazymys INTEGER NOT NULL,
  pazymio_data DATE NOT NULL,
  studentas_id INTEGER REFERENCES studentai (id),
  dalykas_id INTEGER REFERENCES dalykai (id)
);

-- Sukuriame "dalykai" lentelę
CREATE TABLE dalykai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas VARCHAR(255) NOT NULL
);
```

![Modeliavimas](/images/db/modeliavimas.png)

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
INSERT INTO pazymiai (id, pazymys, pazymio_data, fk_studentas_id, fk_dalykas_id)
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

## "studentai" lentelė

- Pirminis raktas (PRIMARY KEY): `id` stulpelis, kuriame saugomi unikalūs studentų identifikatoriai.
- Svetimasis raktas (FOREIGN KEY): `fk_klase_id` stulpelis, kuris nurodo, kuriai klasei priklauso studentas. Šis raktas yra susijęs su "klases" lentelės `id` stulpeliu.

## "mokytojai" lentelė

- Pirminis raktas: `id` stulpelis, kuriame saugomi unikalūs mokytojų identifikatoriai.
- Svetimasis raktas: `fk_dalykas_id` stulpelis, kuris nurodo, kokį dalyką moko mokytojas. Šis raktas yra susijęs su "dalykai" lentelės `id` stulpeliu.

## "klases" lentelė

- Pirminis raktas: `id` stulpelis, kuriame saugomi unikalūs klasės identifikatoriai.
- Svetimasis raktas: `fk_mokytojas_id` stulpelis, kuris nurodo, kuris mokytojas yra klasės vadovas. Šis raktas yra susijęs su "mokytojai" lentelės `id` stulpeliu.

## "pazymiai" lentelė

- Pirminis raktas: `id` stulpelis, kuriame saugomi unikalūs pažymių identifikatoriai.
- Svetimieji raktai:
`fk_studentas_id` stulpelis, kuris nurodo, kuriam studentui priklauso pažymys. Šis raktas yra susijęs su "studentai" lentelės `id` stulpeliu.
`fk_dalykas_id` stulpelis, kuris nurodo, iš kurio dalyko yra pažymys. Šis raktas yra susijęs su "dalykai" lentelės `id` stulpeliu.

## "dalykai" lentelė

- Pirminis raktas: `id` stulpelis, kuriame saugomi unikalūs dalykų identifikatoriai.
Šioje lentelėje nėra svetimųjų raktų, tačiau ji turi ryšius su kitomis lentelėmis per savo `id` stulpelį, kuris yra naudojamas kaip svetimasis raktas kitose lentelėse.

### "studentai" ir "klases"

Viena klasė gali turėti daug studentų, o kiekvienas studentas priklauso tik vienai klasei. "studentai" lentelėje yra foreign key laukas `fk_klase_id`, kuris rodo į "klases" lentelės `id`.

### "mokytojai" ir "dalykai"

Kiekvienas mokytojas moko vieno dalyko, bet kiekvienas dalykas gali būti mokomas kelių mokytojų. "mokytojai" lentelėje yra foreign key laukas `fk_dalykas_id`, kuris rodo į "dalykai" lentelės `id`.

### "klases" ir "mokytojai"

Kiekvienai klasei yra priskirtas vienas mokytojas kaip klasės vadovas, bet kiekvienas mokytojas gali būti vadovu kelioms klasėms. "klases" lentelėje yra foreign key laukas `fk_mokytojas_id`, kuris rodo į "mokytojai" lentelės `id`.

### "pazymiai" ir "studentai"

Kiekvienas studentas gali turėti daug įvertinimų (pazymiai), bet kiekvienas įvertinimas yra priskirtas tik vienam studentui. "pazymiai" lentelėje yra foreign key laukas `fk_studentas_id`, kuris rodo į "studentai" lentelės `id`.

### "pazymiai" ir "dalykai"

Kiekvienas dalykas gali turėti daug įvertinimų (pazymiai), bet kiekvienas įvertinimas yra priskirtas tik vienam dalykui. "pazymiai" lentelėje yra foreign key laukas `fk_dalykas_id`, kuris rodo į "dalykai" lentelės `id`.
