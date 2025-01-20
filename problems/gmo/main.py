def min_cost_to_insert_gene(apple_dna, swine_gene, costs):
    n = len(apple_dna)
    m = len(swine_gene)
    
    # Define the costs for each character insertion
    cost_A, cost_C, cost_G, cost_T = costs
    
    # Initialize the DP table where dp[i][j] represents the minimum cost to insert swine gene into the first i characters of apple_dna
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    # Base case: no characters from swine_gene to insert (cost is 0)
    for i in range(n + 1):
        dp[i][0] = 0
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if apple_dna[i - 1] == swine_gene[j - 1]:
                # No cost if the characters match
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                # Insert each character with its respective cost and choose the minimum
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + cost_A, dp[i - 1][j] + cost_C, dp[i - 1][j] + cost_G, dp[i - 1][j] + cost_T)
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + cost_A, dp[i][j - 1] + cost_C, dp[i][j - 1] + cost_G, dp[i][j - 1] + cost_T)
    
    # The minimum total cost is the last element in the DP table
    return dp[n][m]

# Read input
apple_dna = input().strip()
swine_gene = input().strip()
costs = list(map(int, input().split()))

# Calculate and print the result
result = min_cost_to_insert_gene(apple_dna, swine_gene, costs)
print(result)