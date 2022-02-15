import numpy as np
import copy

from robobase.quaternion import Quaternion

import matplotlib.pyplot as plt


COLOR_BUFFER = ['r', 'g', 'blue', 'black']


def drawTriangles(*triangles):
    for i, triangles in enumerate(triangles):
        for edge in triangles.edges():
            plt.plot([edge[0].x, edge[1].x],
                     [edge[0].y, edge[1].y],
                     marker='o', color=COLOR_BUFFER[i % len(COLOR_BUFFER)])

    plt.show()


def startAndEntToMap(input_map, start_coords, dest_coords):
    map_with_start_end = copy.deepcopy(input_map)
    map_with_start_end[start_coords[0]][start_coords[1]] = 5
    map_with_start_end[dest_coords[0]][dest_coords[1]] = 6
    return map_with_start_end


def routeToMap(input_map, route, color=7):
    map_with_all = copy.deepcopy(input_map)
    for r in range(1, len(route) - 1):
        input_map[route[r][0]][route[r][1]] = color
    return map_with_all


def loadMatrix(path):
    matrix = list()
    with open(path) as file:
        lines = file.readlines()
    for line in lines:
        matrix.append(list(map(float, line.split(","))))
    return matrix


def printQuaternion(q: Quaternion):
    print("~~~~~")
    print("Scalar: ", q.scalar)
    print("Vector:", q.vector)
    print("Is Unit: ", q.isUnit())
    print("~~~~~")


def toNumpy(matrix):
    return np.array(matrix).astype(np.float64)
