import matplotlib.pyplot as plt
from delone_binder.delone_binder import Node, Edge, Triangle, DeloneBinder

my_coordinates = [(1, 0), (0, 1), (2, 5), (1, 2), (0.75, 2), (1.25, 2), (0.5, 1)] #, (3, 5)
coordinates = [Node(*my_coordinate) for my_coordinate in my_coordinates]

delone_binder = DeloneBinder()
edges = delone_binder.bind(coordinates)

for edge in edges:
    x, y = edge.get_line()
    plt.plot(x, y, "k")

plt.show()