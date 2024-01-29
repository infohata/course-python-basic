INSERT INTO clients (first_name, last_name, email, phone)
    VALUES ("Geras", "Klientas", "geras@gmail.com", "+37069922211");
INSERT INTO clients (first_name, last_name, email, phone)
    VALUES ("Mokus", "Zmogus", "mokutis@gmail.com", "+37064688114");
INSERT INTO clients (first_name, last_name, email, phone)
    VALUES ("Sunkus", "Zmogus", "vargelis@kibiras.lt", "+37068812345");
INSERT INTO clients (first_name, last_name, email, phone)
    VALUES ("Grazi", "Mergaite", "grazuole@panos.lt", "+37069969699");
INSERT INTO clients (first_name, last_name, email, phone)
    VALUES ("Linksma", "Mergaite", "linksma@gmail.com", "+37066677722");
INSERT INTO clients (first_name, last_name, email, phone)
    VALUES ("Mazutis", "Zmogutis", "liolikas@gmail.com", "+37064611111");

SELECT * FROM clients;
SELECT * FROM clients WHERE id = 2;
SELECT id, first_name, last_name FROM clients;
SELECT first_name || " " || last_name AS full_name FROM clients;
SELECT * FROM clients WHERE last_name = "Mergaite";
SELECT * FROM clients WHERE email LIKE "%.lt";
SELECT * FROM clients WHERE phone LIKE "+37069%";
SELECT * FROM clients 
    WHERE email LIKE "%@gmail%" 
        AND last_name LIKE "Zmo%s";

UPDATE clients SET first_name = "Keistas" WHERE id = 3;
UPDATE clients SET last_name = "Mergiene" WHERE last_name = "Mergaite";

DELETE FROM clients WHERE id > 3;
DELETE FROM clients;
