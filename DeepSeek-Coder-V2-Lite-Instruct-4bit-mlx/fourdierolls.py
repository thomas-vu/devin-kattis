def count_ways(rolls, n):
    if n == 0:
        return factorial(4) - len(set(rolls)), factorial(4) - count_unique_digits(rolls, n)
    elif n == 1:
        return count_unique_digits(rolls, n) * factorial(3), factorial(4) - count_unique_digits(rolls, n)
    elif n == 2:
        return count_unique_digits(rolls, n) * factorial(2), factorial(4) - count_unique_digits(rolls, n)
    elif n == 3:
        return count_unique_digits(rolls, n) * factorial(1), factorial(4) - count_unique_digits(rolls, n)
    else:
        return 0, 0

def count_unique_digits(rolls, n):
    unique_digits = set()
    for roll in rolls:
        unique_digits.add(roll)
    return len(unique_digits)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Read input
n = int(input())
rolls = list(map(int, input().split()))

# Calculate the number of ways for Ashley and Brandon to win
ashley_wins, brandon_wins = count_ways(rolls, n)

# Output the result
print(ashley_wins, brandon_wins)