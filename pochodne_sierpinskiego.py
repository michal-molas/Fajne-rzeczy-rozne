import random
from math import *
import numpy as np
import matplotlib.pyplot as plt

def plot():
    #####
    X1 = [0]
    Y1 = [0]
    
    for n in range(100000):
        r = random.randint(0, 2)
        a = r/3*2*pi
        px = sin(a)
        py = cos(a)
        x = (px - X1[n-1])/2
        y = (py - Y1[n-1])/2
        X1.append(x)
        Y1.append(y)
        
    ######
    X2 = [0]
    Y2 = [0]

    for n in range(100000):
        r = random.randint(0, 2)
        a = -r/3*2*pi
        px = sin(a)
        py = cos(a)
        x = (px + X2[n-1])/2
        y = (py + Y2[n-1])/2
        X2.append(x)
        Y2.append(y)

    ######
    X3 = [0]
    Y3 = [0]
    
    for n in range(100000):
        r = random.randint(0, 2)
        a = r/3*2*pi
        px = sin(a)
        py = cos(a)
        x = (px - abs(X3[n-1]))/2
        y = (py - abs(Y3[n-1]))/2
        X3.append(x)
        Y3.append(y)

    ######
    X4 = [0]
    Y4 = [0]
    
    for n in range(100000):
        r = random.randint(0, 2)
        a = r/3*2*pi
        px = sin(a)
        py = cos(a)
        x = abs(px - X4[n-1])/2
        y = abs(py - Y4[n-1])/2
        X4.append(x)
        Y4.append(y)

    ######
    X5 = [0]
    Y5 = [0]
    
    for n in range(100000):
        r = random.randint(0, 2)
        a = r/3*2*pi
        px = sin(a)
        py = cos(a)
        x = abs(px + X5[n-1])/2
        y = abs(py + Y5[n-1])/2
        X5.append(x)
        Y5.append(y)

    ######
    X6 = [0]
    Y6 = [0]
    
    for n in range(100000):
        r = random.randint(0, 2)
        a = r/3*2*pi
        px = sin(a)
        py = cos(a)
        x = (px + Y6[n-1])/2
        y = (py + X6[n-1])/2
        X6.append(x)
        Y6.append(y)

            
    plt.figure(figsize = [10,20])
    plt.scatter(X1, Y1, marker = '.', s = 0.01)
    plt.scatter(X2, Y2, marker = '.', s = 0.01)
    plt.scatter(X3, Y3, marker = '.', s = 0.01)
    plt.scatter(X4, Y4, marker = '.', s = 0.01)
    plt.scatter(X5, Y5, marker = '.', s = 0.01)
    plt.scatter(X6, Y6, marker = '.', s = 0.01)
    plt.show()

plot()
