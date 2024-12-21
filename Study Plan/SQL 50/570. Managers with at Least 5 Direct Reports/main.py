import polars as pl

data = [
    [101, "John", "A", None],
    [102, "Dan", "A", 101],
    [103, "James", "A", 101],
    [104, "Amy", "A", 101],
    [105, "Anne", "A", 101],
    [106, "Ron", "B", 101],
]
employee = pl.LazyFrame(
    data, schema=["id", "name", "department", "managerId"], orient="row"
).cast(
    {"id": pl.Int64, "name": pl.String, "department": pl.String, "managerId": pl.Int64}
)


def find_managers(employee: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        employee.join(
            employee.group_by("managerId").agg(id_count=pl.col("id").n_unique()),
            left_on="id",
            right_on="managerId",
        )
        .filter(pl.col("id_count") >= 5)
        .select("name")
        .collect()
    )

    return result_df


result = find_managers(employee)
print(result)
