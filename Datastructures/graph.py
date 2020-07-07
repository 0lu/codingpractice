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
    def add_edge(self, source, destination, weight=None):
        pass

    @abstractmethod
    def remove_edge(self, source, destination, weight=None):
        pass

    def __repr__(self):
        result = ""
        result += f"Vertices: {self.vertices}\n"
        for vertex, set_list in self.edges.items():
            result += f"{vertex}: {set_list}\n"
        return result

    def __str__(self):
        return self.__repr__()


class UnweightedDirectedGraph(Graph):
    def add_edge(self, source, destination, weight=None):
        self.edges[source].add(destination)

    def remove_edge(self, source, destination, weight=None):
        self.edges[source].remove(destination)


class UnweightedUndirectedGraph(Graph):
    def add_edge(self, source, destination, weight=None):
        self.edges[source].add(destination)
        self.edges[destination].add(source)

    def remove_edge(self, source, destination, weight=None):
        self.edges[source].remove(destination)
        self.edges[destination].remove(source)

class WeightedDirectedGraph(Graph):
    def add_edge(self, source, destination, weight=None):
        self.edges[source].add((destination, weight))

    def remove_edge(self, source, destination, weight=None):
        self.edges[source].remove((destination, weight))

class WeightedUndirectedGraph(Graph):
    def add_edge(self, source, destination, weight=None):
        self.edges[source].add((destination, weight))
        self.edges[destination].add((source, weight))

    def remove_edge(self, source, destination, weight=None):
        self.edges[source].remove((destination, weight))
        self.edges[destination].remove((source, weight))


graph = UnweightedUndirectedGraph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
