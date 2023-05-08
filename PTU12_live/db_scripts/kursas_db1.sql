-- db1/person.db

SELECT * FROM person;
SELECT first_name, gender FROM person;
SELECT first_name, gender FROM person ORDER BY gender, first_name;
SELECT DISTINCT gender FROM person;
SELECT * FROM person WHERE gender="Male";
SELECT * FROM person WHERE date_of_birth > DATE("1995-01-01");
SELECT * FROM person 
    WHERE gender="Male" 
    AND date_of_birth < DATE("1995-01-01");
SELECT * FROM person ORDER BY date_of_birth DESC;
