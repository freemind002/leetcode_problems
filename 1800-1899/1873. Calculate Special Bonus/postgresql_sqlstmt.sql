select
	employee_id,
	case
		when substring(name, 1, 1) <> 'M'
		and mod(employee_id, 2) <> 0 then salary
		else 0
	end as bonus
from
	Employees
order by
	employee_id;