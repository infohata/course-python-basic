# SQL sintaksė pagrindiniams CRUD veiksmams (CREATE, READ, UPDATE, DELETE)

Pirma, sukursime lentelę "studentai" su šiais stulpeliais: "id", "vardas", "pavarde", "gimimo_metai" ir "miestas".

```sql
CREATE TABLE studentai (
  id INT PRIMARY KEY,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  gimimo_metai DATE,
  miestas VARCHAR(255)
);
```

## INSERT

INSERT sakinys naudojamas norint įterpti naujus įrašus į lentelę.
Įterpkime naują įrašą į lentelę "studentai":

```sql
INSERT INTO studentai (id, vardas, pavarde, gimimo_metai, miestas) 
VALUES (1, 'Jonas', 'Jonaitis', '2000-01-01', 'Vilnius');
```

## SELECT (...WHERE)

SELECT sakinys naudojamas norint nuskaityti duomenis iš vienos ar kelių lentelių. Jis gali būti papildytas WHERE sąlyga, kad nuskaitytų tik tuos įrašus, kurie atitinka nurodytą sąlygą.

```sql
-- Parodo visus įrašus iš lentelės "studentai"
SELECT * FROM studentai;
```

```sql
-- Parodo tik tuos įrašus, kurių miestas yra 'Vilnius'
SELECT * FROM studentai WHERE miestas = 'Vilnius';
```

## UPDATE (...WHERE)

UPDATE sakinys naudojamas norint atnaujinti vieną ar kelis stulpelius esamame įraše. Jis gali būti papildytas WHERE sąlyga, kad atnaujintų tik tuos įrašus, kurie atitinka nurodytą sąlygą.

```sql
-- Atnaujina visų studentų, kurių miestas yra 'Vilnius', miestą į 'Kaunas'
UPDATE studentai SET miestas = 'Kaunas' WHERE miestas = 'Vilnius';
```

## DELETE (...WHERE)

DELETE sakinys naudojamas norint pašalinti vieną ar kelis įrašus iš lentelės. Jis gali būti papildytas WHERE sąlyga, kad pašalintų tik tuos įrašus, kurie atitinka nurodytą sąlygą.

```sql
-- Pašalina visus įrašus iš lentelės "studentai", kurių miestas yra 'Kaunas'
DELETE FROM studentai WHERE miestas = 'Kaunas';
```

Pavyzdys, jei norite ištrinti kelis įrašus naudodami OR (arba) sąlygą:

```sql
DELETE FROM studentai WHERE miestas = 'Kaunas' OR miestas = 'Vilnius';
```

Pavyzdys, jei norite ištrinti įrašą naudodami AND sąlygą:

```sql
DELETE FROM studentai WHERE miestas = 'Kaunas' AND gimimo_metai > '2000-01-01';
```

## Užduotys

### Pirma užduotis

Sukurkite lentelę "mokytojai" su šiais stulpeliais: "id", "vardas", "pavarde", "specialybe" ir "patirtis_metais".

### Antra užduotis

Įterpkite šiuos įrašus į sukurtą lentelę "mokytojai":

```text
Mokytojas su ID 1, vardu Petras, pavarde Petraitis, specialybe Matematika ir 10 metų patirtimi.
Mokytojas su ID 2, vardu Ona, pavarde Onaitė, specialybe Fizika ir 11 metų patirtimi.
Mokytojas su ID 3, vardu Marius, pavarde Marijus, specialybe Biologija ir 8 metų patirtimi.
Mokytojas su ID 4, vardu Rasa, pavarde Rasaitė, specialybe Anglų kalba ir 12 metų patirtimi.
Mokytojas su ID 5, vardu Aurimas, pavarde Aurimaitis, specialybe Lietuvių kalba ir 5 metų patirtimi.
Mokytojas su ID 6, vardu Gintare, pavarde Gintarėlė, specialybe Istorija ir 3 metų patirtimi.
```

### Trečia užduotis

Parodykite visus įrašus iš lentelės "mokytojai", kurių specialybė yra "Matematika".

### Ketvirta užduotis

Atnaujinkite visus įrašus lentelėje "mokytojai", kurių patirtis_metais yra mažesnė nei 6, padidindami jų patirties metų skaičių vienetu

### Penkta užduotis

Pašalinkite visus įrašus iš lentelės "mokytojai", kurių specialybė yra "Fizika" ir patirtis_metais yra daugiau nei 10.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```sql
CREATE TABLE mokytojai (
  id INT PRIMARY KEY,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  specialybe VARCHAR(255) NOT NULL,
  patirtis_metais INT
);
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```sql
-- Įterpiame pirmąjį mokytoją
INSERT INTO mokytojai (id, vardas, pavarde, specialybe, patirtis_metais)
VALUES (1, 'Petras', 'Petraitis', 'Matematika', 10);

-- Įterpiame antrąjį mokytoją
INSERT INTO mokytojai (id, vardas, pavarde, specialybe, patirtis_metais)
VALUES (2, 'Ona', 'Onaitė', 'Fizika', 11);

-- Įterpiame trečiąjį mokytoją
INSERT INTO mokytojai (id, vardas, pavarde, specialybe, patirtis_metais)
VALUES (3, 'Marius', 'Marijus', 'Biologija', 8);

-- Įterpiame ketvirtąjį mokytoją
INSERT INTO mokytojai (id, vardas, pavarde, specialybe, patirtis_metais)
VALUES (4, 'Rasa', 'Rasaitė', 'Anglų kalba', 12);

-- Įterpiame penktąjį mokytoją
INSERT INTO mokytojai (id, vardas, pavarde, specialybe, patirtis_metais)
VALUES (5, 'Aurimas', 'Aurimaitis', 'Lietuvių kalba', 5);

-- Įterpiame šeštąjį mokytoją
INSERT INTO mokytojai (id, vardas, pavarde, specialybe, patirtis_metais)
VALUES (6, 'Gintare', 'Gintarėlė', 'Istorija', 3);
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```sql
SELECT * FROM mokytojai WHERE specialybe = 'Matematika';
```

</details>
<details>
<summary>Ketvirta užduotis</summary>
<hr>

```sql
UPDATE mokytojai SET patirtis_metais = patirtis_metais + 1 WHERE patirtis_metais < 6;
```

</details>
<details>
<summary>Penkta užduotis</summary>
<hr>

```sql
DELETE FROM mokytojai WHERE specialybe = 'Fizika' AND patirtis_metais > 10;
```

</details>
</details>