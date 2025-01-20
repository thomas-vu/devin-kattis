def solve(N, K, stars):
    from math import inf
    from itertools import combinations
    
    # Precompute the sum of stars for all possible subsets of houses
    sums = [0] * (1 << N)
    for i in range(N):
        for mask in range(1 << N):
            if mask & (1 << i):
                sums[mask] += stars[i]
    
    # Calculate the initial answer for maximum stars Mario can rob
    max_stars = 0
    min_bowser_stole = inf
    
    # Try all possible ways to distribute the stars into K sacks
    for mask in range(1 << N):
        if sum((mask >> i) & 1 for i in range(N)) == K:
            # Sort the taken houses by their stars
            taken_houses = [stars[i] for i in range(N) if (mask >> i) & 1]
            taken_houses.sort()
            
            # Calculate the number of stars Mario will have
            mario_stars = sum(taken_houses[-K//2:])
            
            # Update the maximum stars and minimum Bowser's steal
            max_stars = max(max_stars, mario_stars)
            
            # Calculate the number of stars Bowser will steal
            bowser_stole = sum(taken_houses[:K//2])
            
            # Update the minimum Bowser's steal
            min_bowser_stole = min(min_bowser_stole, bowser_stole)
    
    return max_stars, min_bowser_stole

# Read input
N, K = map(int, input().split())
stars = list(map(int, input().split()))

# Solve the problem and output the result
max_stars, min_bowser_stole = solve(N, K, stars)
print(max_stars, min_bowser_stole)