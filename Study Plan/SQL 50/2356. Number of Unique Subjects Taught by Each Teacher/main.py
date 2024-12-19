import polars as pl

data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
teacher = pl.LazyFrame(data, schema=["teacher_id", "subject_id", "dept_id"]).cast(
    {"teacher_id": pl.Int64, "subject_id": pl.Int64, "dept_id": pl.Int64}
)


def count_unique_subjects(teacher: pl.LazyFrame) -> pl.DataFrame:
    print(teacher.collect())

    result_df = (
        teacher.group_by("teacher_id")
        .agg(cnt=pl.col("subject_id").unique().count())
        .collect()
    )

    return result_df


result = count_unique_subjects(teacher)
print(result)
