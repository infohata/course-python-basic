-- Lentelių jungimas per WHERE sąlygą
SELECT first_name, last_name, plate FROM person, car
    WHERE person.car_id = car.id;

SELECT first_name, last_name, plate, name FROM person, car, company
    WHERE person.car_id = car.id AND person.company_id = company.id
    ORDER BY name;

SELECT first_name, last_name, make, plate, name FROM person, car, company
    WHERE person.car_id = car.id AND person.company_id = company.id
    AND NOT make="Ford"
    ORDER BY name;

-- Lentelių jungimas per JOIN
SELECT first_name, last_name, plate 
FROM person JOIN car ON person.car_id = car.id;

SELECT first_name, last_name, make, model, plate, name
FROM person 
JOIN car ON person.car_id = car.id
JOIN company ON person.company_id = company.id;

SELECT first_name, last_name, make, model, plate, name
FROM person 
JOIN car ON person.car_id = car.id
JOIN company ON person.company_id = company.id
WHERE make = "Ford"
ORDER BY last_name;

SELECT name, count() FROM person JOIN company
    ON person.company_id = company.id
    GROUP BY name;

SELECT name, count() FROM person JOIN company
    ON person.company_id = company.id
    GROUP BY name
    HAVING count() = 3;

SELECT name, plate FROM person JOIN car ON car_id = car.id
    JOIN company ON company_id = company.id
    ORDER BY name;

SELECT first_name, last_name, make, model, name FROM person
    JOIN company ON company_id = company.id
    JOIN car ON car_id = car.id
    WHERE company_id IN (
        SELECT company_id FROM person GROUP BY company_id
            HAVING count() <= 3
    ) ORDER BY name;

SELECT make, count() FROM person
    JOIN company ON company_id = company.id
    JOIN car ON car_id = car.id
    WHERE company_id IN (
        SELECT company_id FROM person GROUP BY company_id
            HAVING count() <= 3
    ) GROUP BY make ORDER BY count() DESC;

INSERT INTO person (first_name, last_name, email, car_id) VALUES ("Jonas", "Bedarbis", "bomzas@gmail.com", 14);
INSERT INTO company (name) VALUES ("Tesla");
INSERT INTO car (make, model, plate) VALUES ("Tesla", "Model 3", "XXX 999");

SELECT last_name, car_id, make, model, name FROM person
LEFT JOIN car ON person.car_id = car.id
LEFT JOIN company on person.company_id = company.id
WHERE car_id IS NULL OR company_id IS NULL;

SELECT id, make, model FROM car WHERE id NOT IN (
    SELECT DISTINCT car_id FROM person 
        WHERE car_id IS NOT NULL ORDER BY car_id
);
