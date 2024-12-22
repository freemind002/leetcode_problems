import polars as pl

data = [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]]
customer = pl.LazyFrame(data, schema=["customer_id", "product_key"], orient="row").cast(
    {"customer_id": pl.Int64, "product_key": pl.Int64}
)
data = [[5], [6]]
product = pl.LazyFrame(data, schema=["product_key"], orient="row").cast(
    {"product_key": pl.Int64}
)


def find_customers(customer: pl.LazyFrame, product: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        customer.join(
            product.unique(),
            on="product_key",
            how="inner",
        )
        .group_by("customer_id")
        .n_unique()
        .filter(pl.col("product_key") == product.collect().n_unique())
        .select("customer_id")
        .collect()
    )

    return result_df


result = find_customers(customer, product)
print(result)
