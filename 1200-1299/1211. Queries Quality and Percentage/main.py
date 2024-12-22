import polars as pl

data = [
    ["Dog", "Golden Retriever", 1, 5],
    ["Dog", "German Shepherd", 2, 5],
    ["Dog", "Mule", 200, 1],
    ["Cat", "Shirazi", 5, 2],
    ["Cat", "Siamese", 3, 3],
    ["Cat", "Sphynx", 7, 4],
]
queries = pl.LazyFrame(
    data, schema=["query_name", "result", "position", "rating"], orient="row"
).cast(
    {
        "query_name": pl.String,
        "result": pl.String,
        "position": pl.Int64,
        "rating": pl.Int64,
    }
)


def queries_stats(queries: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        queries.group_by("query_name")
        .agg(
            (pl.col("rating") / pl.col("position")).mean().round(2).alias("rating"),
            ((pl.col("rating") < 3).mean() * 100)
            .round(2)
            .alias("poor_query_percentage"),
        )
        .collect()
    )

    return result_df


result = queries_stats(queries)
print(result)
