select
	max(num) num
from
	(
		select
			num
		from
			MyNumbers
		group by
			num
		having
			count(*) = 1
	);