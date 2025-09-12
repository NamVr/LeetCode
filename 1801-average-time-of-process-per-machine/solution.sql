/* Write your T-SQL query statement below */
SELECT A.machine_id, round(avg(B.timestamp - A.timestamp), 3) as processing_time
FROM Activity as A
JOIN
Activity as B
ON
A.machine_id = B.machine_id AND A.process_id = B.process_id
AND A.activity_type = 'start' AND B.activity_type = 'end'
GROUP BY A.machine_id;

