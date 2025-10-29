
-- EXPERIMENT NO: 01
-- AIM: Data Warehouse Construction by Using a Real-Life Problem

-- =============================
-- STEP 1: CREATE DIMENSION TABLES
-- =============================

CREATE TABLE customer (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(50),
  gender VARCHAR(10),
  age INT
);

CREATE TABLE product (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(50),
  category VARCHAR(50),
  price DECIMAL(10,2)
);

CREATE TABLE location (
  location_id INT PRIMARY KEY,
  city VARCHAR(50),
  state VARCHAR(50),
  country VARCHAR(50)
);

CREATE TABLE time (
  time_id INT PRIMARY KEY,
  day INT,
  month VARCHAR(20),
  quarter VARCHAR(10),
  year INT
);

-- =============================
-- STEP 2: CREATE FACT TABLE
-- =============================

CREATE TABLE sales_fact (
  sale_id INT PRIMARY KEY,
  customer_id INT,
  product_id INT,
  location_id INT,
  time_id INT,
  sales_amount DECIMAL(10,2),
  quantity_sold INT,
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
  FOREIGN KEY (product_id) REFERENCES product(product_id),
  FOREIGN KEY (location_id) REFERENCES location(location_id),
  FOREIGN KEY (time_id) REFERENCES time(time_id)
);

-- =============================
-- STEP 3: INSERT SAMPLE DATA
-- =============================

INSERT INTO customer VALUES 
(1, 'Alice', 'Female', 28),
(2, 'Bob', 'Male', 35),
(3, 'Charlie', 'Male', 30);

INSERT INTO product VALUES 
(101, 'Laptop', 'Electronics', 75000),
(102, 'Mobile', 'Electronics', 25000),
(103, 'Chair', 'Furniture', 3000);

INSERT INTO location VALUES 
(201, 'Mumbai', 'Maharashtra', 'India'),
(202, 'Delhi', 'Delhi', 'India'),
(203, 'Pune', 'Maharashtra', 'India');

INSERT INTO time VALUES 
(301, 10, 'January', 'Q1', 2024),
(302, 15, 'March', 'Q1', 2024),
(303, 25, 'April', 'Q2', 2024);

INSERT INTO sales_fact VALUES 
(401, 1, 101, 201, 301, 75000, 1),
(402, 2, 102, 202, 302, 50000, 2),
(403, 3, 103, 203, 303, 9000, 3);

-- =============================
-- STEP 4: SAMPLE OLAP QUERIES
-- =============================

-- 1. Total Sales per City
SELECT l.city, SUM(s.sales_amount) AS total_sales
FROM sales_fact s
JOIN location l ON s.location_id = l.location_id
GROUP BY l.city;

-- 2. Sales by Product Category
SELECT p.category, SUM(s.sales_amount) AS total_sales
FROM sales_fact s
JOIN product p ON s.product_id = p.product_id
GROUP BY p.category;

-- 3. Yearly Sales Trend
SELECT t.year, SUM(s.sales_amount) AS total_sales
FROM sales_fact s
JOIN time t ON s.time_id = t.time_id
GROUP BY t.year;
