from datetime import date

import polars as pl

data = [[1, "Avengers"], [2, "Frozen 2"], [3, "Joker"]]
movies = pl.LazyFrame(data, schema=["movie_id", "title"], orient="row").cast(
    {"movie_id": pl.Int64, "title": pl.String}
)
data = [[1, "Daniel"], [2, "Monica"], [3, "Maria"], [4, "James"]]
users = pl.LazyFrame(data, schema=["user_id", "name"], orient="row").cast(
    {"user_id": pl.Int64, "name": pl.String}
)
data = [
    [1, 1, 3, "2020-01-12"],
    [1, 2, 4, "2020-02-11"],
    [1, 3, 2, "2020-02-12"],
    [1, 4, 1, "2020-01-01"],
    [2, 1, 5, "2020-02-17"],
    [2, 2, 2, "2020-02-01"],
    [2, 3, 2, "2020-03-01"],
    [3, 1, 3, "2020-02-22"],
    [3, 2, 4, "2020-02-25"],
]
movie_rating = pl.LazyFrame(
    data, schema=["movie_id", "user_id", "rating", "created_at"], orient="row"
).cast(
    {
        "movie_id": pl.Int64,
        "user_id": pl.Int64,
        "rating": pl.Int64,
        "created_at": pl.Date,
    }
)


def movie_rating_fun(
    movies: pl.LazyFrame, users: pl.LazyFrame, movie_rating: pl.LazyFrame
) -> pl.DataFrame:
    result_df = pl.concat(
        [
            (
                movie_rating.join(users, on="user_id")
                .group_by("name")
                .len()
                .sort(["len", "name"], descending=[True, False])
                .head(1)
                .select(result=pl.col("name"))
            ),
            (
                movies.join(movie_rating, on="movie_id")
                .filter(
                    pl.col("created_at").is_between(date(2020, 2, 1), date(2020, 2, 28))
                )
                .group_by("title")
                .agg(pl.col("rating").mean())
                .sort(["rating", "title"], descending=[True, False])
                .head(1)
                .select(result=pl.col("title"))
            ),
        ]
    ).collect()

    return result_df


result = movie_rating_fun(movies, users, movie_rating)
print(result)
