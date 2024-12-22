import polars as pl

data = [
    [1, 3, 5, "2019-08-01"],
    [1, 3, 6, "2019-08-02"],
    [2, 7, 7, "2019-08-01"],
    [2, 7, 6, "2019-08-02"],
    [4, 7, 1, "2019-07-22"],
    [3, 4, 4, "2019-07-21"],
    [3, 4, 4, "2019-07-21"],
]
schema = ["article_id", "author_id", "viewer_id", "view_date"]
lf = pl.LazyFrame(data, schema, orient="row").cast(
    {
        "article_id": pl.Int64,
        "author_id": pl.Int64,
        "viewer_id": pl.Int64,
        "view_date": pl.Date,
    }
)


def article_views(views: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        views.filter(pl.col("author_id") == pl.col("viewer_id"))
        .select(pl.col("author_id").alias("id"))
        .unique()
        .sort("id")
        .collect()
    )

    return result_df


result = article_views(lf)
print(result)
