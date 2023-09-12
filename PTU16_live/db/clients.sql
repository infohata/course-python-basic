-- SQLite
CREATE TABLE address (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    street VARCHAR(100),
    zip VARCHAR(10),
    city VARCHAR(50),
    country VARCHAR(50)    
);

CREATE TABLE client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    address_id INTEGER UNIQUE NOT NULL REFERENCES address(id)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time DATETIME,
    quantity DECIMAL(10,2),
    total DECIMAL(10,2),
    client_id INTEGER NOT NULL REFERENCES client(id),
    address_id INTEGER REFERENCES address(id)
);

-- ALTER TABLE client ADD phone VARCHAR(20);
-- ALTER TABLE client DROP email;
-- DROP TABLE client;

INSERT INTO address (street, zip, city, country) VALUES 
    ("Middle of Everywhere", "92307", "Klaipėda", "Lithuania"),
    ("Middle of Nowhere", "82820", "Maukkula", "Finland");

INSERT INTO client (first_name, last_name, address_id, email, phone)
    VALUES ("Kestutis", "Januskevicius", 2, "kestas@gka.lt", "+37069xxx411");
INSERT INTO client (first_name, last_name, address_id, email, phone)
    VALUES ("Piktas", "Trintukas", 1, "piktas@gka.lt", "nesakysiu");

SELECT * FROM client;

UPDATE client SET phone="+37069xxx411" WHERE id=1;
DELETE FROM client WHERE first_name="Piktas";

SELECT * FROM client, address WHERE client.address_id=address.id;
SELECT first_name, last_name, street, city 
    FROM client, address WHERE client.address_id=address.id;

SELECT first_name, last_name, street, city 
    FROM client, address WHERE client.address_id=address.id
        AND city="Maukkula";
SELECT first_name, last_name, street, city FROM client
    JOIN address ON client.address_id=address.id
        WHERE city="Maukkula";
