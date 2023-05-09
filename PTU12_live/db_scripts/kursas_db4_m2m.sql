CREATE TABLE coder (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	f_name VARCHAR(50) NOT NULL,
    l_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INTEGER CHECK (age >= 10 AND age < 100),
    xp_years INTEGER CHECK (age - xp_years >= 10)
);

INSERT INTO coder (f_name, l_name, email, age, xp_years)
VALUES ("Kestutis", "Januskevicius", "kestas@midonow.fi", 40, 30);
INSERT INTO coder (f_name, l_name, email, age, xp_years)
VALUES ("Nepatyres", "Programuotojas", "noobas@midonow.fi", 35, 0);

SELECT * FROM coder;

UPDATE coder SET xp_years = 28 WHERE AGE >= 38;

CREATE TABLE teams (
  id integer PRIMARY KEY,
  name string
);

CREATE TABLE coders (
  id integer PRIMARY KEY,
  f_name string NOT NULL,
  l_name string NOT NULL,
  email string UNIQUE,
  age integer,
  team_id integer,
  FOREIGN KEY (team_id) REFERENCES teams (id)
);

CREATE TABLE tasks (
	id integer PRIMARY KEY,
	name string,
	coder_id integer,
	FOREIGN KEY (coder_id) REFERENCES coders (id)
);

INSERT INTO "teams" ("name") VALUES ('Back End');
INSERT INTO "teams" ("name") VALUES ('DevOps');
INSERT INTO "teams" ("name") VALUES ('Front End');

INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Jonas', 'Jonaitis', 'jj@gmail.com', '20', '1');
INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Antanas', 'Antanaitis', 'aa@gmail.com', '25', '1');
INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Juozas', 'Juozaitis', 'jj@hotmail.com', '30', '2');
INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Petras', 'Petraitis', 'pp@mail.lt', '29', '2');
INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Virgis', 'Virgutis', 'vv@gmail.com', '21', '3');
INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Tomas', 'Aidietis', 'ta@imone.lt', '35', '3');

INSERT INTO "tasks" ("name", "coder_id") VALUES ('Sutvarkyti DB', '5');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perdaryti dizainą', '1');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perdaryti formas', '2');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Atnaujinti tvarkykles', '6');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perkrauti serverius', '5');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Atnaujinti bibliotekas', '6');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Pakeisti logotipus', '2');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Atnaujinti dokumentaciją', '3');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Ištestuoti programą', '4');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perdaryti API', '4');

SELECT f_name, l_name, name FROM coders JOIN teams ON team_id = teams.id;
SELECT f_name, l_name, name FROM tasks JOIN coders ON coder_id = coders.id;
SELECT f_name, l_name, count(name) FROM tasks 
    JOIN coders ON coder_id = coders.id GROUP BY l_name;

CREATE TABLE skills (
  id integer PRIMARY KEY,
  name integer
);
INSERT INTO "skills" ("name") VALUES ('Python');
INSERT INTO "skills" ("name") VALUES ('JS');
INSERT INTO "skills" ("name") VALUES ('CSS');
INSERT INTO "skills" ("name") VALUES ('Go');
INSERT INTO "skills" ("name") VALUES ('AWS');
INSERT INTO "skills" ("name") VALUES ('Linux');

CREATE TABLE coders_skills (
	coder_id integer,
	skill_id integer,
	FOREIGN KEY (coder_id) REFERENCES coders (id),
	FOREIGN KEY (skill_id) REFERENCES skills (id)
  );
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('1', '2');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('1', '3');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('2', '2');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('2', '3');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('3', '1');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('3', '4');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('4', '1');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('4', '6');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('5', '4');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('5', '5');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('6', '5');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('6', '6');

SELECT f_name, l_name, name FROM coders_skills 
    JOIN coders ON coder_id = coders.id
    JOIN skills ON skill_id = skills.id;

CREATE TABLE passwords (
	id integer PRIMARY KEY,
	coder_id integer UNIQUE,
	pwd string,
	FOREIGN KEY (coder_id) REFERENCES coders (id)
);
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('1', '12345');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('2', 'verisykret');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('3', 'qwerty');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('4', 'uauauai');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('5', 'slaptazodis');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('6', 'barzda');

SELECT l_name, pwd FROM coders, passwords WHERE coder_id = coders.id;
