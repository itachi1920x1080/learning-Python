import pandas as pd

data={
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Gender': ['Female', 'Male', '    Male']
}

df_people = pd.DataFrame(data)
df_people['totalAge']=df_people['Age'].sum()
df_people.to_csv("people.csv", index=False)
print("Dataframe : \n",df_people)