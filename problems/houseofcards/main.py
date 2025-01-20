def min_height(h0):
    h0 = int(h0)
    if h0 <= 4:
        return 5
    # The number of cards in a triangular house of height h is given by the sum of the first h natural numbers
    # which is h * (h + 1) / 2
    def num_cards(h):
        return h * (h + 1) // 2
    
    # Binary search to find the minimum height h such that it is possible to build a tower of height h
    left, right = 5, 10**1000
    while left < right:
        mid = (left + right) // 2
        if num_cards(mid) >= h0:
            right = mid
        else:
            left = mid + 1
    return left

# Example usage
print(min_height("25"))  # Sample Output 1
print(min_height("4245"))  # Sample Output 2