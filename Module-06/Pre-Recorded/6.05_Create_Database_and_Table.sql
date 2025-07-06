
-- Create Database
CREATE DATABASE ecommerce;



-- Product Table
CREATE TABLE Products(
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );



