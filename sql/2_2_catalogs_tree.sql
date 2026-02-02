SELECT
    c.name AS category_name,
    COUNT(ch.id) AS children_count
FROM catalogs AS c
LEFT JOIN catalogs AS ch
    ON ch.parent_id = c.id
GROUP BY
    c.id,
    c.name
ORDER BY
    c.name;
