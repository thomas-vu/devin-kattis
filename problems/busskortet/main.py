def min_transactions(K):
    denominations = [500, 200, 100]
    count = 0
    for denom in denominations:
        while K >= denom:
            K -= denom
            count += 1
    return count

# Read input from stdin
K = int(input().strip())
print(min_transactions(K))