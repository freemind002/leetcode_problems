WITH
	cum_sum AS (
		SELECT
			person_name,
			SUM(weight) OVER (
				ORDER BY
					turn asc
			) AS total_weight
		FROM
			Queue
	)
SELECT
	person_name
FROM
	cum_sum
WHERE
	total_weight <= 1000
ORDER BY
	total_weight DESC
LIMIT
	1