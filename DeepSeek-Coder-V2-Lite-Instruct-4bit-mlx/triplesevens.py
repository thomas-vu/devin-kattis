def is_good(n, wheels):
    for wheel in wheels:
        if '7' not in wheel:
            return False
    return True

n = int(input())
wheels = [set(input().split()) for _ in range(3)]
if is_good(n, wheels):
    print("7" * 3)
else:
    print(0)