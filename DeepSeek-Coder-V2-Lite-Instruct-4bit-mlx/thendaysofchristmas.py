def gifts_on_day(N):
    return sum(i + 1 for i in range(N))

def total_gifts(N):
    return sum((i + 1) * (N - i) for i in range(N))

# Read the input
N = int(input())

# Calculate and output the results
print(gifts_on_day(N))
print(total_gifts(N))