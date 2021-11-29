import numpy as np

from src.support_function import rotateMatrixToAxisAndAngle

if __name__ == '__main__':
    R0 = np.array([[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]])

    R1 = np.array([[-1, 0, 0],
                  [0, 1, 0],
                  [0, 0, -1]])

    R2 = np.array([[-0.5092, -0.0269, 0.8602],
                  [0.7973, 0.3617, 0.4833],
                  [-0.3242, 0.9319, -0.1628]])

    print(rotateMatrixToAxisAndAngle(R0))
    print(rotateMatrixToAxisAndAngle(R1))
    print(rotateMatrixToAxisAndAngle(R2))
