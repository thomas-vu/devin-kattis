def find_position(T, K):
    position = 0
    while T > 1:
        position = (position + K) % T
        if position == 0:
            position = T - 1
        else:
            position -= 1
        T -= 1
    return position + 1

# Read input from standard input
T, K = map(int, input().split())
print(find_position(T, K))