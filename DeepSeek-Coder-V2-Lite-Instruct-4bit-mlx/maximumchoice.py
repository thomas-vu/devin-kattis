def max_turns(n, b):
    turns = 0
    while n > 1:
        size = min(b, n)
        n -= size
        turns += 1
    return turns

# Read input from stdin
n, b = map(int, input().split())
print(max_turns(n, b))