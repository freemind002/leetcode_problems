WITH
	temp AS (
		SELECT
			e1.id,
			e1.name
		FROM
			Employee e1
			JOIN Employee e2 ON e1.id = e2.managerId
		GROUP BY
			e1.name,
			e1.id
		HAVING
			COUNT(e1.id) >= 5
	)
SELECT
	name
FROM
	temp