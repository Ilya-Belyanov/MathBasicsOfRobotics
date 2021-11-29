import math

import numpy as np
import sympy as sy
from src.support_function import templateDevidChart
from src.printers import printNumpyMatrix


def coords(link):
    return [round(link.row(j).col(3)[0], 3) for j in range(3)]


def posAndRotate(theta1, theta3, d2):
    d = [10, d2, 0, 5]
    r = [0, 0, 0, 0]
    thetas = [theta1, -math.pi / 2, -math.pi / 2 - math.pi / 4 + theta3, -math.pi / 2]
    alpha = [-math.pi / 2 - math.pi / 4, -math.pi / 2, -math.pi / 2, 0]

    rS, aS, dS, thetaS = sy.symbols('r'), sy.symbols('a'), sy.symbols('d'), sy.symbols('theta')

    links = list([templateDevidChart(rS, aS, dS, thetaS).evalf(subs={rS: r[0], aS: alpha[0], dS: d[0], thetaS: thetas[0]})])
    position = list([[0, 0, 0]])
    position.append(coords(links[-1]))

    for i in range(1, len(d)):
        m = templateDevidChart(rS, aS, dS, thetaS).evalf(subs={rS: r[i], aS: alpha[i], dS: d[i], thetaS: thetas[i]})
        links.append(links[-1] * m)
        position.append(coords(links[-1]))

    return position, np.array(links[-1]).astype(np.float64)[:3, :3]


if __name__ == '__main__':
    sy.init_printing(use_unicode=True)

    # PARAMS
    th1Param = math.pi
    d2Param = -10
    th3Param = math.pi / 2

    pos, R = posAndRotate(th1Param, th3Param, d2Param)

    for p in pos:
        print(p)

    print("R rotate")
    printNumpyMatrix(R)
