class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []


    def add_connection(self, other_station):
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)


    def __str__(self):
        res_str = f"{self.station_name}: "

        for station in self.adjacent_stations:
            res_str += f"{station.station_name} "

        return res_str
        

def create_subway_graph(input_file):
    stations = {}

    with open(input_file) as stations_raw_file:
        for line in stations_raw_file:
            previous_station = None
            subway_line = line.strip().split("-")

            for name in subway_line:
                station_name = name.strip()

                if station_name not in stations:
                    current_station = StationNode(station_name)
                    stations[station_name] = current_station

                else:
                    current_station = stations[station_name]

                if previous_station is not None:
                    current_station.add_connection(previous_station)

                previous_station = current_station

    return stations

stations = create_station_nodes("./stations.txt")
