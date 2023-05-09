SELECT * FROM cars WHERE year BETWEEN 2010 AND 2023;
SELECT * FROM cars WHERE year IN (2005, 2011) ORDER BY price;
SELECT * FROM cars WHERE make LIKE "Merc%";
SELECT * FROM cars WHERE make LIKE "__d%";
SELECT * FROM cars WHERE model LIKE "__0%";
SELECT * FROM cars WHERE color IS NULL;
SELECT * FROM cars WHERE price > 50000 AND year < 2000;
SELECT * FROM cars WHERE NOT price > 50000 AND year < 2000;
-- visi Mercury arba Fordai kainuojantys iki 10k ir virs 50k
SELECT * FROM cars 
    WHERE (make = "Mercury" OR make = "Ford")
    AND price NOT BETWEEN 10000 AND 50000;
-- visi Mercury arba visi Fordai iki 10k ir virs 50k
SELECT * FROM cars 
    WHERE make = "Mercury" OR make = "Ford"
    AND price NOT BETWEEN 10000 AND 50000;
-- visi Mercury iki 10k ir virs 50k arba visi Fordai
SELECT * FROM cars 
    WHERE price NOT BETWEEN 10000 AND 50000
    AND make = "Mercury" OR make = "Ford";
SELECT * FROM cars ORDER BY price;
SELECT * FROM cars WHERE make="Ford" ORDER BY price;
SELECT * FROM cars WHERE make="Mercury" ORDER BY year DESC;
SELECT * FROM cars WHERE model LIKE "%s" COLLATE NOCASE;
SELECT make || " " || model FROM cars;
SELECT make || " " || model AS car, year FROM cars;
SELECT sum(price) from cars;
SELECT make, model, year, color, price, 
    ROUND(price / 3.4528, 2) AS eurais 
    FROM cars ORDER by eurais;
SELECT avg(price), avg(year), 
    max(price), max(year), 
    min(price), min(year) 
    FROM cars;
SELECT make, model, max(price) FROM cars;
SELECT make, count(DISTINCT model), count(*) 
    FROM cars GROUP BY make 
    HAVING count(*) > count(DISTINCT model);
SELECT make, model, color, max(price) FROM cars
    GROUP BY color ORDER BY price DESC;

-- pvz. su senais brangiais Mercury
SELECT * FROM cars WHERE make = "Mercury";
-- WHERE taikoma prieš grupavimą, HAVING po grupavimo
SELECT make, model, year, max(price) FROM cars
    -- WHERE year > 2000
    GROUP BY make
    HAVING year > 2000
;
