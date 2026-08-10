# Module 5 Schema Diagram

```text
categories
    │ 1
    │
    │ N
products
    │ 1
    │
    │ N
product_prices
```

### categories
- PK `category_id`
- UNIQUE `name`

### products
- PK `product_id`
- FK `category_id`
- UNIQUE `product_url`

### product_prices
- PK `price_id`
- FK `product_id`
- `price_gbp`
- `recorded_at`

MongoDB stores scraped products as flexible documents in the `products`
collection. A unique index on `product_url` provides idempotent upserts.
