def min_kp_kr(N, P, D):
    # Find the first position where the sequences differ
    diff_index = -1
    for i in range(N):
        if P[i] != D[i]:
            diff_index = i
            break
    
    if diff_index == -1:
        return (N, N)  # If they are exactly the same, any k is sufficient
    
    # Check for the minimum k_p
    P1 = P[diff_index:] + P[:diff_index]
    D1 = D[diff_index:] + D[:diff_index]
    
    kp = 1
    while P1[kp-1] != D[kp-1]:
        kp += 1
    
    # Check for the minimum k_r
    D2 = D[diff_index:] + D[:diff_index]
    kp = min(kp, N)  # Ensure we don't exceed the number of events
    kr = 1
    while D2[kr-1] != P[kr-1]:
        kr += 1
    
    return (kp, kr)

# Read input
N = int(input())
P = list(map(int, input().split()))
D = list(map(int, input().split()))

# Get the result
kp, kr = min_kp_kr(N, P, D)
print(kp, kr)