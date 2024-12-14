import polars as pl

data = [
    [1, "Will", None],
    [2, "Jane", None],
    [3, "Alex", 2],
    [4, "Bill", None],
    [5, "Zack", 1],
    [6, "Mark", 2],
]
schema = ["id", "name", "referee_id"]
lf = pl.LazyFrame(data, schema, orient="row").cast(
    {"id": pl.Int64, "name": pl.String, "referee_id": pl.Int64}
)


def find_customer_referee(customer: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        customer.with_columns(pl.col("referee_id").fill_null(strategy="zero"))
        .filter(pl.col("referee_id") != 2)
        .select("name")
        .collect()
    )

    return result_df


result = find_customer_referee(lf)
print(result)
