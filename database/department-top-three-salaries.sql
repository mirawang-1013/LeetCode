# Write your MySQL query statement below
select Department, Employee,Salary
from (
SELECT d.name as Department,
e.name as Employee, e.salary as Salary,
dense_rank() over(partition by e.departmentId order by e.salary DESC) as rnk
from Employee e join Department d
on d.id = e.departmentId
) a
where rnk<=3