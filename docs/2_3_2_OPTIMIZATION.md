# Оптимизация БД.

**Минимальный набор индексов:**

```sql
CREATE INDEX idx_orders_status_created_id
    ON orders (status, created_at, id);

CREATE INDEX idx_order_lines_order_id
    ON order_lines (order_id);

CREATE INDEX idx_products_catalog_id
    ON products (catalog_id);

CREATE INDEX idx_catalogs_parent_id
    ON catalogs (parent_id);
```

## Оптимизация схемы данных

1. **Денормализация корневой категории.**  
   Добавить `root_catalog_id` в `products` и поддерживать при изменениях каталога. (Избавляемся от рекурсивного CTE)

2. **Предагрегация продаж.**  
   Таблица `product_sales_daily(product_id, root_catalog_id, day, qty)`.
   Запрос превращается в `SUM(qty)` по небольшой таблице.
