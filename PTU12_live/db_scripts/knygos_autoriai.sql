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
  fk_knyga_id INTEGER REFERENCES knygos(id),
  fk_autorius_id INTEGER REFERENCES autoriai(id)
);

INSERT INTO knygos (pavadinimas) VALUES ("Lietuvos paukščiai");
INSERT INTO knygos (pavadinimas) VALUES ("Dažniausiai perintys paukščiai Lietuvoje");
INSERT INTO knygos (pavadinimas) VALUES ("Vaiduoklis");
INSERT INTO knygos (pavadinimas) VALUES ("Gelbėtojas");
INSERT INTO knygos (pavadinimas) VALUES ("Talismanas");

INSERT INTO autoriai (vardas, pavarde) VALUES ("Marius", "Karlonas");
INSERT INTO autoriai (vardas, pavarde) VALUES ("Jo", "Nesbo");
INSERT INTO autoriai (vardas, pavarde) VALUES ("Stephan", "King");
INSERT INTO autoriai (vardas, pavarde) VALUES ("Peter", "Straub");

SELECT * FROM autoriai;
SELECT * FROM knygos;
SELECT * FROM knygos_autoriai;

INSERT INTO knygos_autoriai (fk_autorius_id, fk_knyga_id) VALUES (1, 1);
INSERT INTO knygos_autoriai (fk_autorius_id, fk_knyga_id) VALUES (1, 2);
INSERT INTO knygos_autoriai (fk_autorius_id, fk_knyga_id) VALUES (2, 3);
INSERT INTO knygos_autoriai (fk_autorius_id, fk_knyga_id) VALUES (2, 4);
INSERT INTO knygos_autoriai (fk_autorius_id, fk_knyga_id) VALUES (3, 5);
INSERT INTO knygos_autoriai (fk_autorius_id, fk_knyga_id) VALUES (4, 5);

SELECT 
  autoriai.id AS autorius_id,
  vardas || " " || pavarde AS vardas_pavarde, 
  knygos.id AS knygos_id,
  pavadinimas
FROM knygos_autoriai 
JOIN autoriai ON fk_autorius_id = autoriai.id
JOIN knygos ON fk_knyga_id = knygos.id
ORDER BY pavarde;
