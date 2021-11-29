import math
import unittest

import numpy as np
import sympy as sy
from lab4.part1 import posAndRotate
from lab4.part2 import getParameters
from src.printers import printNumpyMatrix

th1Parameters = [0, math.pi]
th3Parameters = [0, math.pi/2]
d2Parameters = [5, -10]


class Test(unittest.TestCase):
    def test(self):
        for i in range(len(d2Parameters)):
            th1Param = th1Parameters[i]
            d2Param = d2Parameters[i]
            th3Param = th3Parameters[i]

            pos, R = posAndRotate(th1Param, th3Param, d2Param)
            theta1, theta3, d2 = getParameters(pos[-1][0], pos[-1][1], pos[-1][2], R)
            pos_ik, R_ik = posAndRotate(theta1, theta3, d2)

            print(f"TEST {i} with theta1 = {th1Param} and theta3 = {th3Param} and d2 = {d2Param}")
            print(f"IK: theta1 = {theta1} and theta3 = {theta3} and d2 = {d2}")
            print(f"Pos x = {round(pos[-1][0], 2)}, y = {round(pos[-1][1], 2)}, z = {round(pos[-1][2], 2)}")
            printNumpyMatrix(R)
            print(f"Pos_IK x = {round(pos_ik[-1][0], 2)}, y = {round(pos_ik[-1][1], 2)}, z = {round(pos_ik[-1][2], 2)}")
            printNumpyMatrix(R_ik)
            print()

            self.assertEqual(round(pos[-1][0], 2), round(pos_ik[-1][0], 2))
            self.assertEqual(round(pos[-1][1], 2), round(pos_ik[-1][1], 2))
            self.assertEqual(round(pos[-1][2], 2), round(pos_ik[-1][2], 2))


if __name__ == '__main__':
    unittest.main()
