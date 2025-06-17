-- Active: 1749205642186@@127.0.0.1@5432@student_management@public
-- 1:36:10



SELECT count(*) FROM students;                             -- count the number of rows




SELECT count(*)
FROM students 
WHERE
    first_name LIKE 'J%';                                  -- count the number of rows that has first_name starting with 'j'



-- ----------------------------------




SELECT first_name FROM students WHERE gpa > 3.5;                           -- shows all the data

SELECT COUNT(first_name) FROM students WHERE gpa > 3.5;                    -- counts it


