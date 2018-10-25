import numpy as np
import matplotlib.pyplot as plt


def sierpenski(x_s, y_s):
    rand = np.random.randint(1, 4)
    if rand == 1:
        (x_s, y_s) = (x_s / 2, y_s / 2)
    elif rand == 2:
        (x_s, y_s) = ((x_s + 1) / 2, y_s / 2)
    else:
        (x_s, y_s) = ((x_s + 1 / 2) / 2, (y_s + 1) / 2)
    return (x_s, y_s)
counter = 1
(x, y) = (1/2, 1/2)
xcoords = [1/2]
ycoords = [1/2]
while counter < 3:
    (x, y) = sierpenski(x, y)
    counter += 1
while counter < 100000:
    (x, y) = sierpenski(x, y)
    counter += 1
    xcoords.append(x)
    ycoords.append(y)
plt.scatter(xcoords, ycoords, marker=".", s=0.5, c="blue")
plt.show()
