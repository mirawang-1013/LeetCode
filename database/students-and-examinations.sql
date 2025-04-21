# Write your MySQL query statement below
select s.student_id, s.student_name,sub.subject_name,sum(CASE 
        WHEN e.student_id IS NOT NULL THEN 1
        ELSE 0
    END)AS attended_exams 
from Students as s 
cross join Subjects as sub
left join Examinations as e 
on s.student_id = e.student_id and sub.subject_name = e.subject_name
group by s.student_id, s.student_name,sub.subject_name
order by s.student_id, sub.subject_name;
