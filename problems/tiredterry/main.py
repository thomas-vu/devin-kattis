def count_tired_seconds(n, p, d, sleep_pattern):
    tired_count = 0
    for i in range(p, n + 1):
        if sum([sleep_pattern[j] == 'Z' for j in range(i - p + 1, i)]) < d:
            tired_count += 1
    return tired_count

# Read input
n, p, d = map(int, input().split())
sleep_pattern = input()

# Calculate and output the result
print(count_tired_seconds(n, p, d, sleep_pattern))