import numpy as np
def gradient_descent (x,y,theta,learning_reate,itetations):
    m = len (y)
    for _ in range (itetations):
        predictions = np.dot(x,theta)
        error = predictions-y
        gradients = (1/m)*np.dot(x.T,error)
        theta -= learning_reate* gradients
    return theta
x  = np.array([[1,1],[1,2],[1,3]])
y = np.array([[2],[2.5],[3.5]])
theta = np.array([[0.1],[0.1]])
learning_reate = 0.01 
itetations = 1000

theta_final =gradient_descent(x,y,theta,learning_reate,itetations)
print('final theta (weights):', theta_final)
