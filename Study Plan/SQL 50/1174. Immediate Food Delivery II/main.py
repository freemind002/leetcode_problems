import polars as pl

data = [
    [1, 1, "2019-08-01", "2019-08-02"],
    [2, 2, "2019-08-02", "2019-08-02"],
    [3, 1, "2019-08-11", "2019-08-12"],
    [4, 3, "2019-08-24", "2019-08-24"],
    [5, 3, "2019-08-21", "2019-08-22"],
    [6, 2, "2019-08-11", "2019-08-13"],
    [7, 4, "2019-08-09", "2019-08-09"],
]
delivery = pl.LazyFrame(
    data,
    schema=["delivery_id", "customer_id", "order_date", "customer_pref_delivery_date"],
    orient="row",
).cast(
    {
        "delivery_id": pl.Int64,
        "customer_id": pl.Int64,
        "order_date": pl.Date,
        "customer_pref_delivery_date": pl.Date,
    }
)


def immediate_food_delivery(delivery: pl.LazyFrame) -> pl.DataFrame:
    print(delivery.collect())
    result_df = (
        delivery.sort(["order_date", "customer_id"])
        .group_by("customer_id")
        .agg(
            pl.when(
                (pl.col("order_date") == pl.col("customer_pref_delivery_date")).first()
            )
            .then(1)
            .otherwise(0)
            .alias("immediate_percentage")
        )
        .with_columns(
            (
                pl.col("immediate_percentage").sum()
                / pl.col("customer_id").count()
                * 100
            ).round(2)
        )
        .select("immediate_percentage")
        .head(1)
        .collect()
    )

    return result_df


result = immediate_food_delivery(delivery)
print(result)
