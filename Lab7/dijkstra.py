#----------------------------------------------------------
# Lab #7: Dijkstra’s Shortest-Path Tree
#
# Date: 15-Nov-2024
# Authors:
#           A01749694 Sebastian Antonio Almanza
#           A01749850 Estefanía Rico
#----------------------------------------------------------

# from pprint import pprint
# from typing import Dict, Set, Tuple

# type WeightedGraph = dict[str, set[tuple[str, float]]]

# def dijkstra_spt(initial: str, graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:
#     costs = {vertex: float('inf') for vertex in graph}
#     costs[initial] = 0

#     spanning_tree = {vertex: float('inf') for vertex in graph}

#     unvisited = set(graph.keys())

#     while unvisited:
#         current_vertex = min(
#             (vertex for vertex in unvisited if costs[vertex] != float('inf')),
            
#         )
    



# if __name__ == "__main__":
#     graph: WeightedGraph = {'A': {('B', 5), ('C', 10), ('E', 6)},
#                    'B': {('A', 5), ('D', 2)},
#                    'C': {('A', 10), ('D', 1), ('E', 3)},
#                    'D': {('B', 2), ('C', 1), ('E', 4)},
#                    'E': {('A', 6), ('C', 3), ('D', 4)},
#                   }
#     initial: str = 'A'
    

from typing import Dict, Set, Tuple
import heapq

WeightedGraph = Dict[str, Set[Tuple[str, float]]]

def dijkstra_spt(
        initial: str,
        graph: WeightedGraph) -> Tuple[Dict[str, float], WeightedGraph]:
    distances: Dict[str, float] = {node: float('inf') for node in graph}
    distances[initial] = 0

    spt: WeightedGraph = {node: set() for node in graph}

    #priority queue: min-heap of (distance, node)
    heap = [(0, initial)]
    predecessors: Dict[str, Tuple[str, float]] = {}

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
                predecessors[neighbor] = (current_node, weight)

    for node, (pred_node, weight) in predecessors.items():
        spt[node].add((pred_node, weight))
        spt[pred_node].add((node, weight))

    return distances, spt