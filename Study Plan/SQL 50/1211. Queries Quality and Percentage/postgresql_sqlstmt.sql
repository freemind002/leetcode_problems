select
	query_name,
	ROUND(AVG(cast(rating as decimal) / position), 2) quality,
	coalesce(
		round(
			sum(
				case
					when cast(rating as decimal) < 3 then 1
				end
			) * 100.0 / count(query_name),
			2
		),
		0
	) poor_query_percentage
from
	Queries
GROUP BY
	1
having
	count(query_name) > 0
order by
	2 desc