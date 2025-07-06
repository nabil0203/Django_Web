-- 1:40:00


-- Specific element search


-- searching exact roll
SELECT * FROM student WHERE roll IN(1, 3, 6);



-- those whose roll is not 1,3,6
SELECT * FROM student WHERE roll NOT IN(1, 3, 6);

