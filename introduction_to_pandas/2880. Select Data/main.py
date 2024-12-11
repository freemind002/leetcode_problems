import polars as pl

students_data = [
    [101, "Ulysses", 13],
    [53, "William", 10],
    [128, "Henry", 6],
    [3, "Henry", 11],
]
students_schema = ["student_id", "name", "age"]

lf = pl.LazyFrame(students_data, students_schema)


def selectData(students: pl.LazyFrame) -> pl.DataFrame:
    result = students.filter(student_id=101).select(["name", "age"]).collect()

    return result


result = selectData(lf)
print(result)
