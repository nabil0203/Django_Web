-- 1:25:00


-- Foreign Key
-- When 1 table is connected to another table
-- 



CREATE TABLE Person (
    User_ID INT PRIMARY KEY,
    First_Name VARCHAR(255),
    Last_Name VARCHAR(255)
);



CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Order_Number INT,
    Person_ID INT,
    FOREIGN KEY (Person_ID) REFERENCES Person(User_ID)                          --'User_ID' of Person table is a 'Foreign Key' in Orders Table which references Person_ID
);


