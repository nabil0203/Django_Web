-- 1:24:00


-- LIKE keyword is used to match patterns




SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
WHERE first_name LIKE 'J%';             -- 'J%'----> First name Starts with J





SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
WHERE first_name LIKE '%e';             -- '%e'----> must ends with 'e', anything before it






SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
WHERE first_name LIKE '%a%';             -- '%a%'----> 'a' in the middle, anything before+after




SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
WHERE first_name LIKE 'J___';             -- 'J___'----> 3 underscore means, there could be only 3 letters after J





SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
WHERE first_name LIKE '____';             -- '____'----> 4 underscore means, All Names that has only 4 characters




SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
WHERE first_name LIKE '_o%';             -- any character at first, then 'o', after than any number of character



