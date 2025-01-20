def can_hit_all_targets(targets):
    if len(targets) <= 2:
        return "success"
    
    def on_line(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])
    
    for i in range(len(targets)):
        for j in range(i + 1, len(targets)):
            targets_hit = 0
            for k in range(len(targets)):
                if on_line(targets[i], targets[j], targets[k]):
                    targets_hit += 1
            if targets_hit == len(targets):
                return "success"
    return "failure"

# Read input
N = int(input())
targets = [tuple(map(int, input().split())) for _ in range(N)]

# Check if it's possible to hit all targets with at most two shots
result = can_hit_all_targets(targets)
print(result)