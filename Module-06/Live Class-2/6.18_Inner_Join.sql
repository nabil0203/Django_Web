-- 2:00:00


-- INNER Join
-- common of the both table


-- 2 tables --> "students", "courses"
-- each table has common column--> 'course_id'
-- depending on that, we are getting the details together

SELECT
    students.first_name,
    students.last_name,
    courses.course_name,
    courses.department
FROM students
INNER JOIN courses 
ON students.course_id = courses.course_id;






