# Write your MySQL query statement below


with first as (
select player_id, device_id, min(event_date) as min_date, games_played
from Activity group by player_id )

select round(
sum(case when date_add(first.min_date, interval 1 day) = a.event_date then 1 else 0 end)/
count(distinct a.player_id) 
,2
)as fraction
from Activity a 
left join first
on a.player_id = first.player_id

