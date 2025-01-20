def main():
    n = int(input())
    streets = {}
    
    for _ in range(n):
        data = list(map(int, input().split()))
        street_id = data[0]
        connected_count = data[1]
        connections = data[2:]
        streets[street_id] = connections
    
    trapped_streets = []
    unreachable_streets = []
    
    # Check for trapped streets
    for street_id, connections in streets.items():
        if 0 not in connections:
            trapped_streets.append(street_id)
    
    # Check for unreachable streets
    all_connected = set()
    for connections in streets.values():
        all_connected.update(connections)
    
    for street_id, connections in streets.items():
        if street_id != 0 and street_id not in all_connected:
            unreachable_streets.append(street_id)
    
    # Output results
    if trapped_streets:
        for street_id in trapped_streets:
            print(f"TRAPPED {street_id}")
    if unreachable_streets:
        for street_id in unreachable_streets:
            print(f"UNREACHABLE {street_id}")
    if not trapped_streets and not unreachable_streets:
        print("NO PROBLEMS")

if __name__ == "__main__":
    main()