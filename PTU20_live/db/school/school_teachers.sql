-- school_teachers
INSERT INTO teacher (first_name, last_name, subject_id)
VALUES ('Petras', 'Petraitis', 1),
       ('Ona', 'Onaite', 2),
       ('Marius', 'Marijus', 3),
       ('Rasa', 'Rasaite', 1)
;

UPDATE teacher SET subject_id = 1 WHERE id = 4;