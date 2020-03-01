import random
from math import *
import numpy as np
import matplotlib.pyplot as plt

def plot(k):
    X1 = [0]
    Y1 = [0]
    
    for n in range(100000):
        r = random.randint(0, k-1)
        a = r/k*2*pi
        px = sin(a)
        py = cos(a)
        x = (px + Y1[n-1])/(k-1)
        y = (py + X1[n-1])/(k-1)
        X1.append(x)
        Y1.append(y)
        
    #####

    X2 = [0]
    Y2 = [0]
    
    for n in range(100000):
        r = random.randint(0, k-1)
        a = r/k*2*pi
        px = sin(a)
        py = cos(a)
        x = (px + X2[n-1])/(k-1)
        y = (py + Y2[n-1])/(k-1)
        X2.append(x)
        Y2.append(y)

    plt.figure(figsize = [10,20])
    plt.scatter(X1, Y1, marker = '.', s = 0.01)
    plt.scatter(X2, Y2, marker = '.', s = 0.01)
    plt.show()

for i in range(3, 20):
    plot(i)
