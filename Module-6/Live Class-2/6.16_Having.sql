-- Active: 1749205642186@@127.0.0.1@5432@student_management@public
-- 1:52:10


-- Having
-- when we apply condition on a Group field------------>HAVING
--                  example:- sum, count, avg

-- when we apply condition on a Single column/field---->WHERE
--                  example:- a specific column






-- Which course has GPA higher than 3.5
SELECT course_id, MAX(gpa)
FROM students
WHERE course_id IS NOT NULL
GROUP BY course_id
HAVING MAX(gpa) > 3.5;





-- Which course has an Average GPA higher than 3.5
SELECT course_id, AVG(gpa)
FROM students
WHERE course_id IS NOT NULL
GROUP BY course_id
HAVING AVG(gpa) > 3.5;




-- Courses that have more than 1 student
SELECT course_id, COUNT(*)
FROM students
WHERE course_id IS NOT NULL
GROUP BY course_id
HAVING COUNT(*) > 1;


