# Check Dataset Information Using Pandas

## Objective

In this practice, I learned how to inspect a dataset and check its basic information using Pandas.

## Code

```python
import pandas as pd

df = pd.read_excel('College.xlsx')

print('--- Dataset Information ---')
print(df.info())