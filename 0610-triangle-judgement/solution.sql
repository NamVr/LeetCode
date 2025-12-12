# Write your MySQL query statement below
# check all combinations of 3 line segments

SELECT *, IF (
    x + y > z and y + z > x and z + x > y, "Yes", "No"
) as triangle FROM Triangle;
