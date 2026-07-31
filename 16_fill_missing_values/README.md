# Fill Missing Values in Pandas

This program demonstrates how to replace missing values in a Pandas DataFrame using custom values with the `fillna()` function.

## Topics Covered

* Missing values
* `fillna()`
* Custom replacement values
* Data preprocessing

## Example

```python
df.fillna({
    'Name': 'Unknown',
    'Age': 20,
    'Salary': 50000,
    'Performance_Score': 80
}, inplace=True)
```

## How It Works

The `fillna()` function replaces missing values with user-defined values instead of deleting rows from the dataset.

## Learning

I learned how to replace missing values with custom values using Pandas, an important preprocessing step before performing data analysis or machine learning.
