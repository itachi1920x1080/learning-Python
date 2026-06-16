# def bayes_throrm(prior,likelihood ,evidence):
#     return (likelihood*prior)/evidence

from numpy.random import poisson
import numpy as np 
import matplotlib.pyplot as plt 


# mu , sigma = 0,1
# x = np.linspace(-4,4,100)
# y = (1/(np.sqrt(2*np.pi*sigma**2)))* np.exp(-0.5*((x-mu)/sigma)**2)

# plt.plot(x,y)
# plt.title('Gaussian distribution')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.show()



# p = 0.6
# plt.bar([0.1],[1-p,p],color=["red"])
# plt.title("Brenoulli Distribution")
# plt.xticks([0,1],labels=["0(failure)","1(success)"])
# plt.show()


# from scipy.stats import binom 
# n,p=10,0.5
# x = np.arange(0,n+1)
# y=binom.pmf(x,n,p)
# plt.bar(x,y)
# plt.title("Binomial Distribution")
# plt.xlabel("Number of successes")
# plt.ylabel("Probability of successes")
# plt.show()

from scipy.stats import poisson

lam = 3
x = np .arange(0,10)
y = poisson.pmf(x,lam)
plt.bar(x,y)
plt.title("Poisson Distribution")
plt.xlabel("Number of occ")
plt.show()