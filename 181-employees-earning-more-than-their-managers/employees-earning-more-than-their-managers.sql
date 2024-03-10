# Write your MySQL query statement below
SELECT emp1.name as Employee from Employee emp1 JOIN Employee emp2 where emp1.managerid = emp2.id and emp1.salary>emp2.salary;