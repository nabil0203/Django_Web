-- 56:10



-- Common Table Expression (CTE)
-- name a Query in a temporary name
-- like variable




-- Example-1
-- setting name of a query as 'AVG_SALARY'
WITH AVG_SALARY AS(
    SELECT AVG(salary) FROM Employees;
)

-- using the CTE
SELECT * FROM Employees
    WHERE Salary > AVG_SALARY;









-- Example-2
-- setting name of a query as 'HighEarners'
WITH HighEarners AS (
    SELECT Name, Salary
    FROM Employees
    WHERE Salary > 100000
)


-- using the CTE
SELECT * FROM HighEarners;



