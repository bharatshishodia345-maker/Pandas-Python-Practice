# concat data

import pandas as pd 

df_resion_1 = pd.DataFrame({
    'CoustumerID':[1,2,3],
    'Name':['Bharat','Tarun','Anuj']
})

df_resion_2 = pd.DataFrame({
    'CoustumerID':[4,5,6],
    'Name':['Ayush','Nitin','Vijay']
})

df = pd.concat([df_resion_1,df_resion_2],axis=0, ignore_index=True)

print(df)