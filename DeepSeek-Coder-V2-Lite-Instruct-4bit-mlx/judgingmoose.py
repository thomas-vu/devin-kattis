def moose_points(l, r):
    if l == 0 and r == 0:
        return "Not a moose"
    elif l == r:
        points = l + r
        return f"Even {points}"
    else:
        points = max(l, r) * 2
        return f"Odd {points}"

# Read input
l, r = map(int, input().split())
result = moose_points(l, r)
print(result)