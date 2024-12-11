import polars as pl

employees_data = [
    ["Piper", 4548],
    ["Grace", 28150],
    ["Georgia", 1103],
    ["Willow", 6593],
    ["Finn", 74576],
    ["Thomas", 24433],
]
employees_schema = ["name", "salary"]

lf = pl.LazyFrame(employees_data, employees_schema)


def createBonusColumn(employees: pl.LazyFrame) -> pl.DataFrame:
    result = employees.with_columns(bonus=pl.col("salary") * 2).collect()

    return result


result = createBonusColumn(lf)
print(result)
