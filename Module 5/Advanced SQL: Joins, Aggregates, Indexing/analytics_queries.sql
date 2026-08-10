USE module5_shop;

SELECT p.product_id, p.title, c.name AS category, pp.price_gbp
FROM products p
INNER JOIN categories c ON c.category_id = p.category_id
INNER JOIN product_prices pp ON pp.product_id = p.product_id;

SELECT c.name AS category, p.title
FROM categories c
LEFT JOIN products p ON p.category_id = c.category_id
ORDER BY c.name, p.title;

SELECT c.name AS category,
       COUNT(p.product_id) AS product_count,
       ROUND(AVG(pp.price_gbp), 2) AS avg_price,
       ROUND(MIN(pp.price_gbp), 2) AS min_price,
       ROUND(MAX(pp.price_gbp), 2) AS max_price
FROM categories c
LEFT JOIN products p ON p.category_id = c.category_id
LEFT JOIN product_prices pp ON pp.product_id = p.product_id
GROUP BY c.category_id, c.name
ORDER BY avg_price DESC;

SELECT c.name AS category, AVG(pp.price_gbp) AS avg_price
FROM categories c
JOIN products p ON p.category_id = c.category_id
JOIN product_prices pp ON pp.product_id = p.product_id
GROUP BY c.category_id, c.name
HAVING AVG(pp.price_gbp) > 20;

SELECT title
FROM products
WHERE product_id IN (
    SELECT product_id
    FROM product_prices
    WHERE price_gbp > (SELECT AVG(price_gbp) FROM product_prices)
);

WITH category_stats AS (
    SELECT c.category_id, c.name,
           COUNT(p.product_id) AS product_count,
           AVG(pp.price_gbp) AS avg_price
    FROM categories c
    LEFT JOIN products p ON p.category_id = c.category_id
    LEFT JOIN product_prices pp ON pp.product_id = p.product_id
    GROUP BY c.category_id, c.name
)
SELECT *
FROM category_stats
WHERE product_count > 0
ORDER BY avg_price DESC;

SELECT p.title, c.name AS category, pp.price_gbp,
       RANK() OVER (
           PARTITION BY c.category_id
           ORDER BY pp.price_gbp DESC
       ) AS category_price_rank
FROM products p
JOIN categories c ON c.category_id = p.category_id
JOIN product_prices pp ON pp.product_id = p.product_id;

CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_product_prices_product ON product_prices(product_id);
CREATE INDEX idx_product_prices_price ON product_prices(price_gbp);

EXPLAIN SELECT p.title, pp.price_gbp
FROM products p
JOIN product_prices pp ON pp.product_id = p.product_id
WHERE pp.price_gbp > 20;

START TRANSACTION;
UPDATE product_prices SET price_gbp = price_gbp + 1 WHERE product_id = 1;
COMMIT;
