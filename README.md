# [pq-peek](https://github.com/lars-lewerenz/pq-peek) 🦆

[![PyPI](https://img.shields.io/pypi/v/pq-peek)](https://pypi.org/project/pq-peek/)
[![Publish](https://github.com/lars-lewerenz/pq-peek/actions/workflows/release.yml/badge.svg)](https://github.com/lars-lewerenz/pq-peek/actions/workflows/release.yml)
[![Lint](https://github.com/lars-lewerenz/pq-peek/actions/workflows/lint.yml/badge.svg)](https://github.com/lars-lewerenz/pq-peek/actions/workflows/lint.yml)
[![CLI Smoke](https://github.com/lars-lewerenz/pq-peek/actions/workflows/smoke.yml/badge.svg)](https://github.com/lars-lewerenz/pq-peek/actions/workflows/smoke.yml)

A blazing fast, memory-efficient CLI tool to inspect large Parquet files directly in the terminal.
Built with *Polars*, *Typer*, and *Rich*. Managed via *uv*.

## Install (uv)

```bash
uv pip install --system pq-peek
```

## CLI usage

```bash
pq-peek schema /path/to/file.parquet
pq-peek head /path/to/file.parquet --n 5
pq-peek stats /path/to/file.parquet
```

## Sample output

Schema:

```text
   Schema: data.parquet
┏━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Column name  ┃ Type    ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ id           │ Int64   │
│ price        │ Float64 │
│ category     │ String  │
│ is_available │ Boolean │
│ description  │ String  │
└──────────────┴─────────┘

Amount of columns: 5
```

Head:

```text
                         Preview data.parquet (3 rows)
┏━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ id ┃ price              ┃ category ┃ is_available ┃ description              ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 0  │ 16.00485297904456  │ Clothing │ False        │ Product description      │
│    │                    │          │              │ placeholder              │
│ 1  │ 31.286728959372468 │ Books    │ True         │ Product description      │
│    │                    │          │              │ placeholder              │
│ 2  │ 51.69244000425412  │ Books    │ False        │ Product description      │
│    │                    │          │              │ placeholder              │
└────┴────────────────────┴──────────┴──────────────┴──────────────────────────┘
```

Stats:

```text
shape: (9, 6)
┌────────────┬───────────────┬───────────┬─────────────┬──────────────┬──────────────────────────┐
│ statistic  ┆ id            ┆ price     ┆ category    ┆ is_available ┆ description              │
│ ---        ┆ ---           ┆ ---       ┆ ---         ┆ ---          ┆ ---                      │
│ str        ┆ f64           ┆ f64       ┆ str         ┆ f64          ┆ str                      │
╞════════════╪═══════════════╪═══════════╪═════════════╪══════════════╪══════════════════════════╡
│ count      ┆ 1e6           ┆ 1e6       ┆ 1000000     ┆ 1e6          ┆ 1000000                  │
│ null_count ┆ 0.0           ┆ 0.0       ┆ 0           ┆ 0.0          ┆ 0                        │
│ mean       ┆ 499999.5      ┆ 49.997178 ┆ null        ┆ 0.499979     ┆ null                     │
│ ...        ┆ ...           ┆ ...       ┆ ...         ┆ ...          ┆ ...                      │
│ max        ┆ 9.99999e5     ┆ 99.999956 ┆ Electronics ┆ 1.0          ┆ Product description ...  │
└────────────┴───────────────┴───────────┴─────────────┴──────────────┴──────────────────────────┘
```

## Module usage

```bash
python -m pq_peek schema /path/to/file.parquet
```

## Build and publish (uv)

```bash
uv build
uv publish
```

## Publishing notes

CI publishing uses GitHub's Trusted Publisher OIDC. See `PUBLISHING.md` for the full release steps.