-- 1:05:45



-- LIMIT
-- How many rows I wanna see in output




-- Show only top 3 students of high gpa
SELECT
    student_id,
    first_name,
    last_name,
    gpa
FROM students
ORDER BY gpa DESC
LIMIT 3;



