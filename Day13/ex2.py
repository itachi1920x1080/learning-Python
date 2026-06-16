from matplotlib.scale import scale_factory
import numpy as np 
import matplotlib.pyplot as plt 
from  scipy.stats import norm ,binom ,poisson

x = np.linspace(-4,4,100)
y =norm.pdf(x,loc=0,scale=1)
plt.plot(x,y,label="Gaussian Distribution")
plt.title("Gaussian Distribution")
plt.show()

# binomial  Distribution
n,p = 10,0.5
x=np.arange(0,n+1)
y=binom.pmf(x,n,p)
plt.bar(x,y,label="Binomial Distribution")
# plt.plot(x,y,label="Binomial Distribution")
plt.title("Binomial Distribution")
plt.show()


# poisson Distribution

lam = 3
x = np.arange(0,10)
y = poisson.pmf(x,lam)
plt.bar(x,y,label="Poisson Distribution")
plt.title("Poisson Distribution")
plt.xlabel("Number of occurences")
plt.ylabel("Probability of occurences")
plt.show()