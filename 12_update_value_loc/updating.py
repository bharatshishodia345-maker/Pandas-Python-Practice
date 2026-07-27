'''
Update value using loc function like employ salary is 50000 and you change in 55000 
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

#Using loc function and update the salary of frist employ
df.loc[0,'Salary'] = 55000
print('---Update_the_frist_employ_salary---')
print(df)