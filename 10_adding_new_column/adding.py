'''
Adding new column 
frist access column name 
second using insert dunction
'''

import pandas as pd

data = {
    'Name': ['Bharat', 'Tarun', 'Ayush', 'Sunil', 'Anuj', 'Krrish'],
    'Age': [20, 19, 21, 23, 22, 18],
    'Salary': [51000, 45000, 35000, 40000, 52000, 55000],
    'Performance_Score': [90, 92, 85, 75, 88, 79]
}

df = pd.DataFrame(data)
print('---Simple_Data---')
print(df)

# Adding new column 
df['Bonus'] = df['Salary'] * 0.1
print('---Adding_New_Column(Bonus)---')
print(df)

# Add new column Using Insert function
#df.insert(loc, column_name,some_data)

df.insert(0, 'Employ_Id', [10,20,30,40,50,60])
print('---Adding_New_column_using_insert_function(Employ_Id)---')
print(df,)




