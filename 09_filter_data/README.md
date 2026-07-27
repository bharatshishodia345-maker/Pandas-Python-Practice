```markdown
# Filtering Data Using Pandas

## 📌 Objective

Learn how to filter DataFrame rows using conditions.

## 🧠 Concepts Covered

- Single condition
- Multiple conditions
- AND operator `&`
- OR operator `|`
- Boolean filtering

## 💻 Single Condition

```python
high_salary = df[df['Salary'] > 50000]

print(high_salary)