from Datastructures.graph import WeightedUndirectedGraph, WeightedDirectedGraph
import heapq


class NegativeCycleDetectedException(Exception):
    pass


def shortest_path(source, destination, graph):
    parents = {}
    distances = {}
    heap = []

    for vertex in graph.vertices:
        parents[vertex] = None
        if vertex == source:
            distances[vertex] = 0
        else:
            distances[vertex] = float("inf")
    
    heapq.heappush(heap, (distances[source], source))
    
    while heap:
        distance, vertex = heapq.heappop(heap)

        if vertex == destination:
            break
        
        for neighbor, weight in graph.edges[vertex]:
            calc_dist = distances[vertex] + weight
            if calc_dist < 0:
                raise NegativeCycleDetectedException("negative cycle detected")
            if calc_dist < distances[neighbor]:
                distances[neighbor] = calc_dist
                parents[neighbor] = vertex
                heapq.heappush(heap, (distances[neighbor], neighbor))

    result = [destination]
    curr = parents[destination]
    while curr is not None:
        result.append(curr)
        curr = parents[curr]

    return result[::-1], distances[destination]


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
print(shortest_path(0, 1, g))
print(shortest_path(0, 8, g))
print(shortest_path(5, 0, g))
print(shortest_path(1, 1, g))

g2 = WeightedDirectedGraph()
g2.add_vertex(1)
g2.add_vertex(2)
g2.add_vertex(3)
g2.add_edge(1, 3, 4)
g2.add_edge(3, 2, -6)
g2.add_edge(2, 1, 3)

print(shortest_path(1, 2, g2))
