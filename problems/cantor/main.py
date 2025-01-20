def cantor_set(x):
    while x > 0 and x < 1:
        if '1' in str(x):
            return "NON-MEMBER"
        x *= 3
        if x >= 1:
            x -= 1
    return "MEMBER"

while True:
    try:
        x = float(input())
        print(cantor_set(x))
    except EOFError:
        break