import math

import numpy as np

from src.forwardkinematics import ForwardKinematics
from robobase.dhmatrix import DHMatrix
from src.support import toNumpy


def positionsAndRotate(d: list, r: list, thetas: list, alpha: list, arg:dict):

    links = ForwardKinematics.links(d, r, thetas, alpha)
    frames = ForwardKinematics.frames(links)
    position = list([])
    for frame in frames:
        position.append(toNumpy(DHMatrix.pos(frame).evalf(subs=arg)).T.tolist()[0])
    return position, toNumpy(DHMatrix.rotate(frames[-1]).evalf(subs=arg))


def backKinematicsLab4(x, y, z, rotate):
    theta1 = np.arctan2(float(rotate[1][0]), float(rotate[0][0]))
    theta3 = np.arctan2(float(rotate[2][2]), -float(rotate[2][1]))
    d2 = -(z - 10 - 5 * math.sin(theta3)) / (math.sqrt(2) / 2)
    return theta1, theta3, d2
