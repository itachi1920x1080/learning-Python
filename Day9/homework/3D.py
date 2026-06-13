import numpy as np
# Create a 3D array(2 blocks , 3row and 4 column) with random values
array_3d = np.random.randint(2,3,4)

print("3D Array : \n",array_3d)
print("Shape of 3D array : \n",array_3d.shape)

mean_axis0 = np.mean(array_3d,axis=0)

max_axis2 = np.max(array_3d,axis=2)

print("Mean along axis 0 : \n",mean_axis0)
print("Mean along axis 2 : \n",max_axis2)