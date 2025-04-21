# Write your MySQL query statement below
select a.customer_id, 
sum(case when a.transaction_id is null then 1 else 0 end) as count_no_trans
from (
select v.customer_id, transaction_id
from Visits as v
left join Transactions as t
on v.visit_id = t.visit_id)a
group by customer_id
having count_no_trans>0