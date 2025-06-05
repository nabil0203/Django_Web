-- 1:19:00


-- starts with capital 'K', then any length/char of text 
SELECT name FROM student WHERE name LIKE 'K%';



-- starting any length/char of text, Ends with small 'n'
SELECT name FROM student WHERE name LIKE '%n';



-- anything before+after the small 'o'
SELECT name FROM student WHERE name LIKE '%o%';