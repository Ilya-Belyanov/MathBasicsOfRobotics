import math

import numpy as np
from src.quaternion import Quaternion
from src.quaternionfunctions import quatSlerp

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    a1 = Quaternion(-0.4161, [0.3523, -0.3074, 0.7800])
    a2 = Quaternion.fromAngleAndVector(3.5112, [-0.1457, 0.5976, -0.7884])
    a3 = Quaternion(1, [0, 0, 0])
    a4 = Quaternion(math.cos(math.pi/4), [math.sin(math.pi/4), 0, 0])

    quaternions = quatSlerp(a1, a2, 10)
    quaternions2 = quatSlerp(a3, a4, 10)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Axis Lines
    lengthAxis = 1
    ax.plot([0, lengthAxis], [0, 0], [0, 0], color="red")
    ax.plot([0, 0], [0, lengthAxis], [0, 0], color="green")
    ax.plot([0, 0], [0, 0], [0, lengthAxis], color="blue")

    for q in quaternions:
        ax.plot([0, q.x + q.scalar], [0, q.y + q.scalar], [0, q.z + q.scalar], color="black")
        ax.scatter(q.x + q.scalar, q.y + q.scalar, q.z + q.scalar, c='blue', s=10)

    for q in quaternions2:
        ax.plot([0, q.x + q.scalar], [0, q.y + q.scalar], [0, q.z + q.scalar], color="purple")
        ax.scatter(q.x + q.scalar, q.y + q.scalar, q.z + q.scalar, c='red', s=10)

    ax.view_init(elev=150., azim=55)
    ax.grid(False)
    ax.set_xlabel('$X$', fontsize=20)
    ax.set_ylabel('$Y$', fontsize=20)
    ax.set_zlabel('$Z$', fontsize=20)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='major', length=10, width=2)
    ax.tick_params(which='minor', length=5, width=1)
    plt.show()

