INSERT INTO dalykai (name, description)
VALUES ("Python Essentials", "Introductionary course to Python");
INSERT INTO dalykai (name)
VALUES ("Databases and SQLite");

UPDATE students SET subject_id = 1;
UPDATE students SET subject_id = 2 WHERE id >= 3;

--
SELECT 
    first_name, last_name, 
    dalykai.name AS subject
FROM students JOIN dalykai 
    ON subject_id = dalykai.id;
