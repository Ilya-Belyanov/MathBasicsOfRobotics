import matplotlib.pyplot as plt

COLOR_BUFFER = ['r', 'g', 'blue', 'black']


def drawTriangles(*triangles):
    for i, triangles in enumerate(triangles):
        for edge in triangles.edges():
            plt.plot([edge[0].x, edge[1].x],
                     [edge[0].y, edge[1].y],
                     marker='o', color=COLOR_BUFFER[i % len(COLOR_BUFFER)])

    plt.show()
