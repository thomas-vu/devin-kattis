def min_max_points(n, alice_cards):
    # Sort Alice's cards to simulate the best possible scenario for her
    alice_cards.sort()
    
    # The minimum points Alice can score is when she wins all the matches with her smallest cards
    min_points = sum(1 for i in range(n) if alice_cards[i] > (i + 1))
    
    # The maximum points Alice can score is when she wins all the matches with her largest cards
    max_points = sum(1 for i in range(n) if alice_cards[i] > (2 * n - i))
    
    return min_points + 1, max_points + (n - sum(alice_cards[i] > (2 * n - i) for i in range(n)))

# Read input
n = int(input())
alice_cards = [int(input()) for _ in range(n)]

# Calculate and print the result
min_points, max_points = min_max_points(n, alice_cards)
print(min_points, max_points)