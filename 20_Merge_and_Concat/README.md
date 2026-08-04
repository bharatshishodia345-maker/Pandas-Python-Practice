# Merge and Concat Data in Pandas

## Overview

This folder demonstrates two important Pandas operations:

1. Merge DataFrames
2. Concatenate DataFrames

---

## 1. Merge DataFrames

### Description

The `merge()` function is used to combine two DataFrames based on a common column (key), similar to SQL joins.

### Example

```python
pd.merge(df_customer, df_order, on='CustomerID', how='inner')
```

### Join Used

- Inner Join

### Output

Only matching `CustomerID` values from both DataFrames are returned.

---

## 2. Concatenate DataFrames

### Description

The `concat()` function combines multiple DataFrames either row-wise or column-wise.

### Example

```python
pd.concat([df_region_1, df_region_2], axis=0, ignore_index=True)
```

### Parameters

- `axis=0` → Append rows
- `ignore_index=True` → Reset index after concatenation

### Output

Both DataFrames are combined into a single DataFrame.

---

## Files

- `merge_data.py` → Demonstrates merging DataFrames using `merge()`.
- `concat_data.py` → Demonstrates combining DataFrames using `concat()`.

---

## Concepts Covered

- DataFrame Merge
- Inner Join
- Common Key
- DataFrame Concatenation
- Row-wise Combination
- Index Reset

---

## Library Used

- pandas
