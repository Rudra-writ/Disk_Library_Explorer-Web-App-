import pandas as pd
df = pd.read_excel('C:\\Users\\rudrawrit.majumdar.ADRFA\\Desktop\\systemcodes.xlsx') 
mylist = df['column1'].tolist()
mylist1 = list(set(mylist))
print(mylist1)
