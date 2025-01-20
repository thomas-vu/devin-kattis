def solve(N, A, queries):
    max_product = float('-inf')
    
    for L, R in queries:
        X_candidates = []
        Y_candidates = []
        
        for i in range(L, R - 1):
            X_candidates.append((A[i], i))
        
        for j in range(L + 2, R):
            Y_candidates.append((A[j], j))
        
        X_candidates.sort(reverse=True)
        Y_candidates.sort(reverse=True)
        
        if len(X_candidates) >= 1 and len(Y_candidates) >= 1:
            max_product = max(max_product, A[L] * X_candidates[0][0] * Y_candidates[0][0] * A[R])
        
        if len(X_candidates) >= 2 and len(Y_candidates) >= 1:
            max_product = max(max_product, A[L] * X_candidates[0][0] * X_candidates[1][0] * A[R])
        
        if len(X_candidates) >= 1 and len(Y_candidates) >= 2:
            max_product = max(max_product, A[L] * X_candidates[0][0] * Y_candidates[0][0] * A[R])
        
        if len(X_candidates) >= 2 and len(Y_candidates) >= 2:
            max_product = max(max_product, A[L] * X_candidates[0][0] * X_candidates[1][0] * Y_candidates[0][0] * A[R])
    
    return max_product

# Read input
N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Process queries and output results
for L, R in queries:
    result = solve(N, A, [((L-1), (R-1))])
    print(result)