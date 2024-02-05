SELECT subject.id AS subject_id, name, 
    teacher.id AS teacher_id, first_name, last_name
    FROM teacher JOIN subject ON subject_id = subject.id;

SELECT schedule.id, weekday, start_time, codename, name, last_name
    FROM schedule 
    JOIN subject ON schedule.subject_id = subject.id
    JOIN teacher ON teacher_id = teacher.id
    JOIN classroom ON classroom_id = classroom.id
    -- WHERE classroom.codename = "code01";
    -- WHERE teacher_id = 2
    ORDER BY codename, weekday, start_time;

SELECT student.id AS std_id, first_name, last_name, 
    classroom.id AS class_id, codename FROM student
    JOIN classroom ON classroom_id = classroom.id
    ORDER BY classroom.id, student.id;

SELECT weekday, start_time, 
    student.id AS std_id, student.last_name,
    subject.id AS sub_id, subject.name,
    teacher.id AS t_id, teacher.last_name
    FROM schedule
    JOIN subject ON schedule.subject_id = subject.id
    JOIN classroom ON schedule.classroom_id = classroom.id
    JOIN teacher ON schedule.teacher_id = teacher.id
    JOIN student ON student.classroom_id = classroom.id;

SELECT assigned_at, grade, subject.name, teacher.last_name 
FROM grade 
JOIN subject ON grade.subject_id = subject.id
JOIN teacher ON grade.teacher_id = teacher.id
WHERE student_id = 1;

SELECT AVG(grade), subject.name, teacher.last_name 
FROM grade 
JOIN subject ON grade.subject_id = subject.id
JOIN teacher ON grade.teacher_id = teacher.id
JOIN student ON grade.student_id = student.id
WHERE student.last_name = "Simaitis"
GROUP BY grade.teacher_id;
