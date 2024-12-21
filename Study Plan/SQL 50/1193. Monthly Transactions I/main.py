import polars as pl

data = [
    [121, "US", "approved", 1000, "2018-12-18"],
    [122, "US", "declined", 2000, "2018-12-19"],
    [123, "US", "approved", 2000, "2019-01-01"],
    [124, "DE", "approved", 2000, "2019-01-07"],
]
transactions = pl.LazyFrame(
    data, schema=["id", "country", "state", "amount", "trans_date"], orient="row"
).cast(
    {
        "id": pl.Int64,
        "country": pl.String,
        "state": pl.String,
        "amount": pl.Int64,
        "trans_date": pl.Date,
    }
)


def monthly_transactions(transactions: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        transactions.with_columns(
            month=pl.col("trans_date").dt.to_string("%Y-%m"),
            approved_total_amount=pl.when(pl.col("state") == "approved")
            .then(pl.col("amount"))
            .otherwise(0),
        )
        .group_by(["month", "country"])
        .agg(
            trans_count=pl.col("state").count(),
            approved_count=pl.col("state").str.count_matches("approved").count(),
            trans_total_amount=pl.col("amount").sum(),
            approved_total_amount=pl.col("approved_total_amount").sum(),
        )
        .select(
            [
                "month",
                "country",
                "trans_count",
                "approved_count",
                "trans_total_amount",
                "approved_total_amount",
            ]
        )
        .collect()
    )

    return result_df


result = monthly_transactions(transactions)
print(result)
