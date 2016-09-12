# Write your MySQL query statement below
# https://discuss.leetcode.com/topic/15672/solution-in-a-single-query-without-any-conflicts
SELECT DISTINCT a.Num as ConsecutiveNums
FROM Logs a, Logs b, Logs c WHERE a.Id = b.Id - 1 and b.Id = c.Id - 1 and a.Num = b.Num and b.Num = c.Num 
