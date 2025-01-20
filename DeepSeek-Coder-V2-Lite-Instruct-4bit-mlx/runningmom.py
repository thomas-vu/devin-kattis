def find_safe_cities(flights, cities):
    city_graph = {}
    for flight in flights:
        o, d = flight.split()
        if o not in city_graph:
            city_graph[o] = []
        city_graph[o].append(d)
    
    def can_escape(city):
        visited = set()
        queue = [city]
        while queue:
            current_city = queue.pop()
            if current_city in visited:
                continue
            visited.add(current_city)
            if current_city in city_graph:
                queue.extend(city for city in city_graph[current_city] if city not in visited)
        return set(visited)
    
    safe_cities = {}
    for city in cities:
        if city not in safe_cities:
            escape = can_escape(city)
            for other_city in cities:
                if other_city not in escape and other_city != city:
                    safe_cities[other_city] = False
                else:
                    safe_cities[other_city] = True
            safe_cities[city] = len(escape) == len(cities)
    
    return safe_cities

# Read input
n = int(input())
flights = [input().strip() for _ in range(n)]
cities = []
while True:
    city_name = input().strip()
    if not city_name:
        break
    cities.append(city_name)

safe_cities = find_safe_cities(flights, cities)
for city in cities:
    print(city, "safe" if safe_cities[city] else "trapped")