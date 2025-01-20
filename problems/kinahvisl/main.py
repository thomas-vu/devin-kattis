def minimum_number_of_people(initial, final):
    n = len(initial)
    min_N = n
    
    for i in range(n):
        diff = 0
        for j in range(n):
            if initial[j] != final[(i + j) % n]:
                diff += 1
        min_N = min(min_N, diff)
    
    return min_N

# Read input
initial = input().strip()
final = input().strip()

# Calculate and print the result
print(minimum_number_of_people(initial, final))