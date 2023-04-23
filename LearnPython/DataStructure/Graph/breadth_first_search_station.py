from collections import deque
from subway_graph import create_station_graph

def bfs(graph, start_node):
    queue = deque()

    for station_node in graph.values():
        station_node.visited = False

    start_node.visited = True
    queue.append(start_node)
    
    while queue:
        current_station = queue.popleft()
        for neighbor in current_station.adjacent_stations:
            if not neighbor.visited:
                neighbor.visited = True
                neighbor.predecessor = current_station
                queue.append(neighbor)


def back_track(destination_node):
    res_str = ""
    temp = destination_node

    while temp is not None:
        res_str = f"{temp.station_name} {res_str}"
        temp = temp.predecessor

    return res_str