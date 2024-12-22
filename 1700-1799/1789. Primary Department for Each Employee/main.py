import polars as pl

data = [
    ["1", "1", "N"],
    ["2", "1", "Y"],
    ["2", "2", "N"],
    ["3", "3", "N"],
    ["4", "2", "N"],
    ["4", "3", "Y"],
    ["4", "4", "N"],
]
employee = pl.LazyFrame(
    data, schema=["employee_id", "department_id", "primary_flag"], orient="row"
).cast({"employee_id": pl.Int64, "department_id": pl.Int64, "primary_flag": pl.String})


def find_primary_department(employee: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        employee.filter(
            (~pl.col("employee_id").is_duplicated()) | (pl.col("primary_flag") == "Y")
        )
        .select(["employee_id", "department_id"])
        .collect()
    )

    return result_df


result = find_primary_department(employee)
print(result)
