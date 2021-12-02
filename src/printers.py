from .quaternion import Quaternion


def printQuaternion(q: Quaternion):
    print("~~~~~")
    print("Scalar: ", q.scalar)
    print("Vector:", q.vector)
    print("Is Unit: ", q.isUnit())
    print("~~~~~")