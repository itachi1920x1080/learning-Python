import numpy as np

# Array and scalars broadcasting
# arr = np.array([1,2,3,4])
# print(arr+10)
# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix)
# vetor = np.array([[1,0,1]])
# print(vetor)
# print(matrix+vetor)


# Array and aggregation function

# arr =  np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("Sum : ", np.sum(arr))
# print("Mean : ",np.mean(arr))
# print("Max : ",np.max(arr))
# print("Min : ",np.min(arr))
# print("Standard Deviation : ",np.std(arr))
# print("Sum along rows : ",np.sum(arr,axis=1))
# print("Sum along columns : ",np.sum(arr,axis=0))


# arr =  np.array([1,2,3,4,5,6])
# evens = arr[arr % 2 == 0]
# print("Evens : ",evens)

# arr[arr > 3 ] = 0
# print("Modified array : ",arr)

# np.random.seed(42)  # random seed is seed value used to generate random numbers
radom_array = np.random.rand(3,3)
print("Random Array  : \n",radom_array)
random_integers = np.random.randint(0,10,size=(3,3))
print("Random integers : \n",random_integers)
