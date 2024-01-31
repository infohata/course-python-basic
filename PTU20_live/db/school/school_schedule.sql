-- school_schedule

DELETE FROM schedule;
-- code01
INSERT INTO schedule 
    (weekday, start_time, subject_id, classroom_id, teacher_id)
VALUES (0, TIME("08:00"), 1, 1, 1),
    (0, TIME("13:00"), 2, 1, 2),
    (1, TIME("08:00"), 1, 1, 1),
    (1, TIME("13:00"), 3, 1, 3),
    (2, TIME("08:00"), 1, 1, 1),
    (2, TIME("13:00"), 2, 1, 2),
    (3, TIME("08:00"), 1, 1, 1),
    (3, TIME("13:00"), 3, 1, 3);

-- code02
INSERT INTO schedule 
    (weekday, start_time, subject_id, classroom_id, teacher_id)
VALUES (0, TIME("08:00"), 1, 2, 4),
    (0, TIME("13:00"), 3, 2, 3),
    (1, TIME("08:00"), 1, 2, 4),
    (1, TIME("13:00"), 2, 2, 2),
    (2, TIME("08:00"), 1, 2, 4),
    (2, TIME("13:00"), 3, 2, 3),
    (3, TIME("08:00"), 1, 2, 4),
    (3, TIME("13:00"), 2, 2, 2);

-- UPDATE schedule SET classroom_id = 2 WHERE id >= 9;
-- UPDATE schedule SET subject_id = 2 WHERE id IN (12, 16);
-- UPDATE schedule SET subject_id = 3 WHERE id IN (10, 14);

-- code03
INSERT INTO schedule 
    (weekday, start_time, subject_id, classroom_id, teacher_id)
VALUES (0, TIME("08:00"), 2, 3, 2),
    (0, TIME("13:00"), 1, 3, 1),
    (1, TIME("08:00"), 3, 3, 3),
    (1, TIME("13:00"), 1, 3, 1),
    (2, TIME("08:00"), 2, 3, 2),
    (2, TIME("13:00"), 1, 3, 1),
    (3, TIME("08:00"), 3, 3, 3),
    (3, TIME("13:00"), 1, 3, 1);

-- code04
INSERT INTO schedule 
    (weekday, start_time, subject_id, classroom_id, teacher_id)
VALUES (0, TIME("08:00"), 3, 4, 3),
    (0, TIME("13:00"), 1, 4, 4),
    (1, TIME("08:00"), 2, 4, 2),
    (1, TIME("13:00"), 1, 4, 4),
    (2, TIME("08:00"), 3, 4, 3),
    (2, TIME("13:00"), 1, 4, 4),
    (3, TIME("08:00"), 2, 4, 2),
    (3, TIME("13:00"), 1, 4, 4);
