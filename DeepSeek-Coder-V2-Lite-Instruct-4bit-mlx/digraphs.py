def find_largest_square(forbidden):
    def is_safe(x, y, size):
        for i in range(size):
            for j in range(size):
                if (x + i, y + j) in forbidden:
                    return False
        return True

    n = min(8, int(input()))
    for _ in range(n):
        forbidden.add((ord(input()[0]) - ord('a'), ord(input()[1]) - ord('b')))
    
    size = 0
    while True:
        found = False
        for i in range(16 - size):
            for j in range(16 - size):
                if is_safe(i, j, size + 1):
                    found = True
                    break
            if found:
                break
        else:
            size += 1
            continue
        break
    
    square = [[' ' for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            square[i][j] = chr(ord('a') + (i * size + j) % 26)
    
    for i in range(size):
        print(''.join(square[i]))

# Read input and process each test case
T = int(input())
for _ in range(T):
    n = int(input())
    forbidden = set()
    find_largest_square(forbidden)