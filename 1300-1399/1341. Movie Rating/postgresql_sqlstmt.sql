(
	select
		u.name as results
	from
		MovieRating m
		join users u on u.user_id = m.user_id
	group by
		u.name
	order by
		count(u.name) desc,
		u.name
	limit
		1
)
union all
(
	select
		m.title as results
	from
		movies m
		join movierating mr on m.movie_id = mr.movie_id
	where
		mr.created_at >= '2020-02-01'
		and mr.created_at <= '2020-02-28'
	group by
		m.title
	order by
		avg(mr.rating) desc,
		m.title
	limit
		1
)