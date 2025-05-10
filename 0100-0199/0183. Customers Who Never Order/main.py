import polars as pl

data = [[1, "Joe"], [2, "Henry"], [3, "Sam"], [4, "Max"]]
customers = pl.LazyFrame(data, schema={"id": pl.Int64, "name": pl.String}, orient="row")
data = [[1, 3], [2, 1]]
orders = pl.LazyFrame(
    data, schema={"id": pl.Int64, "customerId": pl.Int64}, orient="row"
)


def find_customers(customers: pl.LazyFrame, orders: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        customers.join(orders, how="anti", left_on="id", right_on="customerId")
        .select(Customers=pl.col("name"))
        .collect()
    )

    return result_df


result = find_customers(customers, orders)
print(result)
