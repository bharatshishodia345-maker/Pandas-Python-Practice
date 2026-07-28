'''
Remove column using drop function
frist remove single column df.drop(coloumn = ['column name], inplace = True)                        
second remove multple column df.drop(coloumn = ['column name','second column name'], inplace = True)                        

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

# remove single column
df.drop(columns=['Performance_Score'], inplace=True)
print('---After removing column---')
print(df)

# multple column remove 
df.drop(columns=['Salary', 'Age'], inplace= True)
print('---After remove multple column---')
print(df)
