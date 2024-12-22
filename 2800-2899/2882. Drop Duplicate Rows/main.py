import polars as pl

customers_data = [
    [1, "Ella", "emily@example.com"],
    [2, "David", "michael@example.com"],
    [3, "Zachary", "sarah@example.com"],
    [4, "Alice", "john@example.com"],
    [5, "Finn", "john@example.com"],
    [6, "Violet", "alice@example.com"],
]
customers_schema = ["customer_id", "name", "email"]

lf = pl.LazyFrame(customers_data, customers_schema)


def dropDuplicateEmails(customers: pl.LazyFrame) -> pl.DataFrame:
    result = customers.unique(subset=["email"], keep="first").collect()

    return result


result = dropDuplicateEmails(lf)
print(result)
