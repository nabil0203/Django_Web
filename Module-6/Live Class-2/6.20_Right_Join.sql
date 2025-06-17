-- 2:12:30



-- RIGHT Join
-- RIGHT all + common of the LEFT table



-- 2 tables --> "students", "courses"
-- each table has common column--> 'course_id'
-- depending on that, we are getting the details together


SELECT
    students.first_name,
    students.last_name,
    courses.course_name,
    courses.department
FROM students
RIGHT JOIN courses 
ON students.course_id = courses.course_id;

