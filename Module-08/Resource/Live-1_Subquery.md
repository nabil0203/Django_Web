# Advanced SQL

## Subquery

---

### **1. Constraints: UNIQUE, DEFAULT, CHECK, FOREIGN KEY**

Constraints enforce data integrity rules in database tables.

1. **UNIQUE**  
   - **Purpose**: Ensures all values in a column (or set of columns) are distinct.  
   - **Usage**:

     ```sql
     CREATE TABLE Employees (
         EmployeeID INT PRIMARY KEY,
         Email VARCHAR(255) UNIQUE,  -- Column-level
     );
     ```  

    ```sql
    CREATE TABLE product_variants (
        product_id INT,
        variant_name VARCHAR(50),
        UNIQUE (product_id, variant_name)  -- Table-level
    );
    ```

   - **Key Points**:  
     - Allows `NULL` values (multiple `NULL`s are allowed in most databases, but check your DBMS).  
     - A table can have multiple `UNIQUE` constraints.  

2. **DEFAULT**  
   - **Purpose**: Sets a default value for a column if no value is provided during insertion.  
   - **Usage**:

     ```sql
     CREATE TABLE Orders (
         OrderID INT PRIMARY KEY,
         OrderDate DATE DEFAULT CURRENT_DATE,  -- System date
         Status VARCHAR(20) DEFAULT 'Pending'
     );
     ```

   - **Key Points**:  
     - Applies only to `INSERT` operations.  
     - Useful for audit columns (e.g., `created_at TIMESTAMP DEFAULT NOW()`).

3. **CHECK**  
   - **Purpose**: Validates that a column's value meets a specified condition.  
   - **Usage**:

     ```sql
     CREATE TABLE Products (
         ProductID INT PRIMARY KEY,
         Price DECIMAL(10,2) CHECK (Price > 0),  -- Column-level
         Quantity INT,
         CHECK (Quantity >= 0)                   -- Table-level
     );
     ```

   - **Key Points**:  
     - Supports complex conditions (e.g., `CHECK (Age >= 18 AND Age <= 65)`).  
     - Rejects invalid data at the database level.

---

### **2. Correlated Subqueries and Common Table Expressions (CTEs)**

1. **Correlated Subqueries**  
   - **Definition**: A subquery that references columns from the outer query. Executed **row-by-row** for each result of the outer query.  
   - **Use Case**: Find employees earning more than their department's average salary.  

    ```sql
    SELECT e1.Name, e1.Salary, e1.DepartmentID
    FROM Employees e1
    WHERE Salary > (
        SELECT AVG(Salary)
        FROM Employees e2
        WHERE e2.DepartmentID = e1.DepartmentID  -- Correlation
    );
    ```
  
   - **Pros**: Flexible for row-specific conditions.  
   - **Cons**: Performance-intensive (executed repeatedly). Use indexes to optimize.

2. **Common Table Expressions (CTEs)**  
   - **Definition**: A **temporary named result set** used within a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement.  
   - **Syntax**:

    ```sql
    WITH CTE_Name AS (
        SELECT ...  -- CTE definition
    )
    SELECT * FROM CTE_Name;  -- Main query
    ```

    For example:

    ```sql
    WITH HighEarners AS (
        SELECT Name, Salary 
        FROM Employees 
        WHERE Salary > 100000
    )
    SELECT * FROM HighEarners;
    ```

---

### **3. Indexes: Types and Performance**

#### What is an Index?

An index is a separate data structure that contains a sorted list of values from one or more columns in a table, along with pointers to the actual rows where those values are found. When you query data, the database engine can use the index to quickly locate the relevant rows instead of scanning the entire table.

#### How Indexes Work

When you create an index on a column, the database builds a structure (commonly a B-tree) that organizes the column values in a way that allows for fast searching. For example, if you have a table with millions of customer records and frequently search by customer ID, an index on the customer_id column would dramatically speed up those queries.

Without an index, the database performs a "table scan" - examining every row sequentially until it finds the matching records. With an index, it can jump directly to the relevant data using the index structure, similar to how you'd use a phone book's alphabetical organization to find a name quickly.

#### Benefits of Indexing

Indexes dramatically improve query performance, especially for SELECT operations with WHERE clauses, JOIN operations, and ORDER BY clauses. They're essential for maintaining referential integrity through foreign key constraints and can speed up aggregate functions like COUNT, SUM, and GROUP BY operations.

#### Drawbacks of Indexing

Indexes consume **additional storage space**, sometimes significantly. They also **slow down INSERT, UPDATE, and DELETE operations** because the database must maintain the index structures alongside the actual data changes. Over-indexing can actually hurt performance and increase maintenance overhead.

#### When to Use Indexes

Create indexes on columns frequently used in WHERE clauses, JOIN conditions, and ORDER BY clauses. Primary keys and foreign keys typically benefit from indexing. Columns with high selectivity (many unique values) generally make better index candidates than columns with few distinct values.

Avoid indexing small tables, columns that change frequently, or columns rarely used in queries. Tables with heavy INSERT/UPDATE activity may suffer from too many indexes.

#### Creating and Managing Indexes

```sql
-- Creating a simple index
CREATE INDEX idx_customer_lastname ON customers(last_name);

-- Creating a composite index
CREATE INDEX idx_order_date_status ON orders(order_date, status);

-- Creating a unique index
CREATE UNIQUE INDEX idx_customer_email ON customers(email);

-- Dropping an index
DROP INDEX idx_customer_lastname;
```
