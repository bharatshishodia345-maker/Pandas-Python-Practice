# Fill Missing Values with Mean in Pandas

This program demonstrates how to replace missing numerical values in a Pandas DataFrame using the mean (average) of each column.

## Topics Covered

* Missing values
* `fillna()`
* `mean()`
* Data cleaning
* Handling null values

## Example

```python
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Performance_Score'].fillna(df['Performance_Score'].mean(), inplace=True)
```

## How It Works

* Calculates the average value of each numeric column.
* Replaces every missing value (`NaN`) with the calculated mean.
* Keeps the dataset complete without removing rows.

## Learning

I learned how to handle missing numerical data using the `fillna()` and `mean()` functions in Pandas, which is a common data preprocessing technique used in data analysis and machine learning.
