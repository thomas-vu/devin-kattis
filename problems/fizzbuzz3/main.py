def generate_Fi(Y):
    Fi = "F_in_Finals_stands_for_Fizz_Buzz!"
    for _ in range(Y):
        Fi = Fi.replace("F", "F_in_Finals_stands_for_Fizz_Buzz!")
    return Fi

def find_character(X, Y):
    Fi = generate_Fi(Y)
    if X > len(Fi):
        return '?'
    else:
        return Fi[X - 1]

Q = int(input())
results = []
for _ in range(Q):
    X, Y = map(int, input().split())
    results.append(find_character(X, Y))

print(''.join(results))