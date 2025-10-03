# Write your MySQL query statement below

# delivery_id is the primary key
# first order = earliest order date.
# immediate = same order and delivery date
# scheduled = otherwise

# return the percentage of immediate orders for first orders only , ROUND (2)
# % means * 100. ROUND (VALUE * 100, 2)

SELECT
    ROUND(
        SUM(
            order_date = customer_pref_delivery_date -- This will evaluate to 0 or 1
        ) / COUNT(
            DISTINCT customer_id
        ) * 100, 2
    ) AS immediate_percentage
FROM
    Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
);
