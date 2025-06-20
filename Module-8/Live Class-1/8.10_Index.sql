-- 1:17:40



-- Creating and Managing Indexes





-- Creating a simple index
CREATE INDEX idx_customer_lastname ON customers(last_name);

-- Creating a composite index
CREATE INDEX idx_order_date_status ON orders(order_date, status);

-- Creating a unique index
CREATE UNIQUE INDEX idx_customer_email ON customers(email);

-- Dropping an index
DROP INDEX idx_customer_lastname;



