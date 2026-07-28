# Finding Missing Values in Pandas

This program demonstrates how to identify missing values in a Pandas DataFrame using the `isnull()` function.

## Topics Covered

* Missing values
* `None`
* `isnull()`
* `sum()`
* Counting missing values column-wise

## Example

```python
df.isnull().sum()
```

## How It Works

`isnull()` checks every cell in the DataFrame and returns:

* `True` → value is missing
* `False` → value is present

The `sum()` function then counts the missing values in each column.

## Example Output

```text
Name                  1
Age                   2
Salary                1
Performance_Score     1
dtype: int64
```

## Learning

I learned how to detect and count missing values in a Pandas DataFrame using `isnull().sum()`.
