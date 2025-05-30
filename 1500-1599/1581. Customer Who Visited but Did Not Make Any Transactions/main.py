import polars as pl

data = [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]]
visits = pl.LazyFrame(
    data, schema={"visit_id": pl.Int64, "customer_id": pl.Int64}, orient="row"
)
data = [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]]
transactions = pl.LazyFrame(
    data,
    schema={"transaction_id": pl.Int64, "visit_id": pl.Int64, "amount": pl.Int64},
    orient="row",
)


def find_customers(visits: pl.LazyFrame, transactions: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        visits.join(transactions, on="visit_id", how="left")
        .filter(pl.col("transaction_id").is_null())
        .group_by("customer_id")
        .agg(count_no_trans=pl.col("visit_id").count())
        .collect()
    )

    return result_df


result = find_customers(visits, transactions)
print(result)
