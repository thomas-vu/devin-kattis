def check_odd_even(x):
    if x % 2 == 0:
        return f"{x} is even"
    else:
        return f"{x} is odd"

n = int(input())
for _ in range(n):
    x = int(input())
    print(check_odd_even(x))