def find_available_room(r, booked_rooms):
    available_rooms = set(range(1, r + 1)) - set(booked_rooms)
    return next(iter(available_rooms), "too late")

# Read input
r, n = map(int, input().split())
booked_rooms = [int(input()) for _ in range(n)]

# Output the result
print(find_available_room(r, booked_rooms))