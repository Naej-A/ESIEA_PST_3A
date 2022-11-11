import numpy as np
import random

if __name__ == '__main__':

    x = 100
    y = 100
    z = 3

    data = np.zeros((z, y, x))
    for i in range (x):
        for j in range(y):
            data[0, j, i] = 1
    for i in range (x):
        for j in range(y):
            data[1, j, i] = random.randint(0,1)
    for i in range (x):
        for j in range(y):
            if data[1, j, i] == 1:
                data[2, j, i] = random.randint(0,1)
            else:
                data[2, j, i] = 0

    print(data[::])