SELECT
	product_name,
	year,
	price
FROM
	Sales
	INNER JOIN Product USING (product_id);