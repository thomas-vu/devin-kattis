def find_same_temperature(X, Y):
    if X == 0:
        return "ALL GOOD" if Y != 0 else -float('inf')
    elif Y == 1:
        return "IMPOSSIBLE"
    else:
        return X / (Y - 1)

# Read inputs from stdin
X, Y = map(int, input().split())
result = find_same_temperature(X, Y)
if result == -float('inf'):
    print("ALL GOOD")
elif result is None:
    print("IMPOSSIBLE")
else:
    print("{:.9f}".format(result))