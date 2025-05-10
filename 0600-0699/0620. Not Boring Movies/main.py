import polars as pl

data = [
    [1, "War", "great 3D", 8.9],
    [2, "Science", "fiction", 8.5],
    [3, "irish", "boring", 6.2],
    [4, "Ice song", "Fantacy", 8.6],
    [5, "House card", "Interesting", 9.1],
]
cinema = pl.LazyFrame(
    data,
    schema={
        "id": pl.Int64,
        "movie": pl.String,
        "description": pl.String,
        "rating": pl.Float64,
    },
    orient="row",
)


def not_boring_movies(cinema: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        cinema.filter(pl.col("id") % 2 == 1, pl.col("description") != "boring")
        .sort("rating", descending=True)
        .collect()
    )

    return result_df


result = not_boring_movies(cinema)
print(result)
