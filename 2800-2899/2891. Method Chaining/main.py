import polars as pl
import polars.selectors as cs

animals_lf = pl.LazyFrame(
    [
        ["Tatiana", "Snake", 98, 464],
        ["Khaled", "Giraffe", 50, 41],
        ["Alex", "Leopard", 6, 328],
        ["Jonathan", "Monkey", 45, 463],
        ["Stefan", "Bear", 100, 50],
        ["Tommy", "Panda", 26, 349],
    ],
    ["name", "species", "age", "weight"],
)


def findHeavyAnimals(animals: pl.LazyFrame) -> pl.DataFrame:
    result = (
        animals.filter(pl.col("weight") > 100)
        .sort("weight", descending=True)
        .select("name")
        .collect()
    )

    return result


result = findHeavyAnimals(animals_lf)
print(result)
