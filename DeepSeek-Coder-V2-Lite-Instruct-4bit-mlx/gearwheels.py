def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    N = int(input())
    T = list(map(int, input().split()))
    
    # dp[i] will store the length of the longest chain ending at gear i
    dp = [1] * N
    # parent[i] will store the index of the previous gear in the chain for gear i
    parent = [-1] * N
    
    # Compute the longest chain ending at each gear
    for i in range(N):
        for j in range(i + 1, N):
            if T[j] % T[i] == 0:
                if dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
                    parent[j] = i
    
    # Find the length of the longest chain
    L = max(dp)
    
    # Collect all chains of length L
    longest_chains = []
    for i in range(N):
        if dp[i] == L:
            chain = []
            while i != -1:
                chain.append(i + 1)
                i = parent[i]
            longest_chains.append(chain[::-1])
    
    # Output the result
    print(L, len(longest_chains))
    for chain in longest_chains:
        print(' '.join(map(str, chain)))

if __name__ == "__main__":
    main()