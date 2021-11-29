import sympy as sy
import numpy as np

from src.forwardkinematick import rotateFromTransform


def jacobiLinear(transform, args: dict):
    argNames = list(args.keys())
    return np.array(
        [[sy.diff(transform.row(i).col(3)[0], argNames[j]).subs(args).n() for j in range(len(args))] for i in
         range(3)], dtype='float')


def linearSpeed(transform, args: dict, delta: list):
    yak = jacobiLinear(transform, args)
    return np.dot(yak, np.array(delta).T)


def jacobiAngle(frames, args: dict):
    return np.array([np.array(rotateFromTransform(frames[j]).evalf(subs=args).col(2)) for j in range(len(frames) - 1)],
                    dtype='float').T


def angleSpeed(frames, args: dict, delta: list):
    yak = jacobiAngle(frames, args)
    return np.dot(yak, np.array(delta).T).T
