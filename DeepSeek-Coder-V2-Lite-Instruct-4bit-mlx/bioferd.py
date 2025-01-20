def solve(n, preferences):
    from itertools import permutations
    
    for perm in permutations(range(n)):
        valid = True
        seating = [0] * n
        for i, p in enumerate(perm):
            seats = preferences[p]
            valid_seat = False
            for seat in seats:
                if seating[n - seat] == 0:
                    seating[n - seat] = i + 1
                    valid_seat = True
                    break
            if not valid_seat:
                valid = False
                break
        if valid and all(seating):
            return ' '.join(map(str, [seat + 1 for seat in seating]))
    return 'Neibb'

# Read input
n = int(input().strip())
preferences = [list(map(int, input().strip().split()))[1:] for _ in range(n)]

# Solve and print the result
print(solve(n, preferences))