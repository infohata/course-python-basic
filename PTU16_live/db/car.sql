SELECT first_name, last_name, name, plate FROM person, car, company
    WHERE person.car_id = car.id AND person.company_id = company.id
        AND make="Ford"
    ORDER BY name;

SELECT first_name, last_name, name, plate, make FROM person
    JOIN company ON company_id=company.id
    JOIN car ON car_id=car.id
    WHERE make="Ford"
    ORDER BY name;

SELECT name, count(*) AS employees FROM person 
    JOIN company ON company_id=company.id
    GROUP BY name
    HAVING employees >= 3;

SELECT name, plate FROM person
    JOIN car ON car_id=car.id
    JOIN company ON company_id=company.id
    WHERE name="Apple";

SELECT company_id FROM person GROUP BY company_id HAVING count() >= 3;

SELECT first_name, last_name, name, make FROM person
    JOIN company ON company_id=company.id
    JOIN car ON car_id=car.id
    WHERE company_id IN (
        SELECT company_id FROM person GROUP BY company_id HAVING count() >= 3
    )
    ORDER BY name;


-- SELECT
-- JOIN
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY

UPDATE person SET car_id=1 WHERE id IN (
    SELECT person.id FROM person LEFT JOIN car ON car_id=car.id
        WHERE car_id IS NULL
);

SELECT count() FROM person LEFT JOIN car ON car_id=car.id WHERE car_id IS NULL;
