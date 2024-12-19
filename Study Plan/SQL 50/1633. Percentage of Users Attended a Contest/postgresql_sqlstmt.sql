SELECT
	contest_id,
	ROUND(
		100. * COUNT(DISTINCT user_id) / (
			SELECT
				COUNT(*)
			FROM
				users u
		),
		2
	) percentage
FROM
	Register
GROUP BY
	contest_id
ORDER BY
	percentage DESC,
	contest_id;