-- db1/darbuotojai.db

SELECT COUNT(VARDAS), COUNT(DISTINCT PAREIGOS), SKYRIUS_PAVADINIMAS 
    FROM DARBUOTOJAI 
    GROUP BY SKYRIUS_PAVADINIMAS;

SELECT DISTINCT PAREIGOS, SKYRIUS_PAVADINIMAS, COUNT(VARDAS) AS KIEKIS
    FROM DARBUOTOJAI
    GROUP BY PAREIGOS;

SELECT DISTINCT PAREIGOS, SKYRIUS_PAVADINIMAS, COUNT(VARDAS) AS KIEKIS
    FROM DARBUOTOJAI
    GROUP BY PAREIGOS
    HAVING KIEKIS > 2;
