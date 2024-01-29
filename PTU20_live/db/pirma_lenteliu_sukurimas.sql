CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(30)
);

ALTER TABLE clients ADD address TEXT(1000);
DROP TABLE clients;
