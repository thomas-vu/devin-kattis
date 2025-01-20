def min_cows_needed(B, required_beans, T, farmers):
    total_required = sum(required_beans)
    max_farmer_beans = [0] * B
    
    for farmer in farmers:
        M, *beans = farmer
        for bean in beans:
            max_farmer_beans[bean - 1] += 1
    
    min_cows = 0
    for i in range(B):
        if required_beans[i] > max_farmer_beans[i]:
            min_cows = max(min_cows, (required_beans[i] - max_farmer_beans[i]) // (T + 1) + ((required_beans[i] - max_farmer_beans[i]) % (T + 1) > 0))
    
    return min_cows

# Read input
B = int(input())
required_beans = list(map(int, input().split()))
T = int(input())
farmers = [list(map(int, input().split())) for _ in range(T)]

# Calculate and output the result
print(min_cows_needed(B, required_beans, T, farmers))