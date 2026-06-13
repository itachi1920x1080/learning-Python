import pandas as pd
import numpy as np

data ={
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 35, 40, 45],
    'City': ['New York', None, 'Chicago', 'Houston', 'Phoenix']
}

df=pd.DataFrame(data)


print("Original DataFrame:\n", df)
# របៀបលុប Column 'City'
df_dropped =df.drop('City', axis=1)
print("\nDataFrame after dropping 'City' column:\n", df_dropped)

# របៀបលុប Row ដែលមាន NaN
df_dropped_rows_NaN = df.dropna()
print("\nDataFrame after dropping rows with NaN values:\n", df_dropped_rows_NaN)
# របៀបលុប Row ដែលមាន NaN នៅក្នុង Column 'Age'
df_dropped_rows_age_NaN = df.dropna(subset=['Age'])
print("\nDataFrame after dropping rows with NaN values in 'Age' column:\n", df_dropped_rows_age_NaN)




df["City"]=df["City"].fillna("Unknown")
print("\nDataFrame after filling NaN values in 'City' column with 'Unknown':\n", df)