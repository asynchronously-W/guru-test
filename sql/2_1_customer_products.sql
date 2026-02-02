SELECT
    c.name AS customer_name,
    SUM(ol.quantity) AS total_quantity
FROM customers AS c
JOIN orders AS o
    ON o.customer_id = c.id
JOIN order_lines AS ol
    ON ol.order_id = o.id
WHERE o.status = 'PLACED'
GROUP BY
    c.id,
    c.name
ORDER BY
    total_quantity DESC;
