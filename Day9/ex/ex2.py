import numpy as np

# Generate a random 5x5 matrix
datataset  = np.random.randint(1,51,size=(5,5))

print("Original: \n",datataset)
# Filter values greater than > 25 and replace with 0
# datataset [ datataset > 25 ]=0
# print("Modified: \n",datataset)


#caculate summary stats
print("Mean: ",np.mean(datataset))
print("Max: ",np.max(datataset))
print("Min: ",np.min(datataset))
print("Sum: ",np.sum(datataset))
print("Standard Deviation: ",np.std(datataset))