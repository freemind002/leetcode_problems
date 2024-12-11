import polars as pl

products_data = [
    ["Wristwatch", None, 135],
    ["WirelessEarbuds", None, 821],
    ["GolfClubs", 779, 9319],
    ["Printer", 849, 3051],
]
products_schema = ["name", "quantity", "price"]

lf = pl.LazyFrame(products_data, products_schema)


def fillMissingValues(products: pl.LazyFrame) -> pl.DataFrame:
    result = products.with_columns(
        quantity=pl.col("quantity").fill_null(strategy="zero")
    ).collect()

    return result


result = fillMissingValues(lf)
print(result)
