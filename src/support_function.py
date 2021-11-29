import math
import numpy as np
import sympy as sy
from src.quaternion import Quaternion


def toNumpy(matrix):
    return np.array(matrix).astype(np.float64)


def rotateMatrixToAxisAndAngle(r):
    theta = math.acos((np.trace(r) - 1) / 2)
    if round(theta, 5) == 0:
        return theta, np.array([None, None, None]), None
    if math.pi - 0.001 <= round(theta, 5) <= math.pi + 0.001:
        wx = math.sqrt((r[0][0] + 1) / 2)
        wy = math.sqrt((r[1][1] + 1) / 2) if wx == 0 else r[0][1] / (2 * wx)
        if wx != 0:
            wz = r[0][2] / (2 * wx)
        elif wy != 0:
            wz = r[1][2] / (2 * wy)
        else:
            wz = math.sqrt((r[2][2] + 1) / 2)
        w = np.array([wx, wy, wz])
        return theta, w, -1 * w
    w = np.array([[r[2][1] - r[1][2]],
                  [r[0][2] - r[2][0]],
                  [r[1][0] - r[0][1]]])
    w = w/(2 * math.sin(theta))
    return theta, w, None


def nextQ(q0: Quaternion, q1: Quaternion, theta: float, t: int):
    firstPart = math.sin((1 - t) * theta) / math.sin(theta)
    secondPart = math.sin(t * theta) / math.sin(theta)
    return q0.multiToScalar(firstPart) + q1.multiToScalar(secondPart)


def quatSlerp(q0: Quaternion, q1: Quaternion, step: int = 3):
    cosTheta = q0.scalarMulti(q1)
    theta = math.acos(cosTheta)
    if theta > math.pi:
        theta -= 2 * math.pi
    quaternions = list()
    tList = [i / step for i in range(step + 1)]
    for t in tList:
        quaternions.append(nextQ(q0, q1, theta, t))
    return quaternions


def templateDevidChart(r, a, d, theta):
    m = sy.Matrix([[sy.cos(theta), -1 * sy.sin(theta) * sy.cos(a), sy.sin(theta) * sy.sin(a), r * sy.cos(theta)],
                   [sy.sin(theta), sy.cos(theta) * sy.cos(a), -1 * sy.cos(theta) * sy.sin(a), r * sy.sin(theta)],
                   [0, sy.sin(a), sy.cos(a), d],
                   [0, 0, 0, 1]])
    return m
