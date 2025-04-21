# Write your MySQL query statement below
with count as (select num, count(num) as times
from MyNumbers group by num
)

select max(num) as num from count
where times=1