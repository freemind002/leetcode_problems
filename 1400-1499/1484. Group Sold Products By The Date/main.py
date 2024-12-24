import polars as pl

data = [
    ["2020-05-30", "Headphone"],
    ["2020-06-01", "Pencil"],
    ["2020-06-02", "Mask"],
    ["2020-05-30", "Basketball"],
    ["2020-06-01", "Bible"],
    ["2020-06-02", "Mask"],
    ["2020-05-30", "T-Shirt"],
]
activities = pl.LazyFrame(data, schema=["sell_date", "product"], orient="row").cast(
    {"sell_date": pl.Date, "product": pl.String}
)


def categorize_products(activities: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        activities.group_by("sell_date")
        .agg(num_sold=pl.col("product").len(), products=pl.col("product").sort())
        .with_columns(pl.col("products").list.join(", "))
        .sort("sell_date")
        .collect()
    )

    return result_df


result = categorize_products(activities)
print(result)
