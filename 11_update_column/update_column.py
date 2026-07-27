'''
Update column like employ salary 
'''
import pandas as pd


data = {
    'Name': ['Bharat', 'Tarun', 'Ayush', 'Sunil', 'Anuj', 'Krrish'],
    'Age': [20, 19, 21, 23, 22, 18],
    'Salary': [51000, 45000, 35000, 40000, 52000, 55000],
    'Performance_Score': [90, 92, 85, 75, 88, 79]
}

df = pd.DataFrame(data)
print('---sample_data----')
print(df)

# Update the all employ salary
df['Salary'] = df['Salary'] * 1.5
print('---New_updating_salary---')
print(df)