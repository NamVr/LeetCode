# Write your MySQL query statement below
SELECT
transaction_date,
SUM(case when amount%2=1 then amount else 0 end) as odd_sum,
SUM(case when amount%2=0 then amount else 0 end) as even_sum
FROM
Transactions
GROUP BY TRANSACTION_DATE
ORDER BY TRANSACTION_DATE
