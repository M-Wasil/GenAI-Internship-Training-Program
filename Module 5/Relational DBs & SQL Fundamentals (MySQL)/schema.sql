DROP DATABASE IF EXISTS module5_shop;
CREATE DATABASE module5_shop;
USE module5_shop;

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    product_url VARCHAR(500) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE product_prices (
    price_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    price_gbp DECIMAL(10,2) NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    CHECK (price_gbp >= 0)
);

INSERT INTO categories (name) VALUES
('Fiction'), ('Non-Fiction'), ('Science'), ('Technology');

INSERT INTO products (category_id, title, description, product_url) VALUES
(1, 'Example Fiction Book', 'Sample fiction product.', 'https://example.com/fiction-1'),
(2, 'Example Non-Fiction Book', 'Sample non-fiction product.', 'https://example.com/nonfiction-1'),
(3, 'Example Science Book', 'Sample science product.', 'https://example.com/science-1'),
(4, 'Example Technology Book', 'Sample technology product.', 'https://example.com/technology-1');

INSERT INTO product_prices (product_id, price_gbp) VALUES
(1, 25.99), (2, 18.50), (3, 31.75), (4, 42.00);

SELECT * FROM products;
SELECT p.title, pp.price_gbp
FROM products p
JOIN product_prices pp ON pp.product_id = p.product_id
WHERE pp.price_gbp > 20
ORDER BY pp.price_gbp DESC
LIMIT 10;

UPDATE products
SET description = 'Updated sample description.'
WHERE product_id = 1;

DELETE FROM product_prices WHERE price_id = 4;
