def can_transport(W, S, C, K):
    if W > K and S > K:
        return "NO"
    total_items = W + S + C
    if total_items <= K:
        return "YES"
    min_needed = max(W - K, S - K, 0)
    if min_needed <= C:
        return "YES"
    else:
        return "NO"

# Read input
W, S, C, K = map(int, input().split())
print(can_transport(W, S, C, K))