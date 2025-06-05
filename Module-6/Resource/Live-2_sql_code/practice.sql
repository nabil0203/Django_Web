SELECT * FROM students;

SELECT * FROM courses;

-- Order
SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
    -- ORDER BY gpa DESC;
ORDER BY first_name DESC, last_name ASC;

-- LIMIT
SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
ORDER BY student_id DESC
LIMIT 5;

-- LIKE
SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
WHERE
    first_name LIKE '%D%';

SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
WHERE
    first_name LIKE '%john%';

-- Aggregate
SELECT COUNT(*) FROM students WHERE first_name LIKE 'J%';

SELECT COUNT(gpa) from students WHERE gpa BETWEEN 3.5 AND 3.75;

SELECT course_id, COUNT(*) from students GROUP BY course_id;

SELECT course_id, MAX(gpa)
from students
WHERE
    course_id IS NOT NULL
GROUP BY
    course_id;

SELECT course_id, AVG(gpa)
from students
WHERE
    course_id IS NOT NULL
GROUP BY
    course_id
HAVING
    AVG(gpa) > 3.5;

SELECT course_id, COUNT(*)
from students
WHERE
    course_id IS NOT NULL
GROUP BY
    course_id
HAVING
    COUNT(*) > 1;

-- INNER JOIN
SELECT students.first_name, students.last_name, courses.course_name, courses.department, courses.instructor
FROM students
    INNER JOIN courses ON students.course_id = courses.course_id;

-- LEFT JOIN
SELECT students.first_name, students.last_name, courses.course_name, courses.department, courses.instructor
FROM students
    LEFT JOIN courses ON students.course_id = courses.course_id;

-- RIGHT JOIN
SELECT students.first_name, students.last_name, courses.course_name, courses.department, courses.instructor
FROM students
    RIGHT JOIN courses ON students.course_id = courses.course_id;

-- FULL JOIN
SELECT students.first_name, students.last_name, courses.course_name, courses.department, courses.instructor
FROM students
    FULL JOIN courses ON students.course_id = courses.course_id
    INNER JOIN omuk ON students.tomuk = omuk.tomuk;