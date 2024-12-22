-- Write your PostgreSQL query statement below
SELECT
	e1.employee_id as employee_id,
	e1.name as name,
	COUNT(e2.reports_to) as reports_count,
	ROUND(AVG(e2.age)) as average_age
FROM
	Employees e1
	JOIN Employees e2 ON e1.employee_id = e2.reports_to
GROUP BY
	e1.employee_id,
	e1.name
ORDER BY
	employee_id