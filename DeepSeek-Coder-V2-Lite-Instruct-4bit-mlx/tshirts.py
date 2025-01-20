def tshirt(N, L, H, T):
    # Sort the t-shirts by size
    T.sort()
    
    # Count how many contestants can wear each t-shirt
    count = 0
    for size in T:
        for i in range(N):
            if L[i] <= size <= H[i]:
                count += 1
                break
    
    return count