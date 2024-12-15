select
	v.customer_id,
	count(v.customer_id) as count_no_trans
from
	visits v
where
	not exists (
		select
			t.visit_id
		from
			transactions t
		where
			t.visit_id = v.visit_id
	)
group by
	v.customer_id