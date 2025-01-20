def find_room_dimensions(R, B):
    # Calculate the possible dimensions of the room
    for L in range(1, int(R**0.5) + 1):
        if R % L == 0:
            W = R // L
            # Check the number of brown blocks
            if (L - 2) * (W - 2) == B:
                return f"{max(L, W)} {min(L, W)}"

# Read input
R, B = map(int, input().split())
print(find_room_dimensions(R, B))