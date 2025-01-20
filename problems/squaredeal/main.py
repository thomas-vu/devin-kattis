def can_form_square(H1, W1, H2, W2, H3, W3):
    # Check all possible orientations of the rectangles
    if (H1 + H2 == W3 and W1 + H3 == W3) or (H1 + H2 == H3 and W1 + W2 == W3):
        return "YES"
    if (H1 + H2 == W3 and W1 + W2 == H3) or (H1 + H2 == H3 and W1 + W2 == W3):
        return "YES"
    if (H1 + H3 == W2 and W1 + H2 == W2) or (H1 + H3 == H2 and W1 + W3 == W2):
        return "YES"
    if (H1 + H3 == W2 and W1 + W3 == H2) or (H1 + H3 == H2 and W1 + W3 == W2):
        return "YES"
    if (H2 + H3 == W1 and W2 + H1 == W1) or (H2 + H3 == H1 and W2 + W3 == W1):
        return "YES"
    if (H2 + H3 == W1 and W2 + W3 == H1) or (H2 + H3 == H1 and W2 + W3 == W1):
        return "YES"
    return "NO"

# Read input
H1, W1 = map(int, input().split())
H2, W2 = map(int, input().split())
H3, W3 = map(int, input().split())

# Determine if the rectangles can be glued to form a square
result = can_form_square(H1, W1, H2, W2, H3, W3)
print(result)