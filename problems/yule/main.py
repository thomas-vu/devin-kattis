def count_yule_lads(N):
    # Initialize the number of Yule Lads that came to town
    yule_lads = 0
    
    # Iterate through each possible Yule Lad (house number)
    for K in range(1, N + 1):
        if N % K == 0:
            # If the house number divides N, it means this Yule Lad visited this house
            yule_lads += 1
    
    # Subtract the first house since it's always on
    yule_lads -= 1
    
    return yule_lads

# Read the number of houses from input
N = int(input())

# Output the number of Yule Lads that came to town
print(count_yule_lads(N))