WITH RECURSIVE catalog_tree AS (
    SELECT
        c.id,
        c.parent_id,
        c.name AS root_name
    FROM catalogs AS c
    WHERE c.parent_id IS NULL

    UNION ALL

    SELECT
        c.id,
        c.parent_id,
        ct.root_name
    FROM catalogs AS c
    JOIN catalog_tree AS ct
      ON c.parent_id = ct.id
),
last_month_orders AS (
    SELECT o.id
    FROM orders AS o
    WHERE o.status = 'PLACED'
      AND o.created_at >= date_trunc('month', now()) - interval '1 month'
      AND o.created_at <  date_trunc('month', now())
)
SELECT
    p.name AS product_name,
    ct.root_name AS category,
    SUM(ol.quantity) AS total_sales
FROM order_lines AS ol
JOIN last_month_orders AS lmo
  ON ol.order_id = lmo.id
JOIN products AS p
  ON ol.product_id = p.id
LEFT JOIN catalog_tree AS ct
  ON p.catalog_id = ct.id
GROUP BY
    p.id, p.name, ct.root_name
ORDER BY total_sales DESC
LIMIT 5;