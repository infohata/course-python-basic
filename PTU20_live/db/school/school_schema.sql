CREATE TABLE IF NOT EXISTS classroom (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codename VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS subject (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    classroom_id INTEGER REFERENCES classroom(id)
);

CREATE TABLE IF NOT EXISTS teacher (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    subject_id INTEGER REFERENCES subject(id)
);

-- DROP TABLE schedule;
CREATE TABLE IF NOT EXISTS schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    weekday INTEGER,
    start_time TIME,
    subject_id INTEGER REFERENCES subject(id),
    classroom_id INTEGER REFERENCES classroom(id),
    teacher_id INTEGER REFERENCES teacher(id)
);

CREATE TABLE IF NOT EXISTS grade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade INTEGER,
    assigned_at DATETIME,
    student_id INTEGER REFERENCES student(id),
    subject_id INTEGER REFERENCES subject(id),
    teacher_id INTEGER REFERENCES teacher(id)
);
