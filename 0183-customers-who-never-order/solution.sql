# Write your MySQL query statement below
SELECT
    NAME AS Customers
FROM
    Customers
WHERE
    ID NOT IN (
        SELECT customerId
        FROM Orders
    );
