import random

import numpy as np


def x_rotation(vector, theta):
    """Rotates 3-D vector around x-axis"""
    R = np.array([[1, 0, 0],
                  [0, np.cos(theta), -np.sin(theta)],
                  [0, np.sin(theta), np.cos(theta)]])
    return np.dot(R, vector)


def y_rotation(vector, theta):
    """Rotates 3-D vector around y-axis"""
    R = np.array([[np.cos(theta), 0, np.sin(theta)],
                  [0, 1, 0],
                  [-np.sin(theta), 0, np.cos(theta)]])
    return np.dot(R, vector)


def z_rotation(vector, theta):
    """Rotates 3-D vector around z-axis"""
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])
    return np.dot(R, vector)


def randomRotate(vector):
    x = random.randint(int(-np.pi * 100), int(np.pi * 100)) / 100
    y = random.randint(int(-np.pi * 100), int(np.pi * 100)) / 100
    z = random.randint(int(-np.pi * 100), int(np.pi * 100)) / 100
    return z_rotation(y_rotation(x_rotation(vector, x), y), z)