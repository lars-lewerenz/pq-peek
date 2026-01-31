from pathlib import Path

import numpy as np
import polars as pl


def create_dummy():
    row_count = 1_000_000
    df = pl.DataFrame(
        {
            "id": range(row_count),
            "price": np.random.rand(row_count) * 100,
            "category": np.random.choice(
                ["Electronics", "Books", "Clothing"], row_count
            ),
            "is_available": np.random.choice([True, False], row_count),
            "description": ["Product description placeholder"] * row_count,
        }
    )

    file_path = Path(__file__).with_name("data.parquet")
    df.write_parquet(file_path)
    print(f"Created '{file_path}' with {row_count} rows.")


if __name__ == "__main__":
    create_dummy()
