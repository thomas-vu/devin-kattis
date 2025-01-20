def will_blink_at_same_time(p, q, s):
    for t in range(1, s + 1):
        if (t % p == 0) and (t % q == 0):
            return "yes"
    return "no"

# Read input
p, q, s = map(int, input().split())

# Output the result
print(will_blink_at_same_time(p, q, s))