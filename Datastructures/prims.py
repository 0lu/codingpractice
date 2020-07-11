from Datastructures.graph import WeightedUndirectedGraph
import heapq

def minimum_spanning_tree(source, graph):
    unvisited = {vertex for vertex in graph.vertices}
    spanning_tree = []
    heap = []
    full_cost = 0

    unvisited.remove(source)

    while unvisited:
        for neighbor, weight in graph.edges[source]:
            if neighbor in unvisited:
                heapq.heappush(heap, (weight, neighbor))

        weight, vertex = heapq.heappop(heap)
        if vertex in unvisited:
            spanning_tree.append(vertex)
            print(f"edge{vertex} with weight {weight} added to the spanning tree")
            full_cost += weight
            source = vertex
            unvisited.remove(source)

    return spanning_tree, full_cost


g = WeightedUndirectedGraph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(7)
g.add_vertex(8)
g.add_edge(0, 1, 4)
g.add_edge(1, 7, 6)
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 3)
g.add_edge(3, 7, 1)
g.add_edge(3, 4, 2)
g.add_edge(3, 5, 1)
g.add_edge(4, 5, 1)
g.add_edge(5, 6, 1)
g.add_edge(6, 7, 2)
g.add_edge(6, 8, 2)
g.add_edge(7, 8, 2)

print(minimum_spanning_tree(1, g))
