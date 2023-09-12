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


INSERT INTO knygos (pavadinimas) VALUES
    ("Monk who sold his Ferrarri"), ("Who will cry when we die"),
    ("Sprint: How to solve big problems and test new ideas in just five days");

INSERT INTO autoriai (vardas, pavarde) VALUES
    ("Robin", "Sharma"), ("Jake", "Knapp"), ("John", "Zeratsky"), ("Braden", "Kowitz");

INSERT INTO knygos_autoriai (knyga_id, autorius_id) VALUES
    (1, 1), (2, 1), (3, 3), (3, 4), (3, 5);

SELECT * FROM knygos_autoriai;
