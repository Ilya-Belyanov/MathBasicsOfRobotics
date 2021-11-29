from .quaternion import Quaternion


def printQuaternion(q: Quaternion):
    print("~~~~~")
    print("Scalar: ", q.scalar)
    print("Vector:", q.vector)
    print("Is Unit: ", q.isUnit())
    print("~~~~~")


def printNumpyMatrix(m):
    print("~~~~~")
    if len(m.shape) == 1:
        for j in range(m.shape[0]):
            print([round(m[j], 2)])
    else:
        for j in range(m.shape[0]):
            print([round(m[j][i], 2) for i in range(m.shape[1])])
    print("~~~~~")
