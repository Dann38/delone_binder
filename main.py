import matplotlib.pyplot as plt

from delone_binder import DeloneBinder, Node

delone_binder = DeloneBinder()
points = [Node(1, 2), Node(3, 5), Node(6, 3), Node(2, 6), Node(3, 9)]

edges, triangles = delone_binder.bind(points)

for edge in edges:
    x, y = edge.get_lines()
    plt.plot(x, y, "b")
    plt.plot(x, y, "ro")

plt.show()
