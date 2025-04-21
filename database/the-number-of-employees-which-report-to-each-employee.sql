# Write your MySQL query statement below
with report as (select reports_to, count(reports_to) as reports_count,round(avg(age),0) as average_age
from Employees
group by reports_to
)

-- select * from report
select employee_id, name, r.reports_count, r.average_age
from Employees e
left join report r
on e.employee_id = r.reports_to
where reports_count is not null
order by employee_id
