# Write your MySQL query statement below
with count as (
    select class, count(student) as num
    from Courses
    group by class
)

select class
from count
where num>4