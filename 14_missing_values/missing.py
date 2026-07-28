'''
find the missing value in dataset using isnull function
'''

import pandas as pd


data = {
    'Name': ['Bharat', None, 'Ayush', 'Sunil', 'Anuj', 'Krrish'],
    'Age': [None, 19, 21, 23, None, 18],
    'Salary': [51000, 45000, 35000, 40000, None, 55000],
    'Performance_Score': [90, None, 85, 75, 88, 79]
}

df = pd.DataFrame(data)
print('---sample_data----')
print(df)

print('Missing value')

print(df.isnull().sum())
