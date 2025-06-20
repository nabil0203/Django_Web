-- 39:50


-- CHECK
-- Validates that the column value meets a specific condition
-- Supports complex condition (AND)
-- Rejects invalid data
-- same to 'if' condition






CREATE Table Product(
    Price INT CHECK (Price > 0),                -- Price can't be zero
    Quantity INT,
    CHECK (Quantity >= 0)                       -- 'Quantity' can't be less than 0; if puts less than 0 while inserting, database will show an error
)


