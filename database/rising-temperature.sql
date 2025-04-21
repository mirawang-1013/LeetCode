# Write your MySQL query statement below
select Weather1.id
from Weather as Weather1,Weather as Weather2
where dateDiff(Weather1.recordDate, Weather2.recordDate)=1
and Weather1.Temperature > Weather2.Temperature