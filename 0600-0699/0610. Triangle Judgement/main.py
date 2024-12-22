import polars as pl

data = [[13, 15, 30], [10, 20, 15]]
triangle = pl.LazyFrame(data, schema=["x", "y", "z"], orient="row").cast(
    {"x": pl.Int64, "y": pl.Int64, "z": pl.Int64}
)


def triangle_judgement(triangle: pl.LazyFrame) -> pl.DataFrame:
    result_df = triangle.with_columns(
        pl.when(
            (pl.sum_horizontal(pl.all()) - pl.max_horizontal(pl.all()))
            > pl.max_horizontal(pl.all())
        )
        .then(pl.lit("Yes"))
        .otherwise(pl.lit("No"))
        .alias("triangle")
    ).collect()

    return result_df


result = triangle_judgement(triangle)
print(result)
