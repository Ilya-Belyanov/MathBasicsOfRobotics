

def loadMatrix(path):
    matrix = list()
    with open(path) as file:
        lines = file.readlines()
    for line in lines:
        matrix.append(list(map(float, line.split(","))))
    return matrix
