from datetime import date

import polars as pl

data = [
    [1, 20, "2019-08-14"],
    [2, 50, "2019-08-14"],
    [1, 30, "2019-08-15"],
    [1, 35, "2019-08-16"],
    [2, 65, "2019-08-17"],
    [3, 20, "2019-08-18"],
]
products = pl.LazyFrame(
    data, schema=["product_id", "new_price", "change_date"], orient="row"
).cast({"product_id": pl.Int64, "new_price": pl.Int64, "change_date": pl.Date})


def price_at_given_date(products: pl.LazyFrame) -> pl.DataFrame:
    concat_lf = products.with_columns(
        price=pl.when(pl.col("change_date") <= date(2019, 8, 16))
        .then(pl.col("new_price"))
        .otherwise(10)
    )
    result_df = (
        concat_lf.group_by("product_id")
        .agg(
            change_date=pl.when(pl.col("change_date").max() <= date(2019, 8, 16))
            .then(pl.col("change_date").max())
            .otherwise(pl.col("change_date").min())
        )
        .join(concat_lf, on=["product_id", "change_date"])
        .select(["product_id", "price"])
        .collect()
    )

    return result_df


result = price_at_given_date(products)
print(result)
