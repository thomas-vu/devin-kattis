def find_youngest(n, ages):
    return min(ages)

# Read input
n = int(input())
ages = [int(input()) for _ in range(n)]

# Output the youngest friend's age
print(find_youngest(n, ages))