def count_numbers(n, e):
    power_of_2 = str(2 ** e)
    count = 0
    
    for i in range(n + 1):
        if power_of_2 in str(i):
            count += 1
    
    return count

# Read input
n, e = map(int, input().split())

# Output the result
print(count_numbers(n, e))