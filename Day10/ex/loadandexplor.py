import pandas as pd
# Load dataset
df= pd.read_csv("dd.csv")
print("First 5 rows : \n",df.head())# បង្ហាញជួរដេក ៥ ដំបូង
print("Last 5 rows : \n",df.tail())
print("Info : \n",df.info())# បង្ហាញព័ត៌មានលម្អិតពី Column និងប្រភេទបច្ចេកទេស (Data types)
print("Statistics : \n",df.describe())# បង្ហាញស្ថិតិសង្ខេប (មធ្យមភាគ, តម្លៃធំបំផុត...)


# ១. ជ្រើសរើសយកតែ Column ខ្លះ

subset = df[["Name", "Age"]]
filterwd_df = df[df["Age"] > 20]
print("My selected Columns : \n ",subset)
print("Filtered Rows : \n",filterwd_df)

# df_excel = pd.read_excel('ឈ្មោះឯកសាររបស់អ្នក.xlsx')
# df_excel = pd.read_excel("dd.xlsx")
# print("Excel Data : \n",df_excel.head())



