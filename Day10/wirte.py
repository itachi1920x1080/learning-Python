import pandas as pd
import os

# 1️⃣ User input
name  = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")

new_data = {
    "Name": [name],
    "Age": [age],
    "Gender": [gender]
}

new_df = pd.DataFrame(new_data)

# 2️⃣ Check if CSV exists
if os.path.exists("pandas.csv"):
    df = pd.read_csv("pandas.csv")
    # 3️⃣ Append new row
    df = pd.concat([df, new_df], ignore_index=True)
else:
    df = new_df

# 4️⃣ Add ID column starting from 1
df['ID'] = range(1, len(df)+1)

# 5️⃣ Save back to CSV
df.to_csv("pandas.csv", index=False)

# 6️⃣ Show result
print(df)
