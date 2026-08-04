# merge data

import pandas as pd 

df_custumer = pd.DataFrame({
    'CoustumerID':[1,2,3,5],
    'Name':['Bharat','Anuj','Tarun','Ayush']
})

df_order = pd.DataFrame({
    'CoustumerID':[1,2,6],
    'Oreder_amount':[200,250,300]
})

df = pd.merge(df_custumer, df_order, on='CoustumerID', how='inner')
print('Inner-join')
print(df)
