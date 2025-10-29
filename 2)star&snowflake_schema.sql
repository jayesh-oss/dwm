
-- EXPERIMENT NO: 02
-- AIM: Construction of Star Schema and Snowflake Schema

-- =============================
-- STAR SCHEMA
-- =============================

CREATE TABLE product (
  p_id INT PRIMARY KEY,
  name VARCHAR(50),
  category VARCHAR(50)
);

CREATE TABLE location (
  loc_id INT PRIMARY KEY,
  loc_name VARCHAR(50),
  country VARCHAR(50)
);

CREATE TABLE time (
  t_id INT PRIMARY KEY,
  day INT,
  month VARCHAR(20),
  quarter VARCHAR(10),
  year INT
);

CREATE TABLE fact_table (
  fact_id INT PRIMARY KEY,
  product_id INT,
  location_id INT,
  time_id INT,
  units_sold INT,
  total_income DECIMAL(10,2),
  FOREIGN KEY (product_id) REFERENCES product(p_id),
  FOREIGN KEY (location_id) REFERENCES location(loc_id),
  FOREIGN KEY (time_id) REFERENCES time(t_id)
);

-- =============================
-- SNOWFLAKE SCHEMA
-- =============================

CREATE TABLE country (
  country_id INT PRIMARY KEY,
  country_name VARCHAR(50)
);

CREATE TABLE location_sf (
  loc_id INT PRIMARY KEY,
  loc_name VARCHAR(50),
  country_id INT,
  FOREIGN KEY (country_id) REFERENCES country(country_id)
);

CREATE TABLE category (
  category_id INT PRIMARY KEY,
  category_name VARCHAR(50)
);

CREATE TABLE product_sf (
  p_id INT PRIMARY KEY,
  name VARCHAR(50),
  category_id INT,
  FOREIGN KEY (category_id) REFERENCES category(category_id)
);

CREATE TABLE time_sf (
  t_id INT PRIMARY KEY,
  day INT,
  month VARCHAR(20),
  quarter VARCHAR(10),
  year INT
);

CREATE TABLE fact_sf (
  fact_id INT PRIMARY KEY,
  product_id INT,
  location_id INT,
  time_id INT,
  units_sold INT,
  total_income DECIMAL(10,2),
  FOREIGN KEY (product_id) REFERENCES product_sf(p_id),
  FOREIGN KEY (location_id) REFERENCES location_sf(loc_id),
  FOREIGN KEY (time_id) REFERENCES time_sf(t_id)
);
