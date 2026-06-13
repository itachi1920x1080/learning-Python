import pandas as pd
import csv

s = pd.Series([10,20,30],index = ['a','b','c'])
# # print(s)
# data  = {"Name ": ["Tom", "Jack", "Steve", "Ricky"],
#     "Age": [28,34,29,42],
#     "Gender": ["Male", "Male", "Male", "Male"]}

# name  = input("Enter your name: ")
# age = input("Enter your age: ")
# gender = input("Enter your gender: ")
# data = {
#     "Name ": [name],
#     "Age": [age],
#     "Gender": [gender]
# }

# df = pd.DataFrame(data)
# df.index = range(1, len(df) + 1)
# df['ID'] = range(1, len(df)+1)
# print(type(df))
# print(df)

df = pd.read_csv("pandas.csv")
df.to_csv("pandas.csv", index=False)
# ===== Viewing DataFrame =====

print(df)  
# បង្ហាញទិន្នន័យទាំងអស់ក្នុង DataFrame

# print(df.head())  
# បង្ហាញ 5 ជួរដំបូង

# print(df.tail(1))  
# បង្ហាញ 1 ជួរចុងក្រោយ

# print(df.info())  
# បង្ហាញព័ត៌មានអំពី DataFrame 
# (ចំនួនជួរ, column, data type, missing values)

# print(df.describe())  
# បង្ហាញស្ថិតិ (mean, min, max, std, count)

# seleting and filtering data

# print(df[["Name","Age"]])

# print(df[df["Age"] > 20])
# sytax:df.iloc[rows, columns]

# print(df.iloc[0])
# print(df.iloc[:, 1])
# print(df[df.iloc[:, 2] < 30])

# df.loc[row_labels, column_labels]
# print(df.loc[1])
# print(df.loc[1, ["Name", "Age"]])


# df = pd.read_csv("pandas.xlsx")
# print(df)