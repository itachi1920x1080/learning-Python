import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

data = pd .read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
del data ['species']

# Calculate correlation matrix

correlation_matix = data.corr()

# Create heatmap
sns.heatmap(correlation_matix,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")

plt.show()