SELECT student.id, first_name, last_name, codename FROM student
    JOIN classroom ON classroom_id = classroom.id
    ORDER BY last_name, first_name;
