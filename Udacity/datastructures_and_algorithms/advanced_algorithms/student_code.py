from heapq import heappush, heappop
import math


def shortest_path(M, start, goal):
    frontier = []
    distances = {}
    visited = set()

    heuristic = get_heuristics(M, start, goal)
    dist_from_start = 0
    total = heuristic + dist_from_start
    distances[start] = total

    heappush(frontier, (total, dist_from_start, start, [start]))

    while frontier:

        total, dist_from_start, current, path = heappop(frontier)
        print(f"current node is {current}")
        if current == goal:
            return path

        if current in visited:
            continue

        for neighbor in M.roads[current]:
            heuristic = get_heuristics(M, neighbor, goal)
            curr_dist_from_start = dist_from_start + get_distance(M, current, neighbor)
            total = heuristic + curr_dist_from_start
            if neighbor not in distances or total < distances[neighbor]:
                distances[neighbor] = total
                heappush(frontier, (total, curr_dist_from_start, neighbor, path + [neighbor]))

        visited.add(current)


def get_heuristics(M, current, dest):
    return get_distance(M, current, dest)


def get_distance(M, source, dest):
    xcurrent, ycurrent = M.intersections[source]
    xdest, ydest = M.intersections[dest]
    distance = math.sqrt(pow((xdest - xcurrent), 2) + pow((ydest - ycurrent), 2))
    return distance