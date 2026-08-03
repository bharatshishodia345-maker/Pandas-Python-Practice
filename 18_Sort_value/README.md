# Sort Values in Pandas

## Overview

This folder demonstrates how to sort data in a Pandas DataFrame using the `sort_values()` function.

## Examples

### 1. Sort by a Single Column

- Sort employee records by `Age` in ascending order.
- Uses:
  - `sort_values()`
  - `ascending=True`
  - `inplace=True`

### 2. Sort by Multiple Columns

- Sort employee records using multiple columns.
- First sorts by `Age`, then by `Salary`.
- Uses:
  - `sort_values(by=['Age', 'Salary'])`
  - `ascending=[True, True]`

## Methods Used

- `sort_values()`
- `ascending`
- `inplace`

## Time Complexity

- Average: **O(n log n)**

## Space Complexity

- O(n)