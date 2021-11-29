import math

import numpy as np
import sympy as sy
from src.support_function import templateDevidChart
from  src.printers import printNumpyMatrix

r0, a0, d0, theta0 = sy.symbols('r0'), sy.symbols('a0'), sy.symbols('d0'), sy.symbols('theta0')
r1, a1, d1, theta1 = sy.symbols('r1'), sy.symbols('a1'), sy.symbols('d1'), sy.symbols('theta1')
r2, a2, d2, theta2 = sy.symbols('r2'), sy.symbols('a2'), sy.symbols('d2'), sy.symbols('theta2')
r3, a3, d3, theta3 = sy.symbols('r3'), sy.symbols('a3'), sy.symbols('d3'), sy.symbols('theta3')
r4, a4, d4, theta4 = sy.symbols('r4'), sy.symbols('a4'), sy.symbols('d4'), sy.symbols('theta4')

rSymbols = [r0, r1, r2, r3, r4]
aSymbols = [a0, a1, a2, a3, a4]
dSymbols = [d0, d1, d2, d3, d4]
thetaSymbols = [theta0, theta1, theta2, theta3, theta4]

m0 = templateDevidChart(r0, a0, d0, theta0)
m1 = templateDevidChart(r1, a1, d1, theta1)
m2 = templateDevidChart(r2, a2, d2, theta2)
m3 = templateDevidChart(r3, a3, d3, theta3)
m4 = templateDevidChart(r4, a4, d4, theta4)

matrices = [m0, m1, m2, m3, m4]

r = [0, 5.75, 7.375, 0, 0]
alpha = [-math.pi / 2, 0, 0, -math.pi / 2, 0]
d = [3, 0, 0, 0, 4.125]

e = 1.125

if __name__ == '__main__':
    sy.init_printing(use_unicode=True)
    # PARAMS
    thetas = [math.pi, math.pi / 2, math.pi / 2, -math.pi / 2, -math.pi / 6]
    #thetas = [0, 0, 0, 0, 0]
    g = 2

    # ------------
    point1 = sy.Matrix([0, 0, -e, 1])
    point2 = sy.Matrix([g/2, 0, -e, 1])
    point3 = sy.Matrix([-g/2, 0, -e, 1])
    point4 = sy.Matrix([g / 2, 0, 0, 1])
    point5 = sy.Matrix([-g / 2, 0, 0, 1])

    thetas[1] -= math.pi / 2
    thetas[2] += math.pi / 2
    thetas[3] -= math.pi / 2

    A1 = m0.evalf(subs={rSymbols[0]: r[0], aSymbols[0]: alpha[0],
                        dSymbols[0]: d[0], thetaSymbols[0]: thetas[0]})
    A2 = m1.evalf(subs={rSymbols[1]: r[1], aSymbols[1]: alpha[1],
                        dSymbols[1]: d[1], thetaSymbols[1]: thetas[1]})
    A3 = m2.evalf(subs={rSymbols[2]: r[2], aSymbols[2]: alpha[2],
                        dSymbols[2]: d[2], thetaSymbols[2]: thetas[2]})
    A4 = m3.evalf(subs={rSymbols[3]: r[3], aSymbols[3]: alpha[3],
                        dSymbols[3]: d[3], thetaSymbols[3]: thetas[3]})
    A5 = m4.evalf(subs={rSymbols[4]: r[4], aSymbols[4]: alpha[4],
                        dSymbols[4]: d[4], thetaSymbols[4]: thetas[4]})

    link_1 = A1
    link_2 = link_1 * A2
    link_3 = link_2 * A3
    link_4 = link_3 * A4
    link_5 = link_4 * A5

    print([0, 0, 0])
    print([round(link_1.row(i).col(3)[0], 3) for i in range(3)])
    print([round(link_2.row(i).col(3)[0], 3) for i in range(3)])
    print([round(link_3.row(i).col(3)[0], 3) for i in range(3)])
    print([round(link_4.row(i).col(3)[0], 3) for i in range(3)])
    print([round(link_5.row(i).col(3)[0], 3) for i in range(3)])

    point1 = link_5 * point1
    point2 = link_5 * point2
    point3 = link_5 * point3
    point4 = link_5 * point4
    point5 = link_5 * point5

    print("POINTS")
    print([round(point1.row(i).col(0)[0], 3) for i in range(3)])
    print([round(point2.row(i).col(0)[0], 3) for i in range(3)])
    print([round(point3.row(i).col(0)[0], 3) for i in range(3)])
    print([round(point4.row(i).col(0)[0], 3) for i in range(3)])
    print([round(point5.row(i).col(0)[0], 3) for i in range(3)])

    print(link_5)
    printNumpyMatrix(np.array(link_5).astype(np.float64))
