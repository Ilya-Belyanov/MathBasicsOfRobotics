from math import pi

import numpy as np
import sympy as sy
from src.forwardkinematick import fkMatrix, fkFrames, transformMatrices
from src.printers import printNumpyMatrix
from src.speedkinematick import *

if __name__ == '__main__':
    sy.init_printing(use_unicode=True)
    params = [pi / 2, -pi / 2, pi / 2, pi / 3, pi / 2]
    speed_parameters = [0.1, 0.3, 0.2, -0.1, 0.6]
    theta1, theta2, theta3, theta4, theta5 = sy.symbols('theta1'), sy.symbols('theta2'), \
                                             sy.symbols('theta3'), sy.symbols('theta4'), sy.symbols('theta5')

    r = [0, 5.75, 7.375, 0, 0]
    alpha = [-pi / 2, 0, 0, -pi / 2, 0]
    d = [3, 0, 0, 0, 4.125]
    thetas = [theta1, theta2 - pi / 2, theta3 + pi / 2, theta4 - pi / 2, theta5]

    links = transformMatrices(d, r, thetas, alpha)

    fk_transform = fkMatrix(links)

    frames = fkFrames(links)

    linear_speed = linearSpeed(fk_transform, {theta1: params[0], theta2: params[1], theta3: params[2], theta4: params[3],
                                              theta5: params[4]}, speed_parameters)

    printNumpyMatrix(linear_speed)

    angle_speed = angleSpeed(frames, {theta1: params[0], theta2: params[1], theta3: params[2], theta4: params[3],
                                      theta5: params[4]}, speed_parameters)

    printNumpyMatrix(angle_speed)
