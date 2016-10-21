# Write your MySQL query statement below
# https://discuss.leetcode.com/category/184/second-highest-salary
SELECT max(Salary) as SecondHighestSalary FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee);
