def find_best_position(n, huts):
    total = sum(huts)
    left_sum = 0
    right_sum = total
    min_diff = abs(2 * left_sum - total)
    best_position = 0
    
    for i in range(n):
        right_sum -= huts[i]
        diff = abs(2 * left_sum - total) + abs(2 * right_sum - total)
        if diff < min_diff:
            min_diff = diff
            best_position = i
        left_sum += huts[i]
    
    return best_position + 1

n, q = map(int, input().split())
huts = list(map(int, input().split()))

for _ in range(q):
    i, x = map(int, input().split())
    huts[i] = x
    print(find_best_position(n, huts))