SELECT
	to_char (trans_date, 'yyyy-mm') as month,
	country,
	COUNT(amount) as trans_count,
	COUNT(
		CASE
			WHEN state = 'approved' then id
			else null
		end
	) as approved_count,
	SUM(amount) as trans_total_amount,
	SUM(
		CASE
			WHEN state = 'approved' then amount
			else 0
		end
	) as approved_total_amount
FROM
	Transactions
GROUP BY
	month,
	country