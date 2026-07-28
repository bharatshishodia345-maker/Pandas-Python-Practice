# Remove Columns in Pandas

This program demonstrates how to remove columns from a Pandas DataFrame using the `drop()` function.

## Topics Covered

* Remove a single column
* Remove multiple columns
* `drop()` function
* `columns` parameter
* `inplace=True`

## Example

### Remove Single Column

```python
df.drop(columns=['Performance_Score'], inplace=True)
```

### Remove Multiple Columns

```python
df.drop(columns=['Salary', 'Age'], inplace=True)
```

## Key Concept

`inplace=True` directly modifies the existing DataFrame instead of creating a new DataFrame.

## Output

The program first displays the original DataFrame, then shows the DataFrame after removing one column and finally after removing multiple columns.

## Learning

I learned how to remove unnecessary columns from a Pandas DataFrame using the `drop()` function.
