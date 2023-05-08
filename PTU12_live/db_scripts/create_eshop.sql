CREATE TABLE uzsakymas (
	id integer PRIMARY KEY AUTOINCREMENT,
	suma numeric(18,2),
	klientas_id integer REFERENCES klientas(id),
	data_laikas datetime
);

CREATE TABLE klientas (
	id integer PRIMARY KEY AUTOINCREMENT,
	vardas varchar(50),
	pavarde varchar(50)
);

CREATE TABLE produktas (
	id integer PRIMARY KEY AUTOINCREMENT,
	pavadinimas varchar(100),
	kaina numeric(18,2)
);

CREATE TABLE uzsakymo_eilute (
	id integer PRIMARY KEY AUTOINCREMENT,
	uzsakymas_id integer REFERENCES uzsakymas(id),
	produktas_id integer REFERENCES produktas(id),
	kiekis integer
);


INSERT INTO klientas (vardas, pavarde) VALUES ("Andrius", "Gedvilas");
INSERT INTO produktas (pavadinimas, kaina) VALUES ("Padanga", 1250);
INSERT INTO produktas (pavadinimas, kaina) VALUES ("Valytuvas", 50);
INSERT INTO uzsakymas (data_laikas, klientas_id) 
	VALUES ("2023-05-08 14:00:00", 1);
INSERT INTO uzsakymo_eilute (uzsakymas_id, produktas_id, kiekis) 
	VALUES (1, 1, 14);
INSERT INTO uzsakymo_eilute (uzsakymas_id, produktas_id, kiekis) 
	VALUES (1, 2, 2);

SELECT vardas || " " || pavarde as vardas_pavarde, data_laikas, uzsakymas.id
FROM uzsakymas JOIN klientas ON klientas_id = klientas.id
WHERE uzsakymas.id = 1;

SELECT pavadinimas, kiekis, kaina, kiekis * kaina AS suma 
	FROM uzsakymo_eilute 
	JOIN produktas ON produktas_id = produktas.id
	WHERE uzsakymas_id = 1;

SELECT sum(kiekis * kaina) AS viso 
	FROM uzsakymo_eilute 
	JOIN produktas ON produktas_id = produktas.id
	WHERE uzsakymas_id = 1;
