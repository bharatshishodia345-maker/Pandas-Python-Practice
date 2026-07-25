# Create a DataFrame using Pandas
# Save DataFrame in CSV, Excel and JSON formats

import pandas as pd

data = {
    'Name': ['Bharat', 'Sunil', 'Tarun', 'Ayush'],
    'City': ['Hapur', 'Agra', 'Hathras', 'Mathura'],
    'Age': [20, 22, 19, 21]
}

df = pd.DataFrame(data)

print(df)

# Save as CSV
df.to_csv('Output_file.csv', index=False)

# Save as Excel
# df.to_excel('Output_file.xlsx', index=False)

# Save as JSON
# df.to_json('Output_file.json', orient='records')