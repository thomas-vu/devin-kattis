def wood_needed(trees, height):
    return sum([tree - height for tree in trees if tree > height])

def find_max_height(N, M, trees):
    left, right = 0, max(trees)
    
    while left < right:
        mid = (left + right + 1) // 2
        if wood_needed(trees, mid) >= M:
            left = mid
        else:
            right = mid - 1
    
    return left

# Reading input
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# Finding the maximum height
result = find_max_height(N, M, trees)
print(result)