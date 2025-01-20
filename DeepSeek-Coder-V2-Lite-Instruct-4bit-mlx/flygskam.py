import math
from itertools import permutations

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth's radius in km
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    
    a = math.sin(dLat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dLon/2)**2
    c = 2*R*math.atan2(math.sqrt(a), math.sqrt(1-a))
    return c

def calculate_shame(airports, routes):
    graph = {airport: [] for airport in airports.keys()}
    for route in routes:
        graph[route['a']].append((route['b'], haversine(airports[route['a']]['lat'], airports[route['a']]['lon'], airports[route['b']]['lat'], airports[route['b']]['lon']) + 100))
        graph[route['b']].append((route['a'], haversine(airports[route['b']]['lat'], airports[route['b']]['lon'], airports[route['a']]['lat'], airports[route['a']]['lon']) + 100))
    
    start = next((airport for airport, details in airports.items() if airport == 'S'), None)
    target = next((airport for airport, details in airports.items() if airport == 'T'), None)
    
    if not start or not target:
        return -1
    
    queue = [(0, start)]
    distances = {airport: float('inf') for airport in airports.keys()}
    distances[start] = 0
    
    while queue:
        current_distance, current_node = min(queue, key=lambda x: x[0])
        queue.remove((current_distance, current_node))
        
        if current_node == target:
            break
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append((distance, neighbor))
    
    return distances[target] if distances[target] != float('inf') else -1

# Read input
N, M = map(int, input().split())
S, T = input().split()
airports = {}
routes = []
for _ in range(N):
    code, lat, lon = input().split()
    airports[code] = {'lat': float(lat), 'lon': float(lon)}
for _ in range(M):
    a, b = input().split()
    routes.append({'a': a, 'b': b})

# Calculate and output the result
result = calculate_shame(airports, routes)
print("{:.10f}".format(result))