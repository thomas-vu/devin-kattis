def main():
    n, k, h = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    cow_positions = [tuple(map(int, input().split())) for _ in range(k)]
    flood_levels = [int(input()) for _ in range(h)]
    
    # Initialize the number of cows that can survive
    max_surviving_cows = 0
    
    # Iterate through each flood level and check the maximum cows that can survive
    for flood_level in flood_levels:
        new_positions = []
        for r, c in cow_positions:
            # Check the adjacent positions (up, down, left, right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and field[nr][nc] > flood_level:
                    new_positions.append((nr, nc))
        
        # Update the number of surviving cows and positions for the next iteration
        cow_positions = list(set(new_positions))
        max_surviving_cows += len(cow_positions)
    
    print(max_surviving_cows)

if __name__ == "__main__":
    main()