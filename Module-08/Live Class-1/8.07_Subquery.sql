-- 51:10


-- Subquery
-- a query under another query




SELECT * FROM Employees
    WHERE Salary > (SELECT AVG(salary) FROM Employees)


