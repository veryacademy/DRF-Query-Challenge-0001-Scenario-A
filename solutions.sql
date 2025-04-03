-- ******************************************************************
-- Solution: Fetch all active products from the 'products' table.
-- ******************************************************************

-- Basic Query (Without Aliases)
SELECT 
    id,         -- Selects the Product ID
    name,       -- Selects the Product Name
    price,      -- Selects the Product Price
    is_active,  -- Selects the is_active status (to check if the product is active)
    created_at  -- Selects the created_at timestamp for ordering
FROM products   -- Fetch data from the 'products' table
WHERE is_active = true  -- Filters only active products (where is_active is TRUE)
ORDER BY created_at DESC;  -- Orders the results by 'created_at' in descending order (newest first)

-- ******************************************************************
-- Solution: Query with Aliases for Better Readability
-- ******************************************************************

SELECT 
    id AS "Product ID",          -- Renames 'id' to "Product ID" for clarity
    name AS "Product Name",      -- Renames 'name' to "Product Name"
    price AS "Product Price",    -- Renames 'price' to "Product Price"
    is_active AS "Product is_active"  -- Renames 'is_active' to "Product is_active"
FROM products    -- Fetch data from the 'products' table
WHERE is_active = true  -- Filters only active products (where is_active is TRUE)
ORDER BY created_at DESC;  -- Orders the results by 'created_at' in descending order (newest first)

-- ******************************************************************
-- Notes:
-- 1. PostgreSQL allows boolean values as 'true' or 'false' (case-insensitive).
-- 2. Using ORDER BY created_at DESC ensures the newest products appear first.
-- 3. Aliases (AS) improve readability, especially in reports or API responses.
-- ******************************************************************
