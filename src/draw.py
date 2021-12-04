import matplotlib.pyplot as plt


def drawTriangles(*triangles):
    for triangles in triangles:
        for edge in triangles .edges():
            plt.plot([edge[0].coord()[0], edge[1].coord()[0]],
                     [edge[0].coord()[1], edge[1].coord()[1]],
                     marker='o')

    plt.show()
