def main():
    p = int(input())
    planets = {}
    for _ in range(p):
        line = input().split()
        planet_name = line[0]
        n = int(line[1])
        species_list = line[2:]
        planets[planet_name] = set(species_list)
    
    v = int(input())
    visitor_count = {}
    for _ in range(v):
        line = input().split()
        m = int(line[0])
        species_name = line[1]
        for planet, species in planets.items():
            if species_name in species:
                visitor_count[planet] = visitor_count.get(planet, 0) + m
    
    for planet in sorted(visitor_count.keys()):
        print(f"{planet} {visitor_count[planet]}")

if __name__ == "__main__":
    main()