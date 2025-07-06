-- 30:45



-- make multiple column UNIQUE at the same time
CREATE TABLE product_variant(
    product_id INT,
    variant_name VARCHAR(50),
    UNIQUE (product_id, variant_name)                                       -- multiple col
)


