-- 20:00


-- UNIQUE
-- ensures all the values in column are distinct





CREATE Table Employees(
    Employee_ID INT PRIMARY KEY,                        -- PRIMARY KEY is by default Unique
    Email VARCHAR(255) UNIQUE                           -- "Unique" used; same email can't be stored
);





-- Inserting values
INSERT INTO Employees
VALUES
    (1, 'abc@gmail.com'),
    (2, 'xyz@gmail.com'),
    (3, 'pqr@gmail.com');





-- Inserting the same values
INSERT INTO Employees                              -- this will throw an error; Bcz duplicate key value violates unique constraint "employees_email_key"
VALUES
    (4, 'abc@gmail.com'),
    (5, 'xyz@gmail.com'),
    (6, 'pqr@gmail.com');





