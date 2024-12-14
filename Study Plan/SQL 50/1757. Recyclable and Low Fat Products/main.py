import polars as pl

data = [
    ["0", "Y", "N"],
    ["1", "Y", "Y"],
    ["2", "N", "Y"],
    ["3", "Y", "Y"],
    ["4", "N", "N"],
]
schema = ["product_id", "low_fats", "recyclable"]
lf = pl.LazyFrame(data, schema).cast(
    {"product_id": pl.Int64, "low_fats": pl.Categorical, "recyclable": pl.Categorical}
)


def find_products(products: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        products.filter(low_fats="Y", recyclable="Y").select("product_id").collect()
    )

    return result_df


result = find_products(lf)
print(result)
