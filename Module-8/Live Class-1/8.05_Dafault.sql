-- 35:40


-- DEFAULT
-- Sets a default value for a column if no value is provided during insertion of data
-- doesn't works on UPDATE, only works on Insertion
-- useful for Audit columns





CREATE TABLE Orders(
    Order_ID INT,
    Order_Date DATE DEFAULT CURRENT_DATE,               -- 'Order_Date' will be the system date
    Status VARCHAR(50) DEFAULT 'Pending'                -- 'Status' will be 'Pending'
);


