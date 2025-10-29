
-- EXPERIMENT NO: 03
-- AIM: Construction of OLAP Operations and Queries

-- =============================
-- SAMPLE DATA
-- =============================

INSERT INTO product VALUES (1, 'Laptop', 'Electronics'), (2, 'Mobile', 'Electronics');
INSERT INTO location VALUES (1, 'New York', 'USA'), (2, 'Dallas', 'USA');
INSERT INTO time VALUES (1, 10, 'March', 'Q1', 2024), (2, 15, 'September', 'Q3', 2024);
INSERT INTO fact_table VALUES (1, 1, 1, 1, 5, 250000), (2, 2, 2, 2, 10, 500000);

-- =============================
-- OLAP OPERATIONS
-- =============================

-- 1. Slice Operation
SELECT  
    l.loc_name, 
    p.name AS product_name, 
    f.total_income 
FROM  
    fact_table f 
JOIN product p ON f.product_id = p.p_id 
JOIN location l ON f.location_id = l.loc_id 
JOIN time t ON f.time_id = t.t_id 
WHERE  
    t.quarter = 'Q3';

-- 2. Roll-Up Operation
SELECT  
    l.country, 
    t.quarter, 
    SUM(f.total_income) AS total_income 
FROM  
    fact_table f 
JOIN location l ON f.location_id = l.loc_id 
JOIN time t ON f.time_id = t.t_id 
GROUP BY  
    l.country, t.quarter;

-- 3. Drill-Down Operation
SELECT  
    l.loc_name, 
    t.month, 
    p.name, 
    SUM(f.units_sold) AS units_sold 
FROM  
    fact_table f 
JOIN location l ON f.location_id = l.loc_id 
JOIN time t ON f.time_id = t.t_id 
JOIN product p ON f.product_id = p.p_id 
WHERE  
    l.country = 'USA' 
GROUP BY  
    l.loc_name, t.month, p.name;
