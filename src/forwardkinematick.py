import sympy as sy

from src.support_function import templateDevidChart


def posFromTransform(link: sy.Matrix) -> sy.Matrix:
    return sy.Matrix([link.row(j).col(3)[0] for j in range(3)])


def rotateFromTransform(link: sy.Matrix) -> sy.Matrix:
    return sy.Matrix([[link.row(j).col(i)[0] for i in range(3)] for j in range(3)])


def transformMatrices(d: list, r: list, thetas: list, alpha: list) -> list:
    return [templateDevidChart(r[i], alpha[i], d[i], thetas[i]) for i in range(len(d))]


def fkFrames(links: list) -> list:
    frames = list([sy.eye(4)])
    frames.append(links[0])
    for i in range(1, len(links)):
        frames.append(frames[-1] * links[i])
    return frames


def fkMatrix(links: list) -> sy.Matrix:
    fk = links[0]
    for i in range(1, len(links)):
        fk = fk * links[i]
    return fk
