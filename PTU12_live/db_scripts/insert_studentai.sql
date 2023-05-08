INSERT INTO students (first_name, last_name, email)
VALUES ("Geras", "Studentas", "geras@gmail.com");
INSERT INTO students (first_name, last_name, email)
VALUES ("Linksmas", "Smagulis", "smagulis@gmail.com");
INSERT INTO students (first_name, last_name, email)
VALUES ("Tikras", "Vyras", "vyras@gmail.com");
INSERT INTO students (first_name, last_name, email, address)
VALUES ("Linksma", "Gerulė", "linksma@gerule.lt", "visur");

SELECT * FROM students WHERE id > 4;
SELECT * FROM students WHERE first_name = "Geras";
SELECT * FROM students WHERE address IS NULL;
SELECT * FROM students WHERE NOT address IS NULL;
SELECT * FROM students;

DELETE FROM students WHERE id > 4;
UPDATE students SET phone = "+37069999888";
UPDATE students SET address = "niekur" WHERE address IS NULL;
UPDATE students SET last_name = "Smagulis" WHERE id = 2;
