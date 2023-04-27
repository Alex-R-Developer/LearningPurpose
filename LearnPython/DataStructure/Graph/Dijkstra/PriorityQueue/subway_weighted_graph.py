class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = {}

    def add_connection(self, other_station, distance):
        self.adjacent_stations[other_station] = distance
        other_station.adjacent_stations[self] = distance

def create_station_graph():
    station_dict = {}

    station_dict["A"] = StationNode("A")
    station_dict["B"] = StationNode("B")
    station_dict["C"] = StationNode("C")
    station_dict["D"] = StationNode("D")
    station_dict["E"] = StationNode("E")
    station_dict["F"] = StationNode("F")

    station_dict["A"].add_connection(station_dict["B"], 5)
    station_dict["A"].add_connection(station_dict["C"], 3)
    station_dict["B"].add_connection(station_dict["D"], 2)
    station_dict["C"].add_connection(station_dict["D"], 1)
    station_dict["C"].add_connection(station_dict["E"], 6)
    station_dict["D"].add_connection(station_dict["E"], 4)
    station_dict["E"].add_connection(station_dict["F"], 2)

    return station_dict
