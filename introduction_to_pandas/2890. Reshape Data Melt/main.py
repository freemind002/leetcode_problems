import polars as pl
import polars.selectors as cs

report_lf = pl.LazyFrame(
    [
        ["Umbrella", 417, 224, 379, 611],
        ["SleepingBag", 800, 936, 93, 875],
    ],
    ["product", "quarter_1", "quarter_2", "quarter_3", "quarter_4"],
)


def meltTable(report: pl.LazyFrame) -> pl.DataFrame:
    # return pd.melt(report, id_vars=['product'],var_name='quarter', value_name='sales')
    result = report.unpivot(
        on=cs.numeric(), index="product", value_name="sales"
    ).collect()

    return result


result = meltTable(report_lf)
print(result)
