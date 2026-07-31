'''
Fill the value throw interpolate 
'''
import pandas as pd

data = {
            'Time':[20,30,40,50,60],
            'Complaxity':[1,None,3,None,5]   
}

df = pd.DataFrame(data)

print('---Before_Interpolate---')
print(df)

#Interpolate function
df['Complaxity'] = df['Complaxity'].interpolate(method='linear')
print('---After_interpolate---')
print(df)
