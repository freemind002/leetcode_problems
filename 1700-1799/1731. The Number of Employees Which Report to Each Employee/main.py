import polars as pl

data = [
    [9, "Hercy", None, 43],
    [6, "Alice", 9, 41],
    [4, "Bob", 9, 36],
    [2, "Winston", None, 37],
]
employees = pl.LazyFrame(
    data, schema=["employee_id", "name", "reports_to", "age"], orient="row"
).cast(
    {
        "employee_id": pl.Int64,
        "name": pl.String,
        "reports_to": pl.Int64,
        "age": pl.Int64,
    }
)


def count_employees(employees: pl.LazyFrame) -> pl.DataFrame:
    print(employees.collect())
    result_df = (
        employees.join(employees, left_on="employee_id", right_on="reports_to")
        .group_by(["employee_id", "name"])
        .agg(
            reports_count=pl.col("employee_id_right").count(),
            average_age=pl.col("age_right").mean().round(0),
        )
        .collect()
    )

    return result_df


result = count_employees(employees)
print(result)
