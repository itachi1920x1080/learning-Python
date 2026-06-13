import pandas as pd
import numpy as np

df1= pd.DataFrame({
        'ID': [1, 2, 3, 4, 5],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        })

df2= pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Score': [85, 90, 95, 80, 75]
})




print("Dataset 1:",df1)
print("\nDataset 2:",df2)


merged = pd.merge(df2,df1,left_index=True,right_index=True)
print("Merged Dataset:\n",merged)

inner_merged = pd.merge(df1,df2,on='ID',how='inner')
print("Inner Merged Dataset:\n",inner_merged)


merged["Score_Total"]=(merged["Score"]/100)*100
print("Merged Dataset with Score Total:\n",merged)