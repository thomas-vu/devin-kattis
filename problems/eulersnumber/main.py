def calculate_e(n):
    e = 0.0
    factorial = 1
    for i in range(n + 1):
        if i == 0:
            e += 1
        else:
            factorial *= i
            e += 1 / factorial
    return e

# Example usage:
n = int(input())
print("{:.15f}".format(calculate_e(n)))