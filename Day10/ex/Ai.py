import pandas as pd

# តារាងទី១ (ខាងឆ្វេង)
df_left = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

# តារាងទី២ (ខាងស្តាំ)
df_right = pd.DataFrame({
    'ID': [2, 3, 4],
    'Score': [85, 90, 75]
})

print("Inner Merge (យកតែ ID 2 និង 3 ដែលមានសងខាង):")
inner_merge = pd.merge(df_left, df_right, on='ID', how='inner')
print(inner_merge)
print("-" * 30)

print("Left Merge (រក្សា ID 1, 2, 3 ពីតារាងឆ្វេង):")
left_merge = pd.merge(df_left, df_right, on='ID', how='left')
print(left_merge)
print("-" * 30)

print("Outer Merge (យកទាំងអស់ ID 1, 2, 3, 4):")
outer_merge = pd.merge(df_left, df_right, on='ID', how='outer')
print(outer_merge)