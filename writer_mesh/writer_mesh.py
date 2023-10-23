import matplotlib.pyplot as plt
from delone_binder.delone_binder import Node, Edge, Triangle, DeloneBinder

my_coordinates = [(5, 6), (6, 5)] #, (3, 5)
coordinates = [Node(*my_coordinate) for my_coordinate in my_coordinates]


delone_binder = DeloneBinder()
edges = delone_binder.bind(coordinates, [Node(7, 7), Node(0, 7),  Node(0, 0), Node(7, 0)])

for edge in edges:
    x, y = edge.get_line()
    plt.plot(x, y, "k")

plt.show()