import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20,20,100) #(starting index,ending index,no. of elements)

def func(x):
    y=[]
    for elem in x:
        result = 1-(elem**2)/2
        y.append(result)
    return y

y = func(x)
plt.plot(x,y)
plt.show()

print("I am here")