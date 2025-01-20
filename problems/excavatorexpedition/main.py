def main():
    V, E = map(int, input().split())
    sites = list(input().strip())
    graph = [[] for _ in range(V)]
    
    for _ in range(E):
        F, T = map(int, input().split())
        graph[F].append(T)
    
    # Use dynamic programming to find the maximum happiness
    dp = [0] * V
    dp[0] = 1 if sites[0] == '.' else 0
    
    for i in range(V):
        if dp[i] > 0:
            for neighbor in graph[i]:
                if sites[neighbor] == '.':
                    dp[neighbor] = max(dp[neighbor], dp[i] + 1)
    
    print(dp[-1])

if __name__ == "__main__":
    main()