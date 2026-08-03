# group the data accoding his Age using pandas 


import pandas as pd 

data = {
    'Name': ['Bharat', 'Tarun', 'Ayush', 'Sunil', 'Anuj', 'Krrish'],
    'Age': [20, 20, 21, 21, 20, 21],
    'Salary': [51000, 45000, 35000, 40000, 52000, 55000],
    'Performance_Score': [90, 92, 85, 75, 88, 79]
}

df = pd.DataFrame(data)

group = df.groupby('Age') ['Salary'].sum()
print(group)