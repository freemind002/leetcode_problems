(
	SELECT DISTINCT
		ON (product_id) product_id,
		new_price as price
	FROM
		Products
	WHERE
		change_date <= '2019-08-16'
	ORDER BY
		product_id,
		change_date DESC
)
UNION ALL
SELECT
	product_id,
	10 AS price
FROM
	Products
GROUP BY
	product_id
HAVING
	min(change_date) > '2019-08-16'