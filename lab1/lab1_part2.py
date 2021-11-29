import random

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from src.rotate import randomRotate


if __name__ == '__main__':
    origin = [2 * random.random() - 1 for i in range(3)]
    rotatedV = randomRotate(origin)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Axis Lines
    lengthAxis = 2
    ax.plot([0, lengthAxis], [0, 0], [0, 0], color="red")
    ax.plot([0, 0], [0, lengthAxis], [0, 0], color="green")
    ax.plot([0, 0], [0, 0], [0, lengthAxis], color="blue")

    # Vectors
    ax.plot([0, origin[0]], [0, origin[1]], [0, origin[2]], linestyle="dashed", color="black")
    ax.plot([0, rotatedV[0]], [0, rotatedV[1]], [0, rotatedV[2]], linestyle="dotted", color="black")

    # Point of vector origin and text coord
    ax.scatter(origin[0], origin[1], origin[2], c='red', s=50)
    ax.text(origin[0], origin[1], origin[2],
            "(" + str(round(origin[0], 3)) + ", " + str(round(origin[1], 3)) + ", " + str(round(origin[2], 3)) + ")",
            size=10, zorder=1, color='k')

    # Point of vector rotatedV and text coord
    ax.scatter(rotatedV[0], rotatedV[1], rotatedV[2], c='blue', s=50)
    ax.text(rotatedV[0], rotatedV[1], rotatedV[2],
            "(" + str(round(rotatedV[0], 3)) + ", " + str(round(rotatedV[1], 3)) + ", " + str(round(rotatedV[2], 3)) + ")",
            size=10, zorder=1, color='k')

    ax.grid(False)
    ax.set_xlabel('$X$', fontsize=20)
    ax.set_ylabel('$Y$', fontsize=20)
    ax.set_zlabel('$Z$', fontsize=20)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='major', length=10, width=2)
    ax.tick_params(which='minor', length=5, width=1)
    plt.show()
