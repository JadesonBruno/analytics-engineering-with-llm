/* Lab 5 - Analytics Engineering - Python, SQL e LLM
for Extracting Insights in Data Engineering Pipelines */
-- SQL - Creation of the Database Schema and Tables

-- Drop the schema if it exists
DROP SCHEMA IF EXISTS analytics_engineering CASCADE;

-- Create the schema
CREATE SCHEMA analytics_engineering AUTHORIZATION postgres;

-- Create the tables
CREATE TABLE analytics_engineering.customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(101),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE analytics_engineering.products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE analytics_engineering.purchases (
    purchase_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES analytics_engineering.customers(customer_id),
    product_id INTEGER REFERENCES analytics_engineering.products(product_id),
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
