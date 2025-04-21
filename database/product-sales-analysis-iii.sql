# Write your MySQL query statement below
-- WITH ranked_sales AS 
-- (select a.product_id, 
-- row_number() over (partition by a.product_id order by a.year asc) as rn,
-- a.year,
--  (a.quantity) as quantity , (a.price) as price
-- from Sales a)


-- select product_id, year as first_year, quantity, price
-- from ranked_sales 
-- where rn =1
-- WITH ranked_sales AS (
--     SELECT product_id,
--            year,
--            quantity,
--            price,
--            ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY year ASC) AS rn
--     FROM Sales
-- )
-- SELECT product_id,
--        year AS first_year,
--        quantity,
--        price
-- FROM ranked_sales
-- WHERE rn = 1;

-- SELECT product_id, year as first_year, quantity,price
-- FROM Sales
-- WHERE (product_id,year) in (
-- SELECT product_id,MIN(year)
-- FROM Sales
-- GROUP BY product_id
-- )

WITH ranked_sales AS (
    SELECT product_id,
           year,
           quantity,
           price,
           RANK() OVER (PARTITION BY product_id ORDER BY year ASC) AS rnk
    FROM Sales
)
SELECT product_id,
       year AS first_year,
       quantity,
       price
FROM ranked_sales
WHERE rnk = 1;

