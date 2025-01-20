def min_energy_to_complete_climb(R, C, cliff, energy_matrix):
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Initialize the DP table with infinity
    dp = [[float('inf')] * C for _ in range(R)]
    
    # Start points
    start_points = []
    for r in range(R):
        for c in range(C):
            if cliff[r][c] == 'S':
                start_points.append((r, c))
    
    # Function to perform a DP calculation from a given start point
    def dp_calc(start_r, start_c):
        queue = [(start_r, start_c)]
        dp[start_r][start_c] = 0 if cliff[start_r][start_c] == 'S' else energy_matrix[start_r][start_c]
        
        while queue:
            r, c = queue.pop(0)
            current_energy = dp[r][c]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    new_energy = current_energy + energy_matrix[nr][nc]
                    if new_energy < dp[nr][nc]:
                        dp[nr][nc] = new_energy
                        queue.append((nr, nc))
    
    # Calculate DP for each start point
    for r, c in start_points:
        dp_calc(r, c)
    
    # Find the minimum energy needed to start from any 'S' and still have non-negative energy at the end
    min_energy = float('inf')
    for r in range(R):
        for c in range(C):
            if dp[r][c] > 0:
                min_energy = min(min_energy, dp[r][c])
    
    return -min_energy + 1 if min_energy != float('inf') else 0

# Read input
R, C = map(int, input().split())
cliff = [input().split() for _ in range(R)]
energy_matrix = [list(map(int, input().split())) for _ in range(R)]

# Output the result
print(min_energy_to_complete_climb(R, C, cliff, energy_matrix))