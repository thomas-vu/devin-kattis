def find_items(subset_weights):
    n = len(subset_weights)
    if n == 0:
        return []
    
    # Initialize the list to store possible item weights
    items = [0] * n
    
    # Sort the subset weights to check for consistency
    subset_weights.sort()
    
    # Check if the list is consistent by verifying the weights
    for i in range(1, len(subset_weights)):
        if subset_weights[i] - subset_weights[i-1] >= n:
            return "impossible"
    
    # Backtrack to find the individual item weights
    for i in range(len(subset_weights)):
        weight = subset_weights[i]
        for j in range(n):
            if items[j] == 0 and weight & (1 << j):
                items[j] = weight - (weight & (1 << j))
    
    # Ensure the items are non-negative and in non-decreasing order
    for i in range(1, n):
        if items[i] < items[i-1]:
            return "impossible"
    
    return [item for item in items if item != 0]

# Main function to process input and output the result
def main():
    n = int(input())
    subset_weights = [int(input()) for _ in range(2**n)]
    
    result = find_items(subset_weights)
    if result == "impossible":
        print("impossible")
    else:
        for item in sorted(result):
            print(item)

# Call the main function
main()