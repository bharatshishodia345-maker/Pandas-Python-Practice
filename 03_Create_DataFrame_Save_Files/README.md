# Create DataFrame and Save Files

## Objective

Create a Pandas DataFrame from a Python dictionary and save the data into different file formats.

## Concepts Covered

- Creating DataFrame
- Python Dictionary
- `pd.DataFrame()`
- Saving DataFrame as CSV
- Saving DataFrame as Excel
- Saving DataFrame as JSON

## File Formats

### CSV

```python
df.to_csv('Output_file.csv', index=False)

Excel
df.to_excel('Output_file.xlsx', index=False)
JSON
df.to_json('Output_file.json', orient='records')
Libraries Used
Python
Pandas


---

# 04 — Head & Tail

### `head_tail.py`

```python
