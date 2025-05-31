
-- Shows the whole product table
SELECT * FROM products


-- Shows ONLY the name and stock columns of the product table
SELECT name, stock FROM products


-- Shows ONLY the name and stock of the products that has a Bigger price than 50000
SELECT name, stock FROM products WHERE price > 50000


-- Shows ONLY the name products that has stock lower than 20
SELECT name FROM products WHERE stock < 20


-- Shows ONLY the name products that has stock lower than 20 and Price Higher than 50000
SELECT name FROM products WHERE stock < 20 AND price > 50000
