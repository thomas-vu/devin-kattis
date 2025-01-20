def min_score(tiles):
    tiles.sort()
    n = len(tiles)
    total_sum = sum(tiles)
    min_diff = float('inf')
    
    for i in range(n):
        current_sum = total_sum - tiles[i]
        for j in range(n):
            if i != j:
                min_diff = min(min_diff, abs((total_sum - tiles[j]) - tiles[i]))
    
    return min_diff

n = int(input())
tiles = list(map(int, input().split()))
print(min_score(tiles))