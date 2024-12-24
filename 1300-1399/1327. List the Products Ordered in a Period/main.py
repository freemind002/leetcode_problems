from datetime import date, timedelta

import polars as pl
from annotated_types import T

data = [
    [1, "Leetcode Solutions", "Book"],
    [2, "Jewels of Stringology", "Book"],
    [3, "HP", "Laptop"],
    [4, "Lenovo", "Laptop"],
    [5, "Leetcode Kit", "T-shirt"],
]
products = pl.LazyFrame(
    data, schema=["product_id", "product_name", "product_category"], orient="row"
).cast(
    {"product_id": pl.Int64, "product_name": pl.String, "product_category": pl.String}
)
data = [
    [1, "2020-02-05", 60],
    [1, "2020-02-10", 70],
    [2, "2020-01-18", 30],
    [2, "2020-02-11", 80],
    [3, "2020-02-17", 2],
    [3, "2020-02-24", 3],
    [4, "2020-03-01", 20],
    [4, "2020-03-04", 30],
    [4, "2020-03-04", 60],
    [5, "2020-02-25", 50],
    [5, "2020-02-27", 50],
    [5, "2020-03-01", 50],
]
orders = pl.LazyFrame(
    data, schema=["product_id", "order_date", "unit"], orient="row"
).cast({"product_id": pl.Int64, "order_date": pl.Date, "unit": pl.Int64})


def list_products(products: pl.LazyFrame, orders: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        orders.filter(
            pl.col("order_date").is_between(
                date(2020, 2, 1), date(2020, 3, 1), closed="left"
            )
        )
        .join(products, on="product_id")
        .group_by("product_name")
        .agg(pl.col("unit").sum())
        .filter(pl.col("unit") >= 100)
        .sort("unit", descending=True)
        .collect()
    )

    return result_df


result = list_products(products, orders)
print(result)
