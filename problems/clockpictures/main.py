def same_clock_hands(n, hands1, hands2):
    # Normalize the angles to be within [0, 360) degrees for comparison
    def normalize(angles):
        return [angle % 360000 for angle in angles]
    
    # Sort the angles to make comparison easier
    hands1 = sorted(normalize(hands1))
    hands2 = sorted(normalize(hands2))
    
    # Check if the lists are identical after rotation
    for _ in range(n):
        if hands1 == hands2:
            return "possible"
        # Rotate the second list by one position
        hands2 = [hands2[-1]] + hands2[:-1]
    
    return "impossible"

# Read input
n = int(input())
hands1 = list(map(int, input().split()))
hands2 = list(map(int, input().split()))

# Output the result
print(same_clock_hands(n, hands1, hands2))