import math

from src.quaternion import Quaternion
from src.printers import printQuaternion

if __name__ == '__main__':
    a5 = Quaternion(-0.4161, [0.3523, -0.3074, 0.7800])
    R = a5.toRotateMatrix()
    printQuaternion(a5)
    print(R)
