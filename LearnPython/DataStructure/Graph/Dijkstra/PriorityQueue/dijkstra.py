from math import inf
from priority_queue import PriorityQueue
from subway_weighted_graph import create_station_graph

def dijkstra(graph, start_node):
	queue = PriorityQueue()

	for station_node in graph.values():
		station_node.distance = inf
		station_node.predecessor = None
		station_node.visited = False
		
	start_node.distance = 0
	queue.insert((start_node.distance, start_node))
	
	while len(queue.heap) > 1:
		current_station = queue.extract_min()
		current_station.visited = True
		for neighbor, weight in current_station.adjacent_stations.items():
			if not neighbor.visited:
				new_distance = current_station.distance + weight
				if new_distance < neighbor.distance:
					neighbor.distance = new_distance
					neighbor.predecessor = current_station
					queue.insert((neighbor.distance, neighbor))

			

graph = create_station_graph()
start_node = graph["A"]
dijkstra(graph, start_node)
for station_node in graph.values():
	if station_node.predecessor is None:
		print(station_node.station_name, station_node.predecessor, station_node.distance)
	else:
		print(station_node.station_name, station_node.predecessor.station_name, station_node.distance)
