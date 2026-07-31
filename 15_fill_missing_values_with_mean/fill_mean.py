'''
find the mean  in dataset every column and fill Average value
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


# fill the avg value 

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Performance_Score'].fillna(df['Performance_Score'].mean(), inplace=True)
print('---After_Filling_avg_value---')
print(df)
