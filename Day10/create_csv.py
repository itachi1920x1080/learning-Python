import pandas as pd

# Create correct CSV
data = {
    "Name": ["Tom", "Jack"],
    "Age": [28, 34],
    "Gender": ["Male", "Male"]
}

df = pd.DataFrame(data)

# Add ID column
df['ID'] = range(1, len(df)+1)

# Reorder columns so ID comes first
df = df[['ID','Name','Age','Gender']]

# Save to CSV
df.to_csv("pandas.csv", index=False)
print(df)
print("CSV created!")
