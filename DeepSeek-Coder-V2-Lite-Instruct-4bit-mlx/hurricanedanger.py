def closest_city(hurricane_start, hurricane_end, cities):
    min_distance = float('inf')
    closest_cities = []
    
    for city in cities:
        distance = abs(hurricane_start[0] - city[1]) + abs(hurricane_start[1] - city[2])
        if distance < min_distance:
            min_distance = distance
            closest_cities = [city[0]]
        elif distance == min_distance:
            closest_cities.append(city[0])
    
    return ' '.join(closest_cities)

def main():
    n = int(input())
    
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        hurricane_path = (x1, y1), (x2, y2)
        
        m = int(input())
        cities = []
        
        for _ in range(m):
            city_name, x, y = input().split()
            cities.append((city_name, int(x), int(y)))
        
        print(closest_city(hurricane_path[0], hurricane_path[1], cities))

if __name__ == "__main__":
    main()