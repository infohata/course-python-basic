-- SQLite
CREATE TABLE client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    address VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20)
);

-- ALTER TABLE client ADD phone VARCHAR(20);
-- ALTER TABLE client DROP email;
-- DROP TABLE client;

INSERT INTO client (first_name, last_name, address, email, phone)
    VALUES ("Kestutis", "Januskevicius", "Middle of Nowhere", "kestas@gka.lt", "+37069xxx411");
INSERT INTO client (first_name, last_name, address, email, phone)
    VALUES ("Piktas", "Trintukas", "Middle of Everywhere", "piktas@gka.lt", "nesakysiu");

SELECT * FROM client;

UPDATE client SET phone="+37069xxx411" WHERE id=1;
DELETE FROM client WHERE first_name="Piktas";
