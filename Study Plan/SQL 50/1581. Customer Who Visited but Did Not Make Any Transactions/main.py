import polars as pl

data = [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]]
visits = pl.LazyFrame(data, schema=["visit_id", "customer_id"]).cast(
    {"visit_id": pl.Int64, "customer_id": pl.Int64}
)
data = [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]]
transactions = pl.LazyFrame(data, schema=["transaction_id", "visit_id", "amount"]).cast(
    {"transaction_id": pl.Int64, "visit_id": pl.Int64, "amount": pl.Int64}
)


def find_customers(visits: pl.LazyFrame, transactions: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        visits.join(transactions, on="visit_id", how="left")
        .filter(pl.col("transaction_id").is_null())
        .group_by("customer_id")
        .len("count_no_trans")
        .collect()
    )

    return result_df


result = find_customers(visits, transactions)
print(result)
