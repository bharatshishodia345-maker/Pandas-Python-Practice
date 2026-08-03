# Sort data in multple column togeather

import pandas as pd

data = {
    'Name': ['Bharat','Tarun','Ayush', 'Anuj','Adatiya' ],
    'Age': [20,19,22,18,17],
    'Salary': [20000,30000,60000,10000,15000],
}

df = pd.DataFrame(data)
print('---Simple_data(Before_using_shorting_function)---')
print(df)

# Sort_multple columns
df.sort_values(by=['Age','Salary'], ascending=[True,True], inplace=True)
print(df)