def max_films(emma, marcos):
    emma_likes = set(emma[1:])
    marcos_likes = set(marcos[1:])
    
    prev_emma, prev_marcos = False, False
    count = 0
    
    for day in range(1, 1000001):
        emma_watching = day in emma_likes
        marcos_watching = day in marcos_likes
        
        if (not emma_watching or not prev_emma) and (not marcos_watching or not prev_marcos):
            count += 1
            prev_emma = emma_watching
            prev_marcos = marcos_watching
        else:
            if emma_watching:
                prev_emma = True
            if marcos_watching:
                prev_marcos = True
    
    return count

# Read input
import sys
input_data = sys.stdin.readlines()
emma, marcos = [list(map(int, line.split())) for line in input_data]

# Calculate and print the result
result = max_films(emma, marcos)
print(result)