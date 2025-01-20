def find_valid_k(difficulties):
    n = len(difficulties)
    difficulties.sort()
    
    valid_ks = []
    
    for k in range(2, n + 1):
        if n % k == 0:
            valid = True
            for i in range(k):
                for j in range(i + 1, k):
                    if difficulties[i * (n // k)] > difficulties[j * (n // k)]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                valid_ks.append(k)
    
    return valid_ks if valid_ks else [-1]

# Read input from stdin
n = int(input().strip())
difficulties = [int(input().strip()) for _ in range(n)]

# Find and print valid values of k
valid_ks = find_valid_k(difficulties)
for k in valid_ks:
    print(k)