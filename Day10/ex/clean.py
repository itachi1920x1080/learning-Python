import pandas as pd
import numpy as np

data ={
    "Name": ['Alice', 'Bob', 'Charlie', 'David', 'Eve','Frank'],
    "Age": [25, np.nan, 35, 40, 45,np.nan],
    "Salary": [50000, 60000, np.nan, 80000, 90000,np.nan],
    "City": ['New York', None, 'Chicago', 'Houston', 'Phoenix',None]
}

df=pd.DataFrame(data)
print("Original DataFrame:\n", df)
df["City"]=df["City"].fillna("Unknown")
print("\nDataFrame after filling NaN values in 'City' column with 'Unknown':\n", df)
df["Age"]=df["Age"].fillna(df["Age"].mean())
# print("\nDataFrame after filling NaN values in 'Age' column with mean:\n", df)
# df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
df["Salary"]=df["Salary"].interpolate()
print("\nDataFrame after filling NaN values in 'Salary' column with mean:\n", df)


df=df.rename(columns={"Name":"full_name"})
print("\nDataFrame after renaming 'Name' column to 'full_name':\n", df)