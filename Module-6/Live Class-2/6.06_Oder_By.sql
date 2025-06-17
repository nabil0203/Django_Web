-- 52:40

-- sorting using 'ORDER BY'



-- Ascending (default) order ---> based on 'gpa'
SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
ORDER BY gpa;





-- Descending order ---> based on 'gpa'
SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
ORDER BY gpa DESC;






-- Ascending (default) order ---> based on 'first_name'
SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
ORDER BY first_name;





-- Descending order ---> based on 'first_name'
SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
ORDER BY first_name DESC;