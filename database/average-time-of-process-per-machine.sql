# Write your MySQL query statement below
select machine_id, round(sum(processing_time)/count(distinct process_id),3) as processing_time
from (
select a.machine_id, a.process_id,
(b.timestamp-a.timestamp) as processing_time
from 
activity a 
join activity b
on a.machine_id = b.machine_id and a.process_id = b.process_id and 
a.activity_type = 'start' and b.activity_type = 'end')a
group by machine_id