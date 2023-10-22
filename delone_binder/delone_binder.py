from typing import List, Tuple


class Node:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y


class Edge:
    def __init__(self, n1: Node, n2: Node, t1: "Triangle" = None, t2: "Triangle" = None):
        self.node1 = n1
        self.node2 = n2
        self.triangle1 = t1
        self.triangle2 = t2

    def get_line(self):
        return [self.node1.x, self.node2.x], [self.node1.y, self.node2.y]


class Triangle:
    def __init__(self, e1: Edge, e2: Edge, e3: Edge):
        self.edges = [e1, e2, e3]

    def is_contain(self, node: Node) -> bool:
        n1, n2, n3 = self.get_nodes()
        s0 = self.area_triangle([n1, n2, n3])
        s1 = self.area_triangle([n1, n2, node])
        s2 = self.area_triangle([n2, n3, node])
        s3 = self.area_triangle([n3, n1, node])
        print(s0, s1, s2, s3)
        return s1+s2+s3 <= s0


    def area_triangle(self, nodes: List[Node]) -> float:
        # шнуровка Гаусса
        s_1 = 0
        s_2 = 0
        node_prev = nodes[-1]
        for node in nodes:
            x, y = node.x, node.y
            x_prev, y_prev = node_prev.x, node_prev.y
            node_prev = node
            s_1 += y * x_prev
            s_2 += x * y_prev

        return abs((s_2 - s_1) / 2)


    def get_nodes(self) -> Tuple[Node, Node, Node]:
        n1 = self.edges[0].node1
        n2 = self.edges[0].node2
        n3 = self.edges[1].node1 if self.edges[1].node2 in [n1, n2] else self.edges[1].node2
        return n1, n2, n3

    def diff3(self, node: Node) -> Tuple["Triangle", "Triangle", "Triangle", Edge, Edge, Edge]:
        nodes = self.get_nodes()
        edges = [Edge(node, n_) for n_ in nodes]

        t1 = Triangle(edges[0], edges[1], self.edges[0])
        t2 = Triangle(edges[1], edges[2], self.edges[1])
        t3 = Triangle(edges[2], edges[0], self.edges[2])
        return t1, t2, t3, edges[0], edges[1], edges[2]


class DeloneBinder:
    def __init__(self):
        pass

    def bind(self, nodes: List[Node]):
        edges = [Edge(nodes[0], nodes[1]), Edge(nodes[1], nodes[2]), Edge(nodes[2], nodes[0])]
        triangles = [Triangle(edges[0], edges[1], edges[2])]
        for edge in edges:
            edge.triangle1 = triangles[0]
        for node in nodes[3:]:

            self._add_node(node, edges, triangles)
        print(triangles[0].edges[0].node1, triangles[0].edges[0].node2, triangles[0].edges[1].node2, )
        return edges

    def _add_node(self, node: Node, edges, triangles):
        for i, triangle in enumerate(triangles):
            if triangle.is_contain(node):
                t1, t2, t3, e1, e2, e3 = triangle.diff3(node)
                triangles.pop(i)
                for t_ in [t1, t2, t3]:
                    triangles.append(t_)
                for e_ in [e1, e2, e3]:
                    edges.append(e_)
                return



