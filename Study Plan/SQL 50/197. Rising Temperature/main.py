import polars as pl

data = [
    [1, "2015-01-01", 10],
    [2, "2015-01-02", 25],
    [3, "2015-01-03", 20],
    [4, "2015-01-04", 30],
]
weather = (
    pl.LazyFrame(data, schema=["id", "recordDate", "temperature"], orient="row")
    .cast({"id": pl.Int64, "recordDate": pl.String, "temperature": pl.Int64})
    .with_columns(pl.col("recordDate").str.to_date())
)


def rising_temperature(weather: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        weather.sort("recordDate")
        .filter(
            pl.col("temperature").diff() > 0,
            pl.col("recordDate").diff().dt.total_days() == 1,
        )
        .select("id")
        .collect()
    )

    return result_df


result = rising_temperature(weather)
print(result)
