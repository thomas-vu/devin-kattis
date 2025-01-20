def main():
    while True:
        try:
            w, h = map(int, input().split())
            n = int(input())
            
            # Initialize the office space map with zeros
            office = [[0 for _ in range(w)] for _ in range(h)]
            
            # Process each employee's request
            requests = {}
            for _ in range(n):
                name, x1, y1, x2, y2 = input().split()
                x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
                requests[name] = (x1, y1, x2, y2)
                
                # Mark the requested area on the map
                for i in range(y1, y2 + 1):
                    for j in range(x1, x2 + 1):
                        office[i][j] += 1
            
            # Calculate the total area, unallocated space, and contested space
            total_area = w * h
            unallocated_space = 0
            contested_space = 0
            guaranteed_areas = {}
            
            for name, (x1, y1, x2, y2) in requests.items():
                area = (x2 - x1 + 1) * (y2 - y1 + 1)
                if all(office[i][j] == 1 for i in range(y1, y2 + 1) for j in range(x1, x2 + 1)):
                    guaranteed_areas[name] = area
                else:
                    contested_space += (x2 - x1 + 1) * (y2 - y1 + 1)
                
                # Count unallocated space
                if all(office[i][j] == 0 for i in range(y1, y2 + 1) for j in range(x1, x2 + 1)):
                    unallocated_space += (x2 - x1 + 1) * (y2 - y1 + 1)
            
            # Output the results for each test case
            print(f"Total {total_area}")
            print(f"Unallocated {unallocated_space if unallocated_space else total_area - sum(requests.values(), ())}")
            print(f"Contested {contested_space}")
            
            for name, area in sorted(guaranteed_areas.items(), key=lambda x: list(requests.keys()).index(x[0])):
                print(f"{name} {area}")
            
            print()  # Blank line after each test case
        
        except EOFError:
            break

if __name__ == "__main__":
    main()