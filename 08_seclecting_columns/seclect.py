'''
select multple columns 
select single columns 

'''

import pandas as pd 

data = {
    'Name': ['Bharat', 'Tarun', 'Ayush', 'Sunil', 'Anuj', 'Krrish'],
    'Age': [20, 19, 21, 23, 22, 18],
    'Salary': [50000, 45000, 35000, 400000, 520000, 550000],
    'Performance_Score': [90, 92, 85, 75, 88, 79]
}

df = pd.DataFrame(data)
print('---Simple_Data----')
print(df)

# Select singal columns
print('---Single_columns---')

name = df['Name']
print(name)

# select multple columns
print('---multple_columns---')

multy_columns = df[['Age','Salary']]
print(multy_columns)


