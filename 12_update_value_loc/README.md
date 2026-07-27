# Update Specific Value Using loc

This program demonstrates how to update a specific value in a Pandas DataFrame using the `loc` function.

## Concept Covered

* Using `loc`
* Selecting a specific row and column
* Updating a particular DataFrame value

## Example

The salary of the first employee is changed using:

```python
df.loc[0, 'Salary'] = 55000
```

Here:

* `0` represents the row index.
* `'Salary'` represents the column.
* `55000` is the new value.

## Learning

The `loc` function is useful when we need to access or modify specific rows and columns in a DataFrame.
