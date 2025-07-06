-- 2:14:45


-- FULL join
-- ALL Right + ALL Left



-- 2 tables--> "students", "courses"
-- each table has common column--> 'course_id'
-- depending on that, we are getting the details together




SELECT
    students.first_name,
    students.last_name,
    courses.course_name,
    courses.department
FROM students
FULL JOIN courses 
ON students.course_id = courses.course_id;

