from collections import defaultdict
from abc import ABCMeta, abstractmethod

class Graph(metaclass=ABCMeta):
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(set)

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def remove_vertex(self, vertex):
        self.vertices.remove(vertex)
        del self.edges[vertex]
        for set_list in self.edges.values():
            set_list.remove(vertex)

    @abstractmethod
    def add_edge(self, source, destination):
        pass

    @abstractmethod
    def remove_edge(self, source, destination):
        pass

    def __repr__(self):
        result = ""
        result += f"Vertices: {self.vertices}\n"
        for vertex, set_list in self.edges.items():
            result += f"{vertex}: {set_list}\n"
        return result

    def __str__(self):
        self.__repr__()


class DirectedGraph(Graph):
    def add_edge(self, source, destination):
        self.edges[source].add(destination)

    def remove_edge(self, source, destination):
        self.edges[source].remove(destination)


class UndirectedGraph(Graph):
    def add_edge(self, source, destination):
        self.edges[source].add(destination)
        self.edges[destination].add(source)

    def remove_edge(self, source, destination):
        self.edges[source].remove(destination)
        self.edges[destination].remove(source)


graph = UndirectedGraph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)