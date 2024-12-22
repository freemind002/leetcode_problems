import polars as pl

data = [
    [3, "Mila", 9, 60301],
    [12, "Antonella", None, 31000],
    [13, "Emery", None, 67084],
    [1, "Kalel", 11, 21241],
    [9, "Mikaela", None, 50937],
    [11, "Joziah", 6, 28485],
]
employees = pl.LazyFrame(
    data, schema=["employee_id", "name", "manager_id", "salary"], orient="row"
).cast(
    {
        "employee_id": pl.Int64,
        "name": pl.String,
        "manager_id": pl.Int64,
        "salary": pl.Int64,
    }
)


def find_employees(employees: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        employees.filter(
            ~pl.col("manager_id").is_in(pl.col("employee_id")), pl.col("salary") < 30000
        )
        .select("employee_id")
        .collect()
    )

    return result_df


result = find_employees(employees)
print(result)
