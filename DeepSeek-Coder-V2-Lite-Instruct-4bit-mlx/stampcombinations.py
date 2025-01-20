def can_mail(clusters, query):
    total = sum(clusters)
    if query == 0 or query > total:
        return "No"
    elif query <= min(clusters):
        return "Yes"
    
    dp = [False] * (query + 1)
    dp[0] = True
    
    for cluster in clusters:
        for j in range(query, cluster - 1, -1):
            if dp[j - cluster]:
                dp[j] = True
    
    return "Yes" if dp[query] else "No"

# Read input
m, n = map(int, input().split())
clusters = list(map(int, input().split()))

# Process queries
for _ in range(n):
    query = int(input())
    print(can_mail(clusters, query))