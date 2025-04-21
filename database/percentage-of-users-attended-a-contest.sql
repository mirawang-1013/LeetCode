# Write your MySQL query statement below
with total_user as (
    select count(*) as total_cnt
    from users
)
select contest_id, 
round((count(distinct r.user_id)/t.total_cnt)*100,2) as percentage
from register as r, total_user as t
group by contest_id
order by percentage desc, contest_id asc