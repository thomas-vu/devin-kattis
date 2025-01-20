def count_pink_rose(N, button_names):
    count = 0
    for name in button_names:
        if 'pink' in name.lower() or 'rose' in name.lower():
            count += 1
    return count if count > 0 else "I must watch Star Wars with my daughter"

# Read input
N = int(input())
button_names = [input().strip() for _ in range(N)]

# Output the result
print(count_pink_rose(N, button_names))