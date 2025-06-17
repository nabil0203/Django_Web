-- Active: 1749205642186@@127.0.0.1@5432@student_management@public
-- 1:39:55


-- Group by
-- Removes Duplicate




-- There are some course_id in the database
-- Multiple students have Same course
-- Group them by the "course_id" and "count". This shows which course has how many students



-- Remove Duplicate
SELECT course_id FROM students
GROUP BY course_id;



-- Counts how many students are in a specific course
SELECT course_id, COUNT(*) 
FROM students
GROUP BY course_id;



-- Which GPA has how many students
SELECT gpa, COUNT(*) 
FROM students
GROUP BY gpa;



-- Average gpa of each course
SELECT course_id, AVG(gpa)
FROM students
GROUP BY course_id;




-- Max gpa of each course
SELECT course_id, MAX(gpa)
FROM students
GROUP BY course_id;




-- Max gpa of each course without NULL
SELECT course_id, MAX(gpa)
FROM students
WHERE course_id IS NOT NULL
GROUP BY course_id;






