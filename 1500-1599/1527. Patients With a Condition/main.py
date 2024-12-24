import polars as pl

data = [
    [1, "Daniel", "YFEV COUGH"],
    [2, "Alice", ""],
    [3, "Bob", "DIAB100 MYOP"],
    [4, "George", "ACNE DIAB100"],
    [5, "Alain", "DIAB201"],
]
patients = pl.LazyFrame(
    data, schema=["patient_id", "patient_name", "conditions"], orient="row"
).cast({"patient_id": pl.Int64, "patient_name": pl.String, "conditions": pl.String})


def find_patients(patients: pl.LazyFrame) -> pl.DataFrame:
    result_df = patients.filter(
        pl.col("conditions").str.contains(r"(^| )DIAB1")
    ).collect()

    return result_df


result = find_patients(patients)
print(result)
