import pandas as pd
#load dataset
df = pd.read_csv("dd.csv")

#expore stucure
print("First 5 rows : \n",df.head())

print("Last 5 rows : \n",df.tail())

print("Info : \n",df.info())

print("Statistics : \n",df.describe())


select_columns = df[["Name", "Age"]]
print("My selected Columns : \n ",select_columns)
# filtered_rows =df [(df["Age"]>20) & (df["Age"]<30),df["Name"]]
filtered_rows = df.loc[(df["Age"] > 20) & (df["Age"] < 30), ["Name", "Age"]]

print("Filtered Rows : \n",filtered_rows)