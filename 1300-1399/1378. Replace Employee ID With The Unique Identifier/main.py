import polars as pl

data = [[1, "Alice"], [7, "Bob"], [11, "Meir"], [90, "Winston"], [3, "Jonathan"]]
employees = pl.LazyFrame(data, schema=["id", "name"], orient="row").cast(
    {"id": pl.Int64, "name": pl.String}
)
data = [[3, 1], [11, 2], [90, 3]]
employee_uni = pl.LazyFrame(data, schema=["id", "unique_id"], orient="row").cast(
    {"id": pl.Int64, "unique_id": pl.Int64}
)


def replace_employee_id(
    employees: pl.LazyFrame, employee_uni: pl.LazyFrame
) -> pl.DataFrame:
    result_df = (
        employees.join(employee_uni, on="id", how="left")
        .select(["unique_id", "name"])
        .collect()
    )

    return result_df


result = replace_employee_id(employees, employee_uni)
print(result)
