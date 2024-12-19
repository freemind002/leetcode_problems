-- Write your PostgreSQL query statement below
select
	pro.project_id,
	ROUND(AVG(emp.experience_years), 2) AS average_years
from
	project pro
	left join employee emp on pro.employee_id = emp.employee_id
group by
	pro.project_id
order by
	pro.project_id ASC