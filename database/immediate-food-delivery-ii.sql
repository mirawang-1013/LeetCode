# Write your MySQL query statement below
with first_order as(
    select 
    delivery_id, 
    order_date, 
    customer_id, 
    customer_pref_delivery_date,
    row_number() over(partition by customer_id order by order_date) as rn
from Delivery
)

select round(sum(if(order_date = customer_pref_delivery_date, 1, 0))/count( *),4)*100 as immediate_percentage
from 
first_order
where rn=1

