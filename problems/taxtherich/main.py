def count_applause(N, incomes):
    applause_count = 0
    
    for i in range(N):
        if sum(1 for j in incomes[:i+1] if j < (sum(incomes) / N)) > (i + 1) / 2:
            applause_count += 1
    
    return applause_count

# Read input from the user
N = int(input())
incomes = list(map(int, input().split()))

# Output the result
print(count_applause(N, incomes))