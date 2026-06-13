import pandas as pd
data={
    'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
    'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
    'Sales':[200,120,340,124,243,350]
}
df=pd.DataFrame(data)
# grouped = df.groupby('column_name') # groupby object
grouped = df.groupby('Company')
# print(grouped.sum())

# print(grouped['Sales'].mean())
# print(grouped['Sales'].agg(['sum','mean','std','min','max']))

# for name, group in grouped:
#     # print(name)
#     # print(group)
#     print(name,group['Sales'].mean())


pivot = df.pivot_table(
    values='Sales',
    index='Company',
    aggfunc='mean'
)

# print(pivot)


def range_fun(x):
    return x.max()-x.min()

print(df.groupby('Company')['Sales'].agg(range_fun))


print(df.groupby('Company')['Sales'].agg(['min','max']))