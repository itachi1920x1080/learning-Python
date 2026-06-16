import numpy as np 
def predict (x,theta):
    return np.dt(x,theta)


def gradient_descent (x,y,theata,learing_rate ,interation):
    m=len(y)
    for _ in range(iteration):
        gradients = (1/m)* np.dot(x.T, (np.dot(x,theata)-y))
        theta -= learing_rate * gradients
        return theta 
def mean_squred_error(y_true ,y_pred):
    return np.mean((y_true - y_pred))

def r_squred(y_true,y_pred):
    sse = np.sum((y_true - y_pred)**2)
    sstot =np.sum((y_true - np.mean(y_true))**2)
    return 1-(sse/sstot)    
