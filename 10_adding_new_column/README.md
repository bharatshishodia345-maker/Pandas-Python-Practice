# Adding New Column in Pandas

This program demonstrates how to add a new column to a Pandas DataFrame using two different methods.

## Concepts Covered

* Adding a column directly
* Calculating a new column from an existing column
* Using the `insert()` function
* Understanding column position

## Methods Used

### 1. Direct Column Assignment

```python
df['Bonus'] = df['Salary'] * 0.1
```

This creates a new `Bonus` column based on the employee's salary.

### 2. Using `insert()`

```python
df.insert(0, 'Employ_Id', [10,20,30,40,50,60])
```

The `insert()` function allows us to specify the position of the new column.

## Output

The DataFrame contains the newly added `Bonus` and `Employ_Id` columns.

## Learning

This practice helps understand how to create and insert new columns in Pandas DataFrames.
