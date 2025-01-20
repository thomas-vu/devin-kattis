a, b = map(int, input().split())
c, d = map(int, input().split())

# Calculate the least common multiple of a+b and c+d
def lcm(x, y):
    from math import gcd
    return x * y // gcd(x, y)

lcm_ab = lcm(a + b, c + d)

# Calculate the number of splitters needed to achieve the desired ratio
splitters = []
current_a = lcm_ab * a // (a + b)
current_b = lcm_ab * b // (a + b)
desired_c = lcm_ab * c // (c + d)
desired_d = lcm_ab * d // (c + d)

# Helper function to add splitters and connections
def add_splitter(left, right):
    global current_a, current_b
    splitters.append((left, right))
    new_a = (current_a * left) // (left + right)
    new_b = (current_b * right) // (left + right)
    current_a -= new_a
    current_b -= new_b

# Connect the global input to splitter 0 and the outputs to -1 and -2
add_splitter(desired_c, desired_d)

# Output the result
print(len(splitters))
for left, right in splitters:
    print(left, right)