import polars as pl

data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
logs = pl.LazyFrame(data, schema={"id": pl.Int64, "num": pl.Int64}, orient="row")


def consecutive_numbers(logs: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        logs.with_row_index()
        .rolling("index", period="3i")
        .agg(pl.col("num").alias("ConsecutiveNums"))
        .filter(
            pl.col("ConsecutiveNums").list.len() == 3,
            pl.col("ConsecutiveNums").list.n_unique() == 1,
        )
        .select(pl.col("ConsecutiveNums").count())
        .collect()
    )

    return result_df


result = consecutive_numbers(logs)
print(result)
