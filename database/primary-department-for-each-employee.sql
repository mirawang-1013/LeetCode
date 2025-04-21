# Write your MySQL query statement below
with multi as (
select employee_id,
count(distinct department_id) as department_num
from Employee
group by employee_id
)
-- select * from multi
select e.employee_id,
(case when m.department_num=1 then e.department_id
when m.department_num>1 and e.primary_flag = 'Y' then e.department_id
else null end) as department_id
from Employee e 
left join multi m
on e.employee_id = m.employee_id
having department_id is not null