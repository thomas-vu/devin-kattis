def compare_integers(a, b):
    return int(a > b)

# Read input
a, b = map(int, input().split())

# Output the result
print(compare_integers(a, b))