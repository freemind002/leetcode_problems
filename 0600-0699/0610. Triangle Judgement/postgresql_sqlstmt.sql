SELECT
	*,
	CASE
		WHEN ((x + y + z) - GREATEST (x, y, z)) > GREATEST (x, y, z) THEN 'Yes'
		ELSE 'No'
	END AS triangle
FROM
	Triangle;