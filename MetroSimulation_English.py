from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional

class Station:
    def __init__(self, idx: str, name: str, line: str):
        self.idx = idx
        self.name = name
        self.line = line
        self.neighbors: List[Tuple['Station', int]] = []  # (station, travel_time) tuples

    def add_neighbor(self, station: 'Station', travel_time: int):
        self.neighbors.append((station, travel_time))

class MetroNetwork:
    def __init__(self):
        self.stations: Dict[str, Station] = {}
        self.lines: Dict[str, List[Station]] = defaultdict(list)

    def add_station(self, idx: str, name: str, line: str) -> None:
        if idx not in self.stations:
            station = Station(idx, name, line)
            self.stations[idx] = station
            self.lines[line].append(station)

    def add_connection(self, station1_id: str, station2_id: str, travel_time: int) -> None:
        station1 = self.stations[station1_id]
        station2 = self.stations[station2_id]
        station1.add_neighbor(station2, travel_time)
        station2.add_neighbor(station1, travel_time)
    
    def find_least_transfer_route(self, start_id: str, target_id: str) -> Optional[List[Station]]:
        if start_id not in self.stations or target_id not in self.stations:
            return None 

        start = self.stations[start_id]
        target = self.stations[target_id]

        queue = deque([(start, [start])]) 
        visited = set([start])  # Track visited stations

        while queue:
            current, route = queue.popleft()
            
            if current == target:
                return route 

            for neighbor, _ in current.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, route + [neighbor]))
        return None

    def find_fastest_route(self, start_id: str, target_id: str) -> Optional[Tuple[List[Station], int]]:
        return None

# Example Usage
if __name__ == "__main__":
    metro = MetroNetwork()
    
    # Adding Stations
    metro.add_station("K1", "Kızılay", "Red Line")
    metro.add_station("K2", "Ulus", "Red Line")
    metro.add_station("K3", "Demetevler", "Red Line")
    metro.add_station("K4", "OSB", "Red Line")
    
    metro.add_station("M1", "AŞTİ", "Blue Line")
    metro.add_station("M2", "Kızılay", "Blue Line")  # Transfer Station
    metro.add_station("M3", "Sıhhiye", "Blue Line")
    metro.add_station("M4", "Gar", "Blue Line")
    
    metro.add_station("T1", "Batıkent", "Orange Line")
    metro.add_station("T2", "Demetevler", "Orange Line")  # Transfer Station
    metro.add_station("T3", "Gar", "Orange Line")  # Transfer Station
    metro.add_station("T4", "Keçiören", "Orange Line")
    
    # Adding Connections
    metro.add_connection("K1", "K2", 4)
    metro.add_connection("K2", "K3", 6)
    metro.add_connection("K3", "K4", 8)
    
    metro.add_connection("M1", "M2", 5)
    metro.add_connection("M2", "M3", 3)
    metro.add_connection("M3", "M4", 4)
    
    metro.add_connection("T1", "T2", 7)
    metro.add_connection("T2", "T3", 9)
    metro.add_connection("T3", "T4", 5)
    
    metro.add_connection("K1", "M2", 2)
    metro.add_connection("K3", "T2", 3)
    metro.add_connection("M4", "T3", 2)
    
    # Test Cases
    print("\n=== Test Cases ===")
    
    print("\n1. AŞTİ to OSB:")
    route = metro.find_least_transfer_route("M1", "K4")
    if route:
        print("Least transfer route:", " -> ".join(s.name for s in route))
    
    result = metro.find_fastest_route("M1", "K4")
    if result:
        route, time = result
        print(f"Fastest route ({time} minutes):", " -> ".join(s.name for s in route))
    
    print("\n2. Batıkent to Keçiören:")
    route = metro.find_least_transfer_route("T1", "T4")
    if route:
        print("Least transfer route:", " -> ".join(s.name for s in route))
    
    result = metro.find_fastest_route("T1", "T4")
    if result:
        route, time = result
        print(f"Fastest route ({time} minutes):", " -> ".join(s.name for s in route))
    
    print("\n3. Keçiören to AŞTİ:")
    route = metro.find_least_transfer_route("T4", "M1")
    if route:
        print("Least transfer route:", " -> ".join(s.name for s in route))
    
    result = metro.find_fastest_route("T4", "M1")
    if result:
        route, time = result
        print(f"Fastest route ({time} minutes):", " -> ".join(s.name for s in route))
