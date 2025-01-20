def find_most_distant_pebble(spots):
    n = len(spots)
    max_distance = 0
    
    for i in range(n):
        jump_sum = spots[i]
        j = i + 1
        while j < n and jump_sum <= spots[j]:
            if spots[i] + spots[j] == j - i:
                max_distance = max(max_distance, j - i)
            j += 1
    
    return max_distance + 1 if max_distance > 0 else 0

# Read input from stdin
while True:
    try:
        n = int(input())
        spots = list(map(int, input().split()))
        
        result = find_most_distant_pebble(spots)
        print(result)
    except EOFError:
        break