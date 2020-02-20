import random
from math import *
import matplotlib.pyplot as plt

def plot():
    X = [0]
    Y = [0]
    
    for n in range(100000):
        r = random.randint(0, 2)
        a = r/3*2*pi
        px = sin(a)
        py = cos(a)
        x = (px + Y[n-1])
        y = (py + X[n-1])
        X.append(x)
        Y.append(y)

    plt.figure(figsize = [10,20])
    plt.scatter(X, Y, marker = '.', s = 0.01)
    plt.show()

plot()
