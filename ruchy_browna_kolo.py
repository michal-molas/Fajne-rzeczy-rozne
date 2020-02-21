import random
from math import *
import matplotlib.pyplot as plt

def plot(k):
    X = [0]
    Y = [0]
    for n in range(100000):
        r = random.random()
        a = r*2*pi
        px = sin(a)
        py = cos(a)
        x = (px + X[n-1])/k
        y = (py + Y[n-1])/k
        X.append(x)
        Y.append(y)

    plt.figure(figsize = [10,20])
    plt.scatter(X, Y, marker = '.',s=0.01)
    plt.show()

plot(0.9999)
plot(1.002)
