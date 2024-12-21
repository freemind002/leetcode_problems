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
    result_df = (
        delivery.sort(["order_date", "customer_id"])
        .group_by("customer_id")
        .agg(["order_date", "customer_pref_delivery_date"])
        .filter(
            pl.col("order_date").list.first()
            == pl.col("customer_pref_delivery_date").list.first()
        )
        .select(
            immediate_percentage=(
                pl.col("customer_id").n_unique()
                / delivery.collect().n_unique("customer_id")
                * 100
            ).round(2)
        )
        .collect()
    )

    return result_df


result = immediate_food_delivery(delivery)
print(result)
