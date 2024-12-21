import polars as pl

data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
sales = pl.LazyFrame(
    data, schema=["sale_id", "product_id", "year", "quantity", "price"], orient="row"
).cast(
    {
        "sale_id": pl.Int64,
        "product_id": pl.Int64,
        "year": pl.Int64,
        "quantity": pl.Int64,
        "price": pl.Int64,
    }
)
data = [[100, "Nokia"], [200, "Apple"], [300, "Samsung"]]
product = pl.LazyFrame(data, schema=["product_id", "product_name"], orient="row").cast(
    {"product_id": pl.Int64, "product_name": pl.String}
)


def sales_analysis(sales: pl.LazyFrame, product: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        sales.join(
            sales.join(product, on="product_id", how="inner")
            .group_by("product_id")
            .agg(pl.col("year").min()),
            on=["product_id", "year"],
            how="inner",
        )
        .rename({"year": "first_year"})
        .select(["product_id", "first_year", "quantity", "price"])
        .collect()
    )

    return result_df


result = sales_analysis(sales, product)
print(result)
