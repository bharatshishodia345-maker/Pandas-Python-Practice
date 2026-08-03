# sort value using pnadas function sort_value()

import pandas as pd

data = {
    'Name': ['Bharat','Tarun','Ayush', 'Anuj','Adatiya' ],
    'Age': [20,19,22,18,17],
    'Salary': [20000,30000,60000,10000,15000],
}

df = pd.DataFrame(data)
print('---Simple_data(Before_using_shorting_function)---')
print(df)

# Short_value()
df.sort_values(by='Age', ascending=True, inplace=True)
print('---Sort_data(After_using_sort_value_function)---')
print(df)