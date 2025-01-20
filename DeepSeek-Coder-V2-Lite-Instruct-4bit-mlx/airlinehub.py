import math

def distance(lat1, lon1, lat2, lon2):
    R = 6371000  # Earth's radius in meters
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    
    a = math.sin(dLat/2) * math.sin(dLat/2) + \
        math.cos(lat1) * math.cos(lat2) * \
        math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def find_hub(airports):
    max_distance = float('inf')
    best_hub = None
    
    for i in range(len(airports)):
        min_distance = 0
        for j in range(len(airports)):
            if i != j:
                dist = distance(airports[i][0], airports[i][1], airports[j][0], airports[j][1])
                min_distance = max(min_distance, dist)
        if min_distance < max_distance:
            max_distance = min_distance
            best_hub = airports[i]
    
    return best_hub

import sys
input = sys.stdin.read
data = input().splitlines()

i = 0
while i < len(data):
    n = int(data[i])
    airports = []
    for j in range(1, n + 1):
        lat, lon = map(float, data[i+j].split())
        airports.append((lat, lon))
    best_hub = find_hub(airports)
    print("{:.2f} {:.2f}".format(best_hub[0], best_hub[1]))
    i += n + 1