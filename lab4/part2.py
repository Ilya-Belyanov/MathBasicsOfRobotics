import math

import numpy as np


def getParameters(x, y, z, rotate):
    theta1 = np.arctan2(float(rotate[1][0]), float(rotate[0][0]))
    theta3 = np.arctan2(float(rotate[2][2]), -float(rotate[2][1]))
    d2 = -(z - 10 - 5 * math.sin(theta3)) / (math.sqrt(2) / 2)
    return theta1, theta3, d2
