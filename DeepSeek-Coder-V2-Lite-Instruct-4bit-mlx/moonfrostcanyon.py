def main():
    R, C = map(int, input().split())
    farm = [input() for _ in range(R)]
    
    # Initialize the grid to store the seed types
    grid = [['' for _ in range(C)] for _ in range(R)]
    
    # Helper function to check if a 3x3 grid is valid
    def is_valid(r, c):
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if grid[nr][nc] != '':
                        return False
        return True
    
    # Assign seeds to tilled squares
    seed_type = 1
    for r in range(R):
        for c in range(C):
            if farm[r][c] == '.':
                while not is_valid(r, c):
                    seed_type += 1
                    if seed_type > 4:
                        seed_type = 1
                grid[r][c] = str(seed_type)
    
    # Output the result
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()