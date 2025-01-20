def is_intuitive(a, b):
    for letter in b:
        if letter not in a:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    a = input()
    b = input()
    print(is_intuitive(a, b))