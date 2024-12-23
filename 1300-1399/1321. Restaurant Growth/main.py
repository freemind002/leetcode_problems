from datetime import timedelta

import polars as pl

data = [
    [1, "Jhon", "2019-01-01", 100],
    [2, "Daniel", "2019-01-02", 110],
    [3, "Jade", "2019-01-03", 120],
    [4, "Khaled", "2019-01-04", 130],
    [5, "Winston", "2019-01-05", 110],
    [6, "Elvis", "2019-01-06", 140],
    [7, "Anna", "2019-01-07", 150],
    [8, "Maria", "2019-01-08", 80],
    [9, "Jaze", "2019-01-09", 110],
    [1, "Jhon", "2019-01-10", 130],
    [3, "Jade", "2019-01-10", 150],
]
customer = pl.LazyFrame(
    data, schema=["customer_id", "name", "visited_on", "amount"], orient="row"
).cast(
    {
        "customer_id": pl.Int64,
        "name": pl.String,
        "visited_on": pl.Date,
        "amount": pl.Int64,
    }
)


def restaurant_growth(customer: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        customer.sort("visited_on")
        .group_by("visited_on")
        .agg(pl.col("amount").sum())
        .with_columns(
            amount=pl.sum("amount").rolling(index_column="visited_on", period="1w"),
            average_amount=(pl.sum("amount") / 7)
            .round(2)
            .rolling(index_column="visited_on", period="1w"),
        )
        .filter(pl.col("visited_on") >= pl.col("visited_on").min() + timedelta(days=6))
        .collect()
    )

    return result_df


result = restaurant_growth(customer)
print(result)
