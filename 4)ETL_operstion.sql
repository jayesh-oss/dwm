
-- EXPERIMENT NO: 04
-- AIM: Implementation of OLAP Operations - Slice, Dice, Roll Up, and Drill Down

-- Step 1: Create 'sales' table
CREATE TABLE sales (
  product_id INT,
  store_id INT,
  sales_amount INT,
  sales_date DATE
);

-- Step 2: Insert sample data
INSERT INTO sales (product_id, store_id, sales_amount, sales_date) VALUES
(101, 1, 150, '2024-01-10'),
(102, 1, 200, '2024-01-15'),
(101, 2, 100, '2024-02-10'),
(103, 1, 250, '2024-03-05'),
(101, 3, 300, '2024-04-20'),
(102, 2, 400, '2024-05-10'),
(103, 3, 500, '2024-06-25'),
(101, 1, 350, '2024-07-15');

-- Step 3: Display all data
SELECT * FROM sales;

-- Step 4: Slice Operation - Filter data for a specific product
SELECT * FROM sales WHERE product_id = 101;

-- Step 5: Dice Operation - Filter data on multiple dimensions
SELECT * FROM sales WHERE product_id = 101 AND store_id = 1;

-- Step 6: Roll-Up Operation - Aggregate total sales by store
SELECT store_id, SUM(sales_amount) AS total_sales
FROM sales
GROUP BY store_id;

-- Step 7: Roll-Up Operation - Aggregate total sales by product
SELECT product_id, SUM(sales_amount) AS total_sales
FROM sales
GROUP BY product_id;

-- Step 8: Drill-Down Operation - From summary to detailed data
-- Summary view (total sales per store)
SELECT store_id, SUM(sales_amount) AS total_sales
FROM sales
GROUP BY store_id;

-- Detailed view (sales details for store 1)
SELECT * FROM sales WHERE store_id = 1;
