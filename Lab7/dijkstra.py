#----------------------------------------------------------
# Lab #7: Dijkstra’s Shortest-Path Tree
#
# Date: 15-Nov-2024
# Authors:
#           A01749694 Sebastian Antonio Almanza
#           A01749850 Estefanía Rico
#----------------------------------------------------------
import heapq

type WeightedGraph = dict[str, set[tuple[str, float]]]

#Initilizes distances to all nodes(except initial) & the SPT.
def dijkstra_spt(
        initial: str,
        graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:
    distances: dict[str, float] = {node: float('inf') for node in graph}
    distances[initial] = 0
    spt: WeightedGraph = {node: set() for node in graph}

    #Initialize priority queue with the initial node
    heap = [(0, initial)]
    predecessors: dict[str, tuple[str, float]] ={}

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            #If a shorter path to the neighbor is found, update distance and predecessor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
                predecessors[neighbor] = (current_node, weight)

    #Builds the SPT from precedors
    for node, (pred_node, weight) in predecessors.items():
        spt[node].add((pred_node, weight))
        spt[pred_node].add((node, weight))

    return distances, spt