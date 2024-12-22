import polars as pl

data = [
    [1, "2019-02-17", "2019-02-28", 5],
    [1, "2019-03-01", "2019-03-22", 20],
    [2, "2019-02-01", "2019-02-20", 15],
    [2, "2019-02-21", "2019-03-31", 30],
]
prices = pl.LazyFrame(
    data, schema=["product_id", "start_date", "end_date", "price"], orient="row"
).cast(
    {
        "product_id": pl.Int64,
        "start_date": pl.Date,
        "end_date": pl.Date,
        "price": pl.Int64,
    }
)
data = [
    [1, "2019-02-25", 100],
    [1, "2019-03-01", 15],
    [2, "2019-02-10", 200],
    [2, "2019-03-22", 30],
]
units_sold = pl.LazyFrame(
    data, schema=["product_id", "purchase_date", "units"], orient="row"
).cast({"product_id": pl.Int64, "purchase_date": pl.Date, "units": pl.Int64})


def average_selling_price(
    prices: pl.LazyFrame, units_sold: pl.LazyFrame
) -> pl.DataFrame:
    result_df = (
        prices.join(units_sold, on="product_id", how="left")
        .filter(
            (
                pl.col("purchase_date").is_between(
                    pl.col("start_date"), pl.col("end_date")
                )
            )
            | (pl.col("purchase_date").is_null())
        )
        .group_by("product_id")
        .agg(
            total_revenue=(pl.col("price") * pl.col("units")).sum(),
            total_units=pl.col("units").sum(),
        )
        .select(
            product_id=pl.col("product_id"),
            average_price=(pl.col("total_revenue") / pl.col("total_units")).round(2),
        )
        .collect()
    )

    return result_df


result = average_selling_price(prices, units_sold)
print(result)
