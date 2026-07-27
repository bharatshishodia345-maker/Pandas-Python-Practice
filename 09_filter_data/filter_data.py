'''
Use condition 
Single condition is like Age > 20
multple condition is like Age > 20 & salary > 50000

'''

import pandas as pd 

data = {
    'Name': ['Bharat', 'Tarun', 'Ayush', 'Sunil', 'Anuj', 'Krrish'],
    'Age': [20, 19, 21, 23, 22, 18],
    'Salary': [51000, 45000, 35000, 40000, 52000, 55000],
    'Performance_Score': [90, 92, 85, 75, 88, 79]
}

df = pd.DataFrame(data)

# putup of single condition
high_salary = df[df['Salary'] > 50000]
print('---High_salary(salary > 50000)')
print(high_salary)

# putup of multple condition 
filtered_data = df[(df['Salary'] > 50000) & (df['Age'] > 20)]
print('---Filtered_data(using And operator)---')
print(filtered_data)


# putup the or operator
or_data = df[(df['Performance_Score'] > 90) | (df['Age'] > 20)]
print('---Filtered_data(Using or operator)---')
print(or_data)