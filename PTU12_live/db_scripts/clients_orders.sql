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

INSERT INTO Klientai (vardas, pavarde, el_pastas, telefonas)
VALUES ("Geras", "Klientas", "geras@gmail.com", "+37066655555");
INSERT INTO Klientai (vardas, pavarde, el_pastas, telefonas)
VALUES ("Linksmas", "Samulis", "samulis@gmail.com", "+37062133377");
INSERT INTO Klientai (vardas, pavarde, el_pastas, telefonas)
VALUES ("Grazi", "Mergaite", "grazuole@gmail.com", "+37068912345");

INSERT INTO Uzsakymai (uzsakymo_data, kiekis, suma, kliento_id)
VALUES (DATE("2023-02-14"), 7, 42.69, 3);
INSERT INTO Uzsakymai (uzsakymo_data, kiekis, suma, kliento_id)
VALUES (DATE("2023-03-19"), 1, 23.14, 1);

SELECT 
    Uzsakymai.*, 
    Klientai.vardas, 
    Klientai.pavarde, 
    klientai.el_pastas 
FROM Uzsakymai JOIN Klientai 
ON Uzsakymai.kliento_id = Klientai.id;

SELECT * FROM Klientai
LEFT JOIN Uzsakymai ON Uzsakymai.kliento_id = Klientai.id;
