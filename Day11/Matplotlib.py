import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
data = np.random.rand(5,5)
# sns.heatmap(data,annot=True,cmap="coolwarm")
# plt.title("Heatmap")
sns.pairplot(data=pd.DataFrame(data,columns=["A","B","C","D","E"]))
plt.show()


# # basic plot
# x = [1,2,3,4]
# y=[10,20,30,25]
# plt.plot(x,y)
# plt.show()

# line plot: trend

# plt.plot([1,2,3],[10,20,30],label = "Trend",marker="o",linestyle="--",color="black")
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.show()


# bar chart: bars

# categores=["A","B","C","D"]
# values = [10,15,7,12]
# plt.bar(categores,values)
# plt.title("Bar Chart")
# plt.show()


# Histogram : Buckets

# data = [1,2,2,3,3,3,4,4,4,4]
# plt.hist(data,bins=4,color="green",edgecolor="black")
# plt.title("Histogram")
# plt.show()



# Scatter Plot : Points

# x = [1,2,3,4,5]
# y= [10,20,15,30,45]
# plt.scatter(x,y,color="red")

# plt.title("Scatter Plot")
# plt.show()


