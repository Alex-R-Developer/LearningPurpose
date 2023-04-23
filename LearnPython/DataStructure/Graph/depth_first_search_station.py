from collections import deque
from subway_graph import *

def dfs(graph, start_node):
    stack = deque()

    for station_node in graph.values():
        station_node.visited = 0

    start_node.visited = 1
    stack.append(start_node)
    
    while stack:
        current_station = stack.pop()
        current_station.visited = 2
        for neighbor in current_station.adjacent_stations:
            if neighbor.visited == 0:
                neighbor.visited = 1
                stack.append(neighbor)