# Fill Missing Values Using Interpolation

This program demonstrates how to estimate missing numerical values using the `interpolate()` function in Pandas.

## Topics Covered

* Missing values
* Linear interpolation
* `interpolate()`
* Data preprocessing

## Example

```python
df['Complaxity'] = df['Complaxity'].interpolate(method='linear')
```

## How It Works

Linear interpolation estimates missing values by calculating intermediate values between known data points.

Example:

```text
Before:
1
NaN
3
NaN
5

After:
1
2
3
4
5
```

## Learning

I learned how to estimate missing numerical values using linear interpolation, a commonly used technique for handling continuous data in data analysis.
