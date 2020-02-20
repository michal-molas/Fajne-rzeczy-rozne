import random
from math import *
import matplotlib.pyplot as plt

def check_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, round(sqrt(n))+1):
            if n % i == 0:
                return False
        return True

def plot():
    # 0 - up, 1 - right, 2 - down, 3 - left
    X = []
    Y = []
    x = 0
    y = 0
    direction = 0
    steps = 0
    curr_step = 0
    for i in range(1, 10000):
        curr_step += 1
        if curr_step > steps:
            curr_step = 1
            if direction % 2 != 0:
                steps += 1
            direction+=1
            direction%=4
        if direction == 0:
            y+=1
        elif direction == 1:
            x+=1
        elif direction == 2:
            y-=1
        else:
            x-=1
        is_prime = check_prime(i)
        if is_prime:
            X.append(x)
            Y.append(y)

    plt.figure(figsize = [10,20])
    plt.scatter(X, Y, marker = '.',s=10)
    plt.show()

plot()
