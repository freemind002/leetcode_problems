import polars as pl

data = [[1, "Alice"], [2, "Bob"], [13, "John"], [6, "Alex"]]
students = pl.LazyFrame(data, schema=["student_id", "student_name"], orient="row").cast(
    {"student_id": pl.Int64, "student_name": pl.String}
)
data = [["Math"], ["Physics"], ["Programming"]]
subjects = pl.LazyFrame(data, schema=["subject_name"], orient="row").cast(
    {"subject_name": pl.String}
)
data = [
    [1, "Math"],
    [1, "Physics"],
    [1, "Programming"],
    [2, "Programming"],
    [1, "Physics"],
    [1, "Math"],
    [13, "Math"],
    [13, "Programming"],
    [13, "Physics"],
    [2, "Math"],
    [1, "Math"],
]
examinations = pl.LazyFrame(
    data, schema=["student_id", "subject_name"], orient="row"
).cast({"student_id": pl.Int64, "subject_name": pl.String})


def students_and_examinations(
    students: pl.LazyFrame, subjects: pl.LazyFrame, examinations: pl.LazyFrame
) -> pl.DataFrame:
    result_df = (
        students.join(subjects, how="cross")
        .join(
            examinations.group_by(["student_id", "subject_name"]).len("attended_exams"),
            how="left",
            on=["student_id", "subject_name"],
        )
        .with_columns(pl.col("attended_exams").fill_null(strategy="zero"))
        .sort(["student_id", "subject_name"])
        .collect()
    )

    return result_df


result = students_and_examinations(students, subjects, examinations)
print(result)
