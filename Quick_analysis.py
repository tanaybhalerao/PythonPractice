import pandas as pd
import numpy as np


input_file=

df=pd.ExcelFile(input_file,index=False, header=True).parse('GQV')
groups = df.groupby(["X_DT"])
mad = groups['GQV_BRD_HUL'].transform(lambda x: x.mad())
dif = groups['GQV_BRD_HUL'].transform(lambda x: np.abs(x - x.mean()))

df2 = df[dif > 2.5*mad]
print('Outliers: ')
print('\n')
print(df2)

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
cross_sec = list(df.select_dtypes(exclude=numerics).columns)
other_vars = list(df.select_dtypes(include=numerics).columns)
min_date = df.set_index('X_DT').index.min()
max_date = df.set_index('X_DT').index.max()
print('\n')
print("Cross Sections: ",cross_sec)
print("Measures: ",other_vars)
print("Columns:", df.shape[1])
print("Rows   :", df.shape[0])
print("Minimum Date: ",min_date)
print("Maximum Date: ",max_date)
print('\n')
print('Descriptive Statistics: ')
print(df.describe(include=numerics).round(decimals=3))
print('\n')
print('Correlation Measures: ')
print(df.corr(method='pearson'))



t=df[["X_DT"]]
t_df=pd.DataFrame(t)


df2=t_df.groupby(['X_DT']).value_counts().unstack()
df3=df2.reset_index()
df3["Difference"]=df3["X_DT"].diff()
print(df3)

