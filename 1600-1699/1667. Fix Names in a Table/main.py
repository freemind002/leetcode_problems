import polars as pl

data = [[1, "aLice"], [2, "bOB"]]
users = pl.LazyFrame(data, schema=["user_id", "name"], orient="row").cast(
    {"user_id": pl.Int64, "name": pl.String}
)


def fix_names(users: pl.LazyFrame) -> pl.DataFrame:
    result_df = users.with_columns(pl.col("name").str.to_titlecase()).collect()

    return result_df


result = fix_names(users)
print(result)
