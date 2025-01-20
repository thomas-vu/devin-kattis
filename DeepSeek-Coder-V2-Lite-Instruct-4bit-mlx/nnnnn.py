def decrypt(L):
    low, high = 0, L
    while low < high:
        mid = (low + high) // 2
        n = str(mid) * mid
        if len(n) == L:
            return mid
        elif len(n) < L:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Read the input
L = int(input())
print(decrypt(L))