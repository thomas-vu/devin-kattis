def find_longest_sequence(N):
    def dfs(x, path):
        if x > N:
            return len(path) - 1
        max_length = len(path)
        for next_x in range(x * 2, N + 1, x):
            max_length = max(max_length, dfs(next_x, path + [next_x]))
        return max_length
    
    max_length = 0
    best_sequence = []
    
    for i in range(1, N + 1):
        length = dfs(i, [i])
        if length > max_length:
            max_length = length
            best_sequence = [i] + [x for x in range(i * 2, N + 1, i)]
    
    return max_length, best_sequence

N = int(input().strip())
max_length, sequence = find_longest_sequence(N)
print(max_length)
if max_length > 0:
    print(' '.join(map(str, sequence)))