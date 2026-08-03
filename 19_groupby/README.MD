# Group Data by Age using Pandas

## Problem

Group employee records based on the `Age` column and calculate the total salary for each age group.

## Approach

- Create a DataFrame.
- Use the `groupby()` method on the `Age` column.
- Select the `Salary` column.
- Apply the `sum()` function to calculate the total salary for each age group.

## Methods Used

- `groupby()`
- `sum()`

## Time Complexity

O(n)

## Space Complexity

O(k)

Where:
- `n` = number of rows
- `k` = number of unique age groups

## Example

Input

```python
Age    Salary
20     51000
20     45000
21     35000
21     40000
```

Output

```python
Age
20     96000
21     75000
```