def can_build_closed_track(X, Y):
    # A closed track requires 2 ends for each straight or curved piece.
    # Each X-shaped junction provides 2 ends, and each Y-shaped switch provides 1 end.
    # For a closed track, the total number of ends must be equal to the sum of X and Y.
    # Each straight or curved piece requires 2 ends, and each bridge provides 1 end.
    # However, since the number of bridges is not specified and assumed to be sufficient,
    # we only need to check the balance of ends provided by X and Y.
    
    if (X + Y) % 2 == 1:
        return "impossible"
    else:
        return "possible"

# Read input from stdin
X, Y = map(int, input().split())
result = can_build_closed_track(X, Y)
print(result)