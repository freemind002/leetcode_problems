import polars as pl

emloyees_data = [
    ["Jack", 19666],
    ["Piper", 74754],
    ["Mia", 62509],
    ["Ulysses", 54866],
]
emloyees_schema = ["name", "salary"]

lf = pl.LazyFrame(emloyees_data, emloyees_schema)


def modifySalaryColumn(employees: pl.LazyFrame) -> pl.DataFrame:
    result = employees.with_columns(salary=pl.col("salary") * 2).collect()

    return result


result = modifySalaryColumn(lf)
print(result)
