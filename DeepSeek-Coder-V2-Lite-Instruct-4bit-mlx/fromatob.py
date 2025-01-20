def min_operations(a, b):
    operations = 0
    while a != b:
        if a > b:
            a //= 2
        else:
            if b % 2 == 1:
                b -= 1
            else:
                b //= 2
        operations += 1
    return operations

# Read input
a, b = map(int, input().split())
print(min_operations(a, b))