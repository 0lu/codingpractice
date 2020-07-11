import heapq

from Datastructures.graph import WeightedUndirectedGraph


def shortest_path(source, destination, graph):
    distances = {source: 0}
    parents = {source: None}

    frontier = []
    explored = set()

    heapq.heappush(frontier, (0, source))

    while frontier:
        distance, vertex = heapq.heappop(frontier)

        if vertex == destination:
            continue
        for neighbor, weight in graph.edges[vertex]:
            if neighbor not in explored:
                calc_distance = distances[vertex] + weight
                if neighbor not in distances or calc_distance < distances[neighbor]:
                    distances[neighbor] = calc_distance
                    parents[neighbor] = vertex
                    heapq.heappush(frontier, (calc_distance, neighbor))

        explored.add(vertex)

    results = [destination]
    curr = parents[destination]
    while curr is not None:
        results.append(curr)
        curr = parents[curr]

    return results[::-1], distances[destination]


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
