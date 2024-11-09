#----------------------------------------------------------
# Lab #7: Dijkstra’s Shortest-Path Tree
#
# Date: 15-Nov-2024
# Authors:
#           A01749694 Sebastian Antonio Almanza
#           A01749850 Estefanía Rico
#----------------------------------------------------------


type WeightedGraph = dict[str, set[tuple[str, float]]]

def dijkstra_spt(initial: str, graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:
    visited: set[str] = set()
    travel_cost: int = 0
    
