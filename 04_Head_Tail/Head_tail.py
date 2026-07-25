# Display 10 row frist and last using Head() and Tail() function

import pandas as pd

df = pd.read_excel('04_head_tail\College.xlsx')

print('Display 10 row of frist')
print(df.head())

print('Display 10 row of last ')
print(df.tail())
