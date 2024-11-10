#----------------------------------------------------------
# Lab #7: Dijkstra’s Shortest-Path Tree
#
# Date: 15-Nov-2024
# Authors:
#           A01749694 Sebastian Antonio Almanza
#           A01749850 Estefanía Rico
#----------------------------------------------------------
from pprint import pprint


type WeightedGraph = dict[str, set[tuple[str, float]]]

def dijkstra_spt(initial: str, graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:
    visited: set[str] = set()
    distance: int = 0
    



if __name__ == "__main__":
    graph: WeightedGraph = {'A': {('B', 5), ('C', 10), ('E', 6)},
                   'B': {('A', 5), ('D', 2)},
                   'C': {('A', 10), ('D', 1), ('E', 3)},
                   'D': {('B', 2), ('C', 1), ('E', 4)},
                   'E': {('A', 6), ('C', 3), ('D', 4)},
                  }
    initial: str = 'A'
     
