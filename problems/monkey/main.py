def calculate_bringable_smoothie(D, W, C):
    # If the carrying capacity is greater than or equal to the total amount of smoothie,
    # the monkey can carry all the smoothie in one trip.
    if C >= W:
        return W
    
    # If the distance is zero, the monkey can bring all the smoothie immediately.
    if D == 0:
        return W
    
    # The monkey can carry up to 2 containers, each with a maximum capacity of C ml.
    # Therefore, the total amount she can carry at once is 2 * C ml.
    
    # First, calculate the amount of smoothie she can bring in one trip with 2 containers.
    if W <= C * 2:
        # If the total amount of smoothie is less than or equal to twice the carrying capacity,
        # she can carry all the smoothie in one trip with 2 containers.
        return W / (1 + D * (2 / C))
    else:
        # If the total amount of smoothie is more than twice the carrying capacity,
        # she needs to make multiple trips.
        # First trip: 2 containers carrying C ml each, distance D.
        part1 = (C * 2) / (1 + D * (2 / C))
        # Remaining smoothie after the first trip.
        remaining_smoothie = W - (C * 2)
        # Second trip: 1 container carrying the remaining smoothie, distance D.
        part2 = remaining_smoothie / (1 + D * (2 / C))
        # Total smoothie brought in the end.
        return part1 + part2

# Read input
D, W, C = map(int, input().split())

# Calculate and output the result
result = calculate_bringable_smoothie(D, W, C)
print("{:.10f}".format(result))