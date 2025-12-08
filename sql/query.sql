/* Lab 5 - Analytics Engineering - Python, SQL and LLM
for Extracting Insights in Data Engineering Pipelines */
-- SQL - Query to get the total purchase per customer
SELECT
    c.name,
    COUNT(p.purchase_id) AS total_purchases,
    SUM(pr.price) AS total_spent
FROM
    analytics_engineering.customers c
JOIN
    analytics_engineering.purchases p ON c.customer_id = p.customer_id
JOIN
    analytics_engineering.products pr ON p.product_id = pr.product_id
GROUP BY
    c.name;
