import math

# Constants
R = 6371009  # Earth's radius in meters
PI = math.pi

def degrees_to_radians(degrees):
    return degrees * (PI / 180)

def haversine_distance(lat1, lon1, lat2, lon2):
    lat1 = degrees_to_radians(lat1)
    lon1 = degrees_to_radians(lon1)
    lat2 = degrees_to_radians(lat2)
    lon2 = degrees_to_radians(lon2)
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c

def straight_line_distance(lat1, lon1, lat2, lon2):
    x = (lon2 - lon1) * math.cos((lat1 + lat2) / 2)
    y = (lat2 - lat1)
    return math.sqrt(x**2 + y**2) * R

def main():
    T = int(input())
    for _ in range(T):
        lat1, lon1, lat2, lon2 = map(float, input().split())
        great_circle_distance = haversine_distance(lat1, lon1, lat2, lon2)
        straight_line_distance = straight_line_distance(lat1, lon1, lat2, lon2)
        difference = great_circle_distance - straight_line_distance
        print("{:.7f}".format(difference))

if __name__ == "__main__":
    main()