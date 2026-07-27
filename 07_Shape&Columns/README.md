# Shape and Columns in Pandas

## 📌 Objective

Learn how to check the structure and column names of a Pandas DataFrame.

## 🧠 Concepts Covered

- `df.shape`
- `df.columns`

## 💻 Code

```python
import pandas as pd

data = {
    'Name': ['Bharat', 'Tarun', 'Ayush', 'Sunil', 'Anuj', 'Krrish'],
    'Age': [20, 19, 21, 23, 22, 18],
    'Salary': [50000, 45000, 35000, 400000, 520000, 550000],
    'Performance_Score': [90, 92, 85, 75, 88, 79]
}

df = pd.DataFrame(data)

print(df)

print(f'Shape: {df.shape}')
print(f'Columns: {df.columns}')